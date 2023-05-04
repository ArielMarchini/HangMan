def print_menu():
    """
    This function prints the menu to the client.
    :return: None
    """
    print("Please select an option:")
    print("1. Print the list of products")
    print("2. Print the number of products in the list")
    print("3. Check if a product is on the list")
    print("4. Count how many times a product appears")
    print("5. Delete a product from the list")
    print("6. Add a product to the list")
    print("7. Print all invalid products")
    print("8. Remove all duplicates from the list")
    print("9. Exit")


def is_valid_product(product):
    """
    This function check that the product is valid.
    Valid product needs at least 3 letters and contains only alphabetic letters.
    :param product: The product that needs to add.
    :return: False if the product is not valid. otherwise, True.
    :rtype: Boolean.
    """
    if len(product) < 3:
        return False
    for c in product:
        if not c.isalpha():
            return False
    return True


def get_product_index(products, product):
    for i in range(len(products)):
        if products[i] == product:
            return i
    return -1


def print_products(products):
    """
    This function prints all the products.
    :param products: A list of the products.
    :type products: List.
    :return: Nothing.
    :rtype: None.
    """
    print("Products:")
    print(", ".join(products))


def print_num_products(products):
    """
    This function prints the number of products have on the list.
    :param products: A list of the products.
    :type products: List.
    :return: Nothing.
    :rtype: None.
    """
    print("Number of products:", len(products))


def check_product_in_list(products):
    """
    This function get a product name from the client, check if the product is on the list or not and
    print an appropriate message.
    :param products: A list of the products.
    :type products: List.
    :return: Nothing.
    :rtype: None.
    """
    product = input("Enter product name: ")
    if product in products:
        print(product, "is on the list")
    else:
        print(product, "is not on the list")


def check_occurrences_product(products):
    """
    This function get a product name from the client,
    and print the number of times this product is showing in the products list.
    :param products: A list of the products.
    :type products: List.
    :return: Nothing.
    :rtype: None.
    """
    product = input("Enter product name: ")
    count = products.count(product)
    print(product, "appears", count, "times")


def delete_product(products):
    """
    This function get a product name from the client,
    and deletes the  product from products list, only 1 product will delete.
    :param products: A list of the products.
    :type products: List.
    :return: Nothing.
    :rtype: None.
    """
    product = input("Enter product name to delete: ")
    if product in products:
        products.remove(product)
        print(product, "was removed from the list")
    else:
        print(product, "is not on the list")


def add_product(products):
    """
    This function get a product name from the client,
    and adds the product to products list.
    :param products: A list of the products.
    :type products: List.
    :return: Nothing.
    :rtype: None.
    """
    product = input("Enter product name to add: ")
    if is_valid_product(product):
        products.append(product)
        print(product, "was added to the list")
    else:
        print(product, "is an invalid product")


def print_invalid_products(products):
    """
    This function prints all the invalid products in the products list.
    :param products: A list of the products.
    :type products: List.
    :return: Nothing.
    :rtype: None.
    """
    invalid_products = []
    for product in products:
        if not is_valid_product(product):
            invalid_products.append(product)

    if invalid_products:
        print("Invalid products:")
        print(", ".join(invalid_products))
    else:
        print("No invalid products found")


def remove_duplicates(products):
    """
    This function remove all the duplicates products on the list.
    :param products: A list of the products.
    :type products: List.
    :return: Nothing.
    :rtype: None.
    """
    unique_products = []
    for product in products:
        if product not in unique_products:
            unique_products.append(product)
    products.clear()
    products.extend(unique_products)
    print("Duplicates removed")


def main():
    product_str = input("Enter a list of products, separated by commas: ")
    products = product_str.split(",")

    while True:
        print_menu()
        choice = input("Enter your choice (1-9): ")
        if choice == "1":
            print_products(products)
        elif choice == "2":
            print_num_products(products)
        elif choice == "3":
            check_product_in_list(products)
        elif choice == "4":
            check_occurrences_product(products)
        elif choice == "5":
            delete_product(products)
        elif choice == "6":
            add_product(products)
        elif choice == "7":
            print_invalid_products(products)
        elif choice == "8":
            remove_duplicates(products)
        elif choice == "9":
            break


if __name__ == "__main__":
    main()
