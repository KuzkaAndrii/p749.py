class DictStrIntError(Exception):
    def __init__(self, key, value, problem_cod):
        self._key=key
        self._value=value
        self._prob=problem_cod
    def __str__(self):
        if self._prob==0:
            return f"There are problem in key {self._key}"
        else:
            return f"There are problem in value {self._value}"
if __name__=="__main__":
    print("Hello, world!")