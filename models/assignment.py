class Assignment:
    def __init__(self, assignment_id, job_id, employee_id, assignment_date, status = "assigned"):
        self.assignment_id = assignment_id
        self.job_id = job_id
        self.employee_id = employee_id
        self.assignment_date = assignment_date
        self.status = status

    def display_info(self):
        print(f"Assignment ID       :       {self.assignment_id}")
        print(f"Job ID              :       {self.job_id}")
        print(f"Employee ID         :       {self.employee_id}")
        print(f"Assignment Date     :       {self.assignment_date}")
        print(f"Status              :       {self.status}")