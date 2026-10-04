from utils.file_manager import (load_invoices, load_jobs, save_invoices, load_assignments, save_assignments , save_jobs)
from datetime import datetime, timedelta
from models.invoices import Invoice


def invoice_menu():

    while True:
        print("\n")
        print("╔══════════════════════════════════════════════════════════════════════════════╗")
        print("║                                                                              ║")
        print("║                         INVOICES & PAYMENTS                                  ║")
        print("║                                                                              ║")
        print("╠══════════════════════════════════════════════════════════════════════════════╣")
        print("║                                                                              ║")
        print("║        [1]    Create Invoice                                                 ║")
        print("║        [2]    View Invoices                                                  ║")
        print("║        [3]    Search Invoice                                                 ║")
        print("║        [4]    Update Invoice                                                 ║")
        print("║        [5]    Remove Invoice                                                 ║")
        print("║                                                                              ║")
        print("║        [6]    Record Payment                                                 ║")
        print("║        [7]    View Payments                                                  ║")
        print("║        [8]    Search Payment                                                 ║")
        print("║        [9]    Payment Status                                                 ║")
        print("║                                                                              ║")
        print("║        [0]    Back to Main Menu                                              ║")
        print("║                                                                              ║")
        print("╚══════════════════════════════════════════════════════════════════════════════╝")
 
        choice = input("Enter your choice: ")

        if choice == "1":
            create_invoice()
            input("Press Enter to go back to menu: ")
        elif choice == "2":
            view_invoices()
            input("Press Enter to go back to menu: ")
        elif choice == "3":
            search_invoice()
            input("Press Enter to go back to menu: ")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


def create_invoice():
    jobs = load_jobs()

    if not jobs:
        print("No jobs Available. please create a job first.")
        return

    ask_job = input("Enter the job ID to create an invoice for:")
    found = False
    for job in jobs:
        if job['job_id'].lower() == ask_job.lower():
            found = True
            if job['status'].lower() != 'completed':
                print("invoice can only be created for completed jobs.")
                return
            break
    if not found:
        print("Job not found.")
        return

    invoice_amount = float(input("Enter the invoice amount: "))
    invoice_date = datetime.now().strftime("%Y-%m-%d")
    invoice_due_date = (datetime.now() + timedelta(days = 30)).strftime("%Y-%m-%d")

    invoices = load_invoices()
    invoice_number = len(invoices) + 1
    invoice_id = f"INV{invoice_number:03d}"
    invoice = Invoice(
        invoice_id,
        job['job_id'],
        job['customer_id'],
        invoice_amount,
        invoice_date,
        invoice_due_date,
        "unpaid"
    )
    invoice_data = {
    "invoice_id": invoice.invoice_id,
    "job_id": invoice.job_id,
    "customer_id": invoice.customer_id,
    "amount": invoice.amount,
    "invoice_date": invoice.invoice_date,
    "due_date": invoice.due_date,
    "status": invoice.status
    }
    invoices.append(invoice_data)
    save_invoices(invoices)
    print(f"Invoice {invoice.invoice_id} created successfully for Job {job['job_id']} with amount {invoice.amount}.")


def view_invoices():
    invoices = load_invoices()
    if not invoices:
        print("No invoices found.")
        return
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                       INVOICE DIRECTORY                      ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
""")
    for invoice in invoices:
        print("\n────────────────────────────────────────────────────────────────")
        print(f"    Invoice ID: {invoice['invoice_id']}")
        print(f"    Job ID: {invoice['job_id']}")
        print(f"    Customer ID: {invoice['customer_id']}")
        print(f"    Amount: {invoice['amount']}")
        print(f"    Invoice Date: {invoice['invoice_date']}")
        print(f"    Due Date: {invoice['due_date']}")
        print(f"    Status: {invoice['status']}")
        print()

    print("""
╚══════════════════════════════════════════════════════════════╝
                """)


def search_invoice():
    invoices = load_invoices()

    if not invoices:
        print("No invoices found.")
        return

    search_id = input("Enter the invoice ID to search: ").lower().strip()
    found = False
    for invoice in invoices:
        if invoice['invoice_id'].lower() == search_id:
            found = True
            print("\n────────────────────────────────────────────────────────────────")
            print(f"    Invoice ID: {invoice['invoice_id']}")
            print(f"    Job ID: {invoice['job_id']}")
            print(f"    Customer ID: {invoice['customer_id']}")
            print(f"    Amount: {invoice['amount']}")
            print(f"    Invoice Date: {invoice['invoice_date']}")
            print(f"    Due Date: {invoice['due_date']}")
            print(f"    Status: {invoice['status']}")
            print()
            break

    if not found:
        print("Invoice not found.")