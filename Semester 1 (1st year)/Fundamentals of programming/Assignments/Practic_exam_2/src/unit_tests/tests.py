import unittest
from src.domain.domain import Address
from src.services.services import Service
from src.repository.repository import MemoryRepo


class TestDomain(unittest.TestCase):
    def test_address_distance(self):
        address = Address(1, 'Rares', 5, 15, 20)
        x = 15
        y = 20
        self.assertEqual(address.get_distance_to_point(x, y), 0)
        x2 = 20  # 20-15 = 5, 5^2 = 25
        y2 = 20
        self.assertEqual(address.get_distance_to_point(x2, y2), 5)
        x3 = 15
        y3 = 30
        self.assertEqual(address.get_distance_to_point(x3, y3), 10)


class TestService(unittest.TestCase):
    def test_get_all(self):
        repository = MemoryRepo()
        service = Service(repository, 'TestFile')
        self.assertEqual(len(service.get_all_addresses()), 10)
        address = Address(1, 'Mihali', 10, 12, 20)
        # print(service.get_all_addresses()[0])
        self.assertEqual(address.equal_address(service.get_all_addresses()[0]), True)
