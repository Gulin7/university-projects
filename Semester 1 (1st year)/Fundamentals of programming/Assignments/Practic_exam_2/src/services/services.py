from src.repository.repository import MemoryRepo
from src.domain.domain import Address


class Service:
    def __init__(self, repo: MemoryRepo, file_name):
        self.__repo = repo
        self.__file_name = file_name
        with open(self.__file_name, "r") as f:
            f.seek(0)
            file_lines = f.read().strip().split('\n')
        for line in file_lines:
            address_details = line.split(',')
            try:
                address = Address(int(address_details[0]), address_details[1], int(address_details[2]),
                                  int(address_details[3]), int(address_details[4]))
                self.__repo.add_address_to_repo(address)
            except:
                pass
        f.close()

    def add_address(self, address: Address):
        """
        Adds a new address to the service.

        :param address: address
        :return:
        """
        self.__repo.add_address_to_repo(address)

    def get_all_addresses(self):
        """
        Gets a list of all the addresses.

        :return: list of all the addresses
        """
        return self.__repo.get_all_addresses()

    def find_perfect_station(self):
        minim_distance = 100000000000
        best_x = 1
        best_y = 1
        for x in range(-100, 100):

            for y in range(-100, 100):
                total_distance = 0
                for address in self.get_all_addresses():
                    total_distance += address.get_distance_to_point(x, y)
                if total_distance < minim_distance:
                    minim_distance = total_distance
                    best_x = x
                    best_y = y
                    #print(x)
                    #print(y)
        return best_x, best_y

    def check_existing_id(self, id):
        """
        Checks if we have an address with that id.

        :param id: id, int
        :return: bool
        """
        for address in self.get_all_addresses():
            if address.get_id() == id:
                return True
        return False
