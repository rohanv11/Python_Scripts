import threading


class dbConn:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__new__(cls)

        return cls.__instance


s1 = dbConn()

# this line will throw an error, because of name mangling the interpretter names the __instance as _dbConn__instance
# just a tiny way to make it private, so direct __instance access is not allowed
# print("s1", s1.__instance)

print("__instance access (name mangling by python interpretter)", dbConn._dbConn__instance)
s2 = dbConn()

print(s1 == s2)


# TODO: 1. CREATE A LOGGER IN SINGLETON DP..
#       2. TEST the above code with and without locks in Multi threading env...
