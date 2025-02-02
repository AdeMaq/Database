import mysql.connector

def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="W7301@jqir#",
            database="db"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_customer(conn, name, email, address, phone):
    cursor = conn.cursor()
    query = "INSERT INTO Customer (customerName, customerEmail, customerAddress, customerPhoneNumber) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, email, address, phone))
    conn.commit()

def get_customers(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Customer")
    return cursor.fetchall()

def update_customer(conn, customer_id, name, email, address, phone):
    cursor = conn.cursor()
    query = "UPDATE Customer SET customerName = %s, customerEmail = %s, customerAddress = %s, customerPhoneNumber = %s WHERE customerID = %s"
    cursor.execute(query, (name, email, address, phone, customer_id))
    conn.commit()

def delete_customer(conn, customer_id):
    cursor = conn.cursor()
    query = "DELETE FROM Customer WHERE customerID = %s"
    cursor.execute(query, (customer_id,))
    conn.commit()

def create_category(conn, name, description):
    cursor = conn.cursor()
    query = "INSERT INTO Category (categoryName, description) VALUES (%s, %s)"
    cursor.execute(query, (name, description))
    conn.commit()

def get_categories(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Category")
    return cursor.fetchall()

def update_category(conn, category_id, name, description):
    cursor = conn.cursor()
    query = "UPDATE Category SET categoryName = %s, description = %s WHERE categoryID = %s"
    cursor.execute(query, (name, description, category_id))
    conn.commit()

def delete_category(conn, category_id):
    cursor = conn.cursor()
    query = "DELETE FROM Category WHERE categoryID = %s"
    cursor.execute(query, (category_id,))
    conn.commit()

def create_supplier(conn, name, email, phone):
    cursor = conn.cursor()
    query = "INSERT INTO Supplier (supplierName, contactEmail, phone) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, phone))
    conn.commit()

def get_suppliers(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Supplier")
    return cursor.fetchall()

def update_supplier(conn, supplier_id, name, email, phone):
    cursor = conn.cursor()
    query = "UPDATE Supplier SET supplierName = %s, contactEmail = %s, phone = %s WHERE supplierID = %s"
    cursor.execute(query, (name, email, phone, supplier_id))
    conn.commit()

def delete_supplier(conn, supplier_id):
    cursor = conn.cursor()
    query = "DELETE FROM Supplier WHERE supplierID = %s"
    cursor.execute(query, (supplier_id,))
    conn.commit()

def create_product(conn, name, description, price, quantity, category_id, supplier_id):
    cursor = conn.cursor()
    query = "INSERT INTO Product (productName, description, price, stockQuantity, categoryID, supplierID) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (name, description, price, quantity, category_id, supplier_id))
    conn.commit()

def get_products(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Product")
    return cursor.fetchall()

def update_product(conn, product_id, name, description, price, quantity, category_id, supplier_id):
    cursor = conn.cursor()
    query = "UPDATE Product SET productName = %s, description = %s, price = %s, stockQuantity = %s, categoryID = %s, supplierID = %s WHERE productID = %s"
    cursor.execute(query, (name, description, price, quantity, category_id, supplier_id, product_id))
    conn.commit()

def delete_product(conn, product_id):
    cursor = conn.cursor()
    query = "DELETE FROM Product WHERE productID = %s"
    cursor.execute(query, (product_id,))
    conn.commit()


def create_order(conn, customer_id, status):
    cursor = conn.cursor()
    query = "INSERT INTO Orders (customerID, orderDate, orderStatus) VALUES (%s, NOW(), %s)"
    cursor.execute(query, (customer_id, status))
    conn.commit()
    return cursor.lastrowid

def get_orders(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Orders")
    return cursor.fetchall()

def update_order_status(conn, order_id, status):
    cursor = conn.cursor()
    query = "UPDATE Orders SET orderStatus = %s WHERE orderID = %s"
    cursor.execute(query, (status, order_id))
    conn.commit()

def delete_order(conn, order_id):
    cursor = conn.cursor()
    query = "DELETE FROM Orders WHERE orderID = %s"
    cursor.execute(query, (order_id,))
    conn.commit()

def add_order_item(conn, order_id, product_id, quantity):
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM Product WHERE productID = %s", (product_id,))
    price = cursor.fetchone()[0]
    total_price = price * quantity
    query = "INSERT INTO OrderItem (orderID, productID, purchaseQuantity, totalPrice) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (order_id, product_id, quantity, total_price))
    conn.commit()

def get_order_items(conn, order_id):
    cursor = conn.cursor()
    query = "SELECT * FROM OrderItem WHERE orderID = %s"
    cursor.execute(query, (order_id,))
    return cursor.fetchall()

def update_order_item(conn, order_item_id, quantity):
    cursor = conn.cursor()
    cursor.execute("SELECT productID FROM OrderItem WHERE orderItemID = %s", (order_item_id,))
    product_id = cursor.fetchone()[0]
    cursor.execute("SELECT price FROM Product WHERE productID = %s", (product_id,))
    price = cursor.fetchone()[0]
    total_price = price * quantity
    query = "UPDATE OrderItem SET purchaseQuantity = %s, totalPrice = %s WHERE orderItemID = %s"
    cursor.execute(query, (quantity, total_price, order_item_id))
    conn.commit()

def delete_order_item(conn, order_item_id):
    cursor = conn.cursor()
    query = "DELETE FROM OrderItem WHERE orderItemID = %s"
    cursor.execute(query, (order_item_id,))
    conn.commit()

def create_transaction(conn, order_id, amount, payment_method, status):
    cursor = conn.cursor()
    query = "INSERT INTO Transactions (orderID, totalAmount, paymentMethod, status) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (order_id, amount, payment_method, status))
    conn.commit()

def get_transactions(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Transactions")
    return cursor.fetchall()

def update_transaction_status(conn, transaction_id, status):
    cursor = conn.cursor()
    query = "UPDATE Transactions SET status = %s WHERE transactionID = %s"
    cursor.execute(query, (status, transaction_id))
    conn.commit()

def delete_transaction(conn, transaction_id):
    cursor = conn.cursor()
    query = "DELETE FROM Transactions WHERE transactionID = %s"
    cursor.execute(query, (transaction_id,))
    conn.commit()

def create_delivery(conn, order_id, delivery_date, status, delivery_person, customer_address):
    cursor = conn.cursor()
    query = "INSERT INTO Delivery (orderID, deliveryDate, status, deliveryPerson, customerAddress) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (order_id, delivery_date, status, delivery_person, customer_address))
    conn.commit()

def get_deliveries(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Delivery")
    return cursor.fetchall()

def update_delivery_status(conn, delivery_id, status):
    cursor = conn.cursor()
    query = "UPDATE Delivery SET status = %s WHERE deliveryID = %s"
    cursor.execute(query, (status, delivery_id))
    conn.commit()

def delete_delivery(conn, delivery_id):
    cursor = conn.cursor()
    query = "DELETE FROM Delivery WHERE deliveryID = %s"
    cursor.execute(query, (delivery_id,))
    conn.commit()

def create_user_auth(conn, customer_id, username, password):
    cursor = conn.cursor()
    query = "INSERT INTO UserAuth (customerID, username, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (customer_id, username, password))
    conn.commit()

def authenticate_user(conn, username, password):
    cursor = conn.cursor()
    query = "SELECT customerID FROM UserAuth WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    return result[0] if result else None

def place_order(conn, customer_id, items, payment_method, delivery_person, customer_address):
    order_id = create_order(conn, customer_id, 'pending')
    total_amount = 0
    for item in items:
        add_order_item(conn, order_id, item['product_id'], item['quantity'])
        total_amount += item['quantity'] * get_product_price(conn, item['product_id'])
    create_transaction(conn, order_id, total_amount, payment_method, 'completed')
    create_delivery(conn, order_id, 'pending', delivery_person, customer_address)
    print("Order placed successfully!")

def get_product_price(conn, product_id):
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM Product WHERE productID = %s", (product_id,))
    return cursor.fetchone()[0]


def view_products(conn):
    products = get_products(conn)
    for product in products:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[3]}, Stock: {product[4]}, Category ID: {product[5]}, Supplier ID: {product[6]}")


def main_menu(conn):
    while True:
        print("\nE-commerce Platform")
        print("1. View Products")
        print("2. Add Customer")
        print("3. Place Order")
        print("4. View Orders")
        print("5. Update Order Status")
        print("6. Manage Transactions")
        print("7. Manage Deliveries")
        print("8. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            view_products(conn)
        elif choice == '2':
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            address = input("Enter customer address: ")
            phone = input("Enter customer phone number: ")
            create_customer(conn, name, email, address, phone)
        elif choice == '3':
            customer_id = input("Enter customer ID: ")
            items = []
            while True:
                product_id = input("Enter product ID: ")
                quantity = int(input("Enter quantity: "))
                items.append({'product_id': product_id, 'quantity': quantity})
                more = input("Add more items? (y/n): ")
                if more.lower() != 'y':
                    break
            payment_method = input("Enter payment method: ")
            delivery_person = input("Enter delivery person: ")
            customer_address = input("Enter customer address: ")
            place_order(conn, customer_id, items, payment_method, delivery_person, customer_address)
        elif choice == '4':
            orders = get_orders(conn)
            for order in orders:
                print(order)
        elif choice == '5':
            order_id = input("Enter order ID: ")
            status = input("Enter new status: ")
            update_order_status(conn, order_id, status)
        elif choice == '6':
            transactions = get_transactions(conn)
            for transaction in transactions:
                print(transaction)
        elif choice == '7':
            deliveries = get_deliveries(conn)
            for delivery in deliveries:
                print(delivery)
        elif choice == '8':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    conn = connect_to_db()
    if conn:
        main_menu(conn)
        conn.close()
    else:
        print("Failed to connect to the database.")
