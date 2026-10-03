class Invoice:
    def __init__(self, invoice_id, job_id, customer_id, amount, invoice_date, due_date, status):
        self.invoice_id = invoice_id
        self.job_id = job_id
        self.customer_id = customer_id
        self.amount = amount
        self.invoice_date = invoice_date
        self.due_date = due_date
        self.status = status

    def display_invoice(self):
        print(f"Invoice ID: {self.invoice_id}")
        print(f"Job ID: {self.job_id}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Amount: {self.amount}")
        print(f"Invoice Date: {self.invoice_date}")
        print(f"Due Date: {self.due_date}")
        print(f"Status: {self.status}")