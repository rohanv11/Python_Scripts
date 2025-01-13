import unittest
import tempfile
import os
from logger import LoggerImpl, LogLevel
from pathlib import Path


class LoggerTest(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_log_file = None

        LoggerImpl.reset_instance()
        self.temp_log_file = Path(
            os.path.join(self.temp_dir.name, "test_log.txt")
        )

    def test_get_instance_method(self):
        instance = LoggerImpl.get_instance()
        self.assertIsNotNone(
            instance, "If get_instance() is called, it should return a non-null instance"
        )

    def test_singleton_behavior(self):
        instance1 = LoggerImpl.get_instance()
        self.assertIsNotNone(
            instance1,
            "If get_instance() is called, it should return a non-null instance",
        )
        instance2 = LoggerImpl.get_instance()
        self.assertIs(
            instance1,
            instance2,
            "If get_instance() is called multiple times, it should return the same instance",
        )

    def test_reset_instance_method(self):
        instance1 = LoggerImpl.get_instance()
        self.assertIsNotNone(
            instance1,
            "If get_instance() is called, it should return a non-null instance",
        )
        LoggerImpl.reset_instance()
        instance2 = LoggerImpl.get_instance()
        self.assertIsNot(
            instance1,
            instance2,
            "If reset_instance() is called, get_instance() should return a new instance",
        )

    def test_set_log_file(self):
        instance = LoggerImpl.get_instance()
        self.assertIsNotNone(
            instance, "If get_instance() is called, it should return a non-null instance"
        )
        instance.set_log_file(str(self.temp_log_file))
        self.assertEqual(
            str(self.temp_log_file),
            instance.get_log_file(),
            "After setting log file, get_log_file() should return the same file path",
        )

    def test_log(self):
        instance = LoggerImpl.get_instance()
        self.assertIsNotNone(
            instance, "If get_instance() is called, it should return a non-null instance"
        )
        instance.set_log_file(str(self.temp_log_file))
        message = "Test log message"
        instance.log(LogLevel.INFO, message)
        instance.flush()
        with open(self.temp_log_file, "r") as file:
            lines = file.readlines()
            print(lines)
            self.assertIn(message, lines[-1],
                          "The logged message should appear in the log file")

    def test_flush_method(self):
        instance = LoggerImpl.get_instance()
        self.assertIsNotNone(
            instance, "If get_instance() is called, it should return a non-null instance"
        )
        instance.set_log_file(str(self.temp_log_file))

        level = LogLevel.INFO
        message = "Test log message"

        instance.log(level, message)
        instance.flush()

        # Verify that the log contents are flushed to the log file
        with open(self.temp_log_file, "r") as file:
            log_contents = file.read()
            self.assertIn(
                message, log_contents, "Log message should be present in the log file after flush"
            )

    def test_close(self):
        instance = LoggerImpl.get_instance()
        self.assertIsNotNone(
            instance, "If get_instance() is called, it should return a non-null instance"
        )
        instance.set_log_file(str(self.temp_log_file))
        instance.close()
        # Check if closing causes no error (no assertions)

if __name__ == "__main__":
    unittest.main()
