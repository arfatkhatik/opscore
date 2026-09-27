from models.customers import Customer
from utils.file_manager import save_customer,load_customers
def customer_menu():

    while True:
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                                                              ║")
        print("║                    CUSTOMER MANAGEMENT                       ║")
        print("║                                                              ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print("║                                                              ║")
        print("║      [1]   Add Customer                                      ║")
        print("║      [2]   View Customers                                    ║")
        print("║      [3]   Search Customer                                   ║")
        print("║      [4]   Update Customer                                   ║")
        print("║      [5]   Remove Customer                                   ║")
        print("║                                                              ║")
        print("║      [0]   Back to Main Menu                                 ║")
        print("║                                                              ║")
        print("╚══════════════════════════════════════════════════════════════╝")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_customer()
            input("press Enter to go back menu: ")

        elif choice == "2":
            print("View Customers selected.")

        elif choice == "3":
            print("Search Customer selected.")

        elif choice == "4":
            print("Update Customer selected.")

        elif choice == "5":
            print("Remove Customer selected.")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

def add_customer():
    customer_id = input("Enter customer ID: ")
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone: ")
    address = input("Enter customer address: ")
    

    customer = Customer(customer_id, name, email, phone, address, status)

    customer_data = {
        "customer_id": customer.customer_id,
        "name": customer.name,
        "email": customer.email,
        "phone": customer.phone,
        "address": customer.address,
        "status": customer.status
    }

    customers = load_customers()
    customers.append(customer_data)
    save_customer(customers)
    print("Customer added successfully.")