class CalcNumber:
    def __init__(self):
        self.__value = ""

    def __add__(self, numberToAdd):
        return self.__value + str(numberToAdd)
