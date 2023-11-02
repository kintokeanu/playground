#!/usr/bin/python3
"""simple program that allows users to add items to a shopping cart and view the items in the cart."""
class ShoppingCart:
    """a shopping cart class"""
    def __init__(self):
        """initialize the cart with an empty list of items"""
        self.items = []

    def add_item(self, item):
        """
        Add an item to the cart.

        >>> cart = ShoppingCart()
        >>> cart.add_item('Item 1')
        Added 'Item 1' to the cart.
        >>> cart.add_item('Item 2')
        Added 'Item 2' to the cart.

        """
        self.items.append(item)
        print(f"Added '{item}' to the cart.")

    def view_cart(self):
        """
        View the items in the cart.

        >>> cart = ShoppingCart()
        >>> cart.add_item('Item 1')
        Added 'Item 1' to the cart.
        >>> cart.view_cart()
        Items in the cart:
        1. Item 1
        Total items: 1
        >>> cart.add_item('Item 2')
        Added 'Item 2' to the cart.
        >>> cart.view_cart()
        Items in the cart:
        1. Item 1
        2. Item 2
        Total items: 2
        """
        print("Items in the cart:")
        # the error that was causing only one item to be displayed was the if statement below
        # if self.items:
        #     print(f"1. {self.items[0]}")
        # fixed it with this for loop that iterates through the list and prints each item
        for index, item in enumerate(self.items, 1):
            print(f"{index}. {item}")
        print("Total items:", len(self.items))


def main():
    """main function"""
    cart = ShoppingCart()

    while True:
        print("\nChoose an option:")
        print("1. Add item to cart")
        print("2. View cart")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            cart.add_item(item)
        elif choice == '2':
            cart.view_cart()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    """run the doctests and then the main function"""
    import doctest
    doctest.testmod()
    main()
