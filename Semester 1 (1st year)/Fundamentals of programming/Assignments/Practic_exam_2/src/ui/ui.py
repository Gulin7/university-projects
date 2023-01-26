from src.services.services import Service
from src.domain.domain import Address


class Ui:
    def __init__(self, service: Service):
        self.__service = service

    def get_service(self):
        return self.__service

    def set_service(self, service):
        self.__service = service

    def get_command(self):
        while True:
            try:
                command = int(input('Enter a command: '))
                if command > 0 and command < 6:
                    return command
                else:
                    print('Invalid command!')
            except ValueError:
                print('Invalid command')

    def show_menu(self):
        print("""
1. Add address
2. Display all addresses
3. Determine where to put taxi station
4. Determine taxi station
5. Exit""")

    def add_address(self):
        id = 0
        name = 0
        number = 0
        x = 0
        y = 0
        while True:
            try:
                id = int(input('Enter id: '))
                name = input('Enter name: ')
                number = int(input('Enter number: '))
                x = int(input('Enter x: '))
                y = int(input('Enter y: '))
                if self.__service.check_existing_id(id):
                    print('Existing id!')
                elif x > 100 or y > 100 or x < -100 or y < -100:
                    print('Invalid coordinates!')
                elif id < 0:
                    print('Invalid id!')
                elif len(name) < 3:
                    print('Invalid name!')
                else:
                    address = Address(id, name, number, x, y)
                    self.__service.add_address(address)
                    break
            except ValueError as ve:
                print('Invalid address!', ve)
            except:
                print('Invalid address!')

    def display(self):
        for address in self.__service.get_all_addresses():
            print(address)

    def place_station(self):
        while True:
            try:
                x = int(input('Enter an x: '))
                y = int(input('Enter an y: '))
                distance = int(input('Enter a distance: '))
                break
            except ValueError as ve:
                print('Invalid values!', ve)
        for address in self.__service.get_all_addresses():
            if address.get_distance_to_point(x, y) < distance:
                print(f'An address at distance < {distance} to the given point is: ')
                print(address)

    def find_perfect_station(self):
        best_x, best_y = self.__service.find_perfect_station()
        print(f'The best spot is at coordinates:'
              f'x = {best_x} and y = {best_y}')

    def start(self):
        while True:
            self.show_menu()
            command = self.get_command()
            if command == 5:
                print('You left.')
                break
            elif command == 1:
                self.add_address()
            elif command == 2:
                self.display()
            elif command == 3:
                self.place_station()
            elif command == 4:
                self.find_perfect_station()
