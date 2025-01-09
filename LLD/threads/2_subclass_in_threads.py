import threading

class Adder(threading.Thread):
    # TODO: implement the constructor
    def __init__(self, num1, num2):
        super() #.__init__()
        self.num1 = num1
        self.num2 = num2



    # TODO: Implement the run method
    def run(self):
        print(self.num1 + self.num2)


class Client:
    @staticmethod
    def main():
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        # TODO: create a thread of Adder class and add num1 and num2
        adder_thread = Adder(num1, num2)
        adder_thread.start()
        adder_thread.join()


if __name__ == "__main__":
    Client.main()
    