products = {
    1: {"name": "Laptop", "price": 45000, "category": "Electronics"},
    2: {"name": "Mobile", "price": 20000, "category": "Electronics"},
    3: {"name": "Rice", "price": 1200, "category": "Grocery"},
    4: {"name": "Shirt", "price": 1800, "category": "Clothing"}
}

allowed_categories = {"Electronics", "Grocery", "Clothing"}

def show_products():
    print("\nAvailable Products:")
    for pid, p in products.items():
        print(f"{pid} - {p['name']} | ₹ {p['price']} | {p['category']}")

def admin_panel():
    while True:
        print("\n--- ADMIN PANEL ---")
        print("1. View Products")
        print("2. Add Product")
        print("3. Exit Admin Panel")
        choice = input("Choose an option: ")

        if choice == "1":
            show_products()

        elif choice == "2":
            pid = int(input("Enter new product ID: "))
            if pid in products:
                print("Product ID already exists!")
                continue

            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            category = input("Enter category (Electronics/Grocery/Clothing): ")

            if category not in allowed_categories:
                print("Invalid category!")
                continue

            products[pid] = {"name": name, "price": price, "category": category}
            print("Product added successfully!")

        elif choice == "3":
            break

        else:
            print("Invalid choice!")

def customer_panel():
    name = input("\nEnter your name: ")
    cart = {}
    categories = set()
    total = 0

    show_products()

    while True:
        pid = input("\nEnter product ID to add (or 'done' to checkout): ")
        if pid.lower() == "done":
            break

        pid = int(pid)
        if pid not in products:
            print("Invalid Product ID!")
            continue

        qty = int(input("Enter quantity: "))
        product = products[pid]

        cart[pid] = cart.get(pid, 0) + qty
        categories.add(product["category"])
        total += product["price"] * qty

    if not cart:
        print("Cart is empty!")
        return

    payment = input("\nEnter payment method (UPI/Card/COD): ")

    status = "Order Confirmed"
    discount = 0

    if total >= 5000:
        discount = 20
    elif total >= 2000:
        discount = 10

    if payment == "Card" and total > 30000:
        discount += 5

    if payment == "COD" and "Electronics" in categories:
        status = "Order Not Allowed"

    final_amount = total - (total * discount / 100)

    print("\n==============================")
    print("PURCHASE SUMMARY")
    print("==============================")
    print(f"Customer : {name}\n")
    print("Items:")
    for pid, qty in cart.items():
        p = products[pid]
        print(f"{p['name']} x {qty} → ₹ {p['price'] * qty}")

    print(f"\nCategories : {categories}")
    print(f"Payment    : {payment}")
    print(f"\nCart Total : {total}")
    print(f"Discount   : {discount}%")
    print(f"Final Pay  : {final_amount}")
    print(f"Status     : {status}")
    print("==============================")

while True:
    print("\nSMART SHOPPING SYSTEM")
    print("1. Admin Panel")
    print("2. Customer Panel")
    print("3. Exit")
    option = input("Choose an option: ")

    if option == "1":
        admin_panel()
    elif option == "2":
        customer_panel()
    elif option == "3":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice!")
