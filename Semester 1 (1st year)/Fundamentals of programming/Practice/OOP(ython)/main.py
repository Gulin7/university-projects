from domain.entities import Item

if __name__ == '__main__':
    item = Item("iPhone69", 5000, 10)
    print(type(item))
    print(f"""Name: {item.get_name()};
Price: {item.get_price()};
Quantity: {item.get_quantity()};""")
