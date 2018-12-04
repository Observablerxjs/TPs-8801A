class ReadWrite:
    @staticmethod
    def read(path):
        file = open(path, 'r')
        return file.readlines()

    @staticmethod
    def write(path, data):
        file = open(path, 'a+')
        file.write(data + '\n')
        file.close()

    