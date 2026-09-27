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
            view_customers()
            input("press Enter to go back menu: ")

        elif choice == "3":
            search_customer()
            input("press Enter to go back menu: ")

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
    

    customer = Customer(customer_id, name, email, phone, address)

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


def view_customers():
    customers = load_customers()

    if not customers:
        print("No Customer Found.")
        return
    
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                                                              ║")
    print("║                    CUSTOMER DIRECTORY                        ║")
    print("║                                                              ║")
    print("╠══════════════════════════════════════════════════════════════╣")

    for customer in customers:
        print(f"\n    Customer ID:            {customer['customer_id']}")
        print(f"    Customer Name:          {customer['name']}")
        print(f"    Customer Email:         {customer['email']}")
        print(f"    Customer Phone:         {customer['phone']}")
        print(f"    Customer Address:       {customer['address']}")
        print(f"    Customer Status:        {customer['status']}")
        print("\n────────────────────────────────────────────────────────────────")
    print("\n╚══════════════════════════════════════════════════════════════╝")


def search_customer():
    customers = load_customers()

    if not customers:
        print("No customer found.")
        return

    search_id = input("Enter customer Id to search: ")

    for customer in customers:
        if customer['customer_id'].lower() == search_id:
            print("Customer found.")
            print("────────────────────────────────────────────────────────────────")
            print(f"Customer ID :          {customer['customer_id']}")
            print(f"Name        :          {customer['name']}")
            print(f"Email       :          {customer['email']}")
            print(f"Phone       :          {customer['phone']}")
            print(f"Address     :          {customer['address']}")
            print(f"Status      :          {customer['status']}")
            print("────────────────────────────────────────────────────────────────")
            return

    print("Customer not found.")