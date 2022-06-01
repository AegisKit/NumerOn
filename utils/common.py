class Common:
    @staticmethod
    def checkNumForm(array):
        if len(array) != 3 or len(array) != len(set(array)):
            return False
        return True