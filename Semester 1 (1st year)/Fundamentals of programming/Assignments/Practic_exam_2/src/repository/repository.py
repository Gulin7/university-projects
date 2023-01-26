from src.domain.domain import Address


class MemoryRepo:
    """
        MEMORY_REPO C.R.U.D. OPERATIONS
    """

    def __init__(self):
        """ LIST OF ALL ADDRESSES"""
        self.__repo = list()

    def add_address_to_repo(self, address: Address):
        """
        Adds an address to the repo.

        :param address: address
        :return: none
        """
        if address in self.__repo:
            raise ValueError("existing entity!")
        self.__repo.append(address)

    def number_of_addresses(self):
        """
        :return: Number of addressess.
        """
        return len(self.__repo)

    def get_all_addresses(self):
        """
        Gets all the addresses from the repo.

        :return: a list of all the addresses
        """
        return list(self.__repo)

    def search_address_in_repo(self, address: Address):
        """
        Searches for an address in the repo.

        :param address: address
        :return:
        """
        repo_aux = self.get_all_addresses()
        for _address in repo_aux:
            if _address.equal_address(address):
                return _address
        raise ValueError('address not found!')

    def set_addresses(self, new_list):
        """
        Sets a new list of addresses

        :param new_list: list of addresses
        :return: none
        """
        self.__repo = list(new_list)
