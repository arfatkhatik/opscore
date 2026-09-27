class Customer:

    def __init__(self, customer_id, name, email, phone, address, status = "active" ):
        
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.status = status

    def display_info(self):
        print(f"Customer ID:            {self.customer_id}")
        print(f"Customer Name :         {self.name}")
        print(f"Customer Email:         {self.email}")
        print(f"Customer Phone:         {self.phone}")
        print(f"Customer Address:       {self.address}")
        print(f"Customer Status:        {self.status}")
        