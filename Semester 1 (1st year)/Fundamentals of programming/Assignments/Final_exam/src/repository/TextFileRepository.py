from src.repository.Repository import Repository


class TextFileRepository(Repository):
    def __init__(self, file_name):
        Repository.__init__(self)
        self.__file_name = file_name

    def set_file(self, file_name):
        self.__file_name = file_name

    def read_from_file(self):
        new_board = []
        with open(self.__file_name, "r") as file:
            for line in file:
                line.strip().split(' ')
                new_line = []
                for i in line:
                    if i != '\n':
                        new_line.append(int(i))
                new_board.append(new_line)
        Repository.set_board(self, new_board)

    def write_to_file(self):
        with open(self.__file_name, "w") as file:
            for line in self.get_board():
                write_line = ''
                for i in range(8):
                    write_line = write_line + str(line[i])
                write_line = write_line + '\n'
                file.write(write_line)
