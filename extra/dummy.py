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


def create_product(conn, name, description, price, quantity, category_id, supplier_id):
    cursor = conn.cursor()
    query = "INSERT INTO Product (productName, description, price, stockQuantity, categoryID, supplierID) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (name, description, price, quantity, category_id, supplier_id))
    conn.commit()

def get_products(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Product")
    return cursor.fetchall()

def update_product(conn, product_id, name, description, price, quantity):
    cursor = conn.cursor()
    query = "UPDATE Product SET productName = %s, description = %s, price = %s, stockQuantity = %s WHERE productID = %s"
    cursor.execute(query, (name, description, price, quantity, product_id))
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


def place_order(conn, customer_id, items):
    order_id = create_order(conn, customer_id, 'pending')
    for item in items:
        add_order_item(conn, order_id, item['product_id'], item['quantity'])
    print("Order placed successfully!")

def add_order_item(conn, order_id, product_id, quantity):
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM Product WHERE productID = %s", (product_id,))
    price = cursor.fetchone()[0]
    total_price = price * quantity
    query = "INSERT INTO OrderItem (orderID, productID, purchaseQuantity, totalPrice) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (order_id, product_id, quantity, total_price))
    conn.commit()


def view_products(conn):
    products = get_products(conn)
    for product in products:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[3]}, Stock: {product[4]}")



def main_menu(conn):
    while True:
        print("\nE-commerce Platform")
        print("1. View Products")
        print("2. Add Customer")
        print("3. Place Order")
        print("4. Exit")
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
            place_order(conn, customer_id, items)
        elif choice == '4':
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


