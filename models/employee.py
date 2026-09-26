class Employee:

    company = "OPSCORE"

    def __init__(
        self,
        employee_id,
        name,
        email,
        phone,
        department,
        role,
        salary,
        status="active"
    ):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.phone = phone
        self.department = department
        self.role = role
        self.salary = salary
        self.status = status

    def display_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name:        {self.name}")
        print(f"Email:       {self.email}")
        print(f"Phone:       {self.phone}")
        print(f"Department:  {self.department}")
        print(f"Role:        {self.role}")
        print(f"Salary:      {self.salary}")
        print(f"Status:      {self.status}")
        print(f"Company:     {self.company}")