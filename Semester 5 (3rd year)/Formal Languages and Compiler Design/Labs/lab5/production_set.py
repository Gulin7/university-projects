class ProductionSet:

    def __init__(self):
        self.__productions = dict()

    def get_all(self):
        return self.__productions

    def __getitem__(self, key):
        return self.__productions[key]

    def __setitem__(self, key, value):
        self.__productions[key] = value

    def __len__(self):
        return len(self.__productions)

    def keys(self):
        return self.__productions.keys()

    def __str__(self):
        prod_str = ""

        for key in self.__productions.keys():
            for k in key:
                prod_str += str(k)

            prod_str += " -> "

            for v in self.__productions[key]:
                for v1 in v:
                    prod_str += str(v1)
                prod_str += " | "

            prod_str = prod_str[:-3]
            prod_str += "\n"

        return prod_str[:-1]