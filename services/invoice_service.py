from utils.file_manager import (load_invoices, load_jobs, save_invoices, load_payments, save_payments)
from datetime import datetime, timedelta
from models.invoices import Invoice
from services.system_management import log_event


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
        elif choice == "4":
            update_invoice()
            input("Press Enter to go back to menu: ")
        elif choice == "5":
            remove_invoice()
            input("Press Enter to go back to menu: ")
        elif choice == "6":
            record_payment()
            input("Press Enter to go back to menu: ")
        elif choice == "7":
            view_payments()
            input("Press Enter to go back to menu: ")
        elif choice == "8":
            search_payment()
            input("Press Enter to go back to menu: ")
        elif choice == "9":
            payment_status()
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
    log_event(f"Invoice {invoice_id} created")

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


def update_invoice():
    invoices = load_invoices()
    if not invoices:
        print("No invoices found.")
        return

    search_id = input("Enter the invoice ID to update: ").lower().strip()

    found = False
    for invoice in invoices:
        if invoice['invoice_id'].lower() == search_id:
            found = True
            print(f"Current Amount: {invoice['amount']}")
            new_amount = input("Enter new amount (or press Enter to keep current): ")
            if new_amount:
                invoice['amount'] = float(new_amount)
                print(f"Invoice {invoice['invoice_id']} updated successfully.")
            else:
                print("No changes made in invoice amount.")
            print(f"Current Status: {invoice['status']}")

            new_status = input(
                "Enter new status (paid/unpaid/overdue) "
                "(or press Enter to keep current): "
            ).strip().lower()

            if new_status:
                if new_status in ["paid", "unpaid", "overdue"]:
                    invoice['status'] = new_status
                    print(f"Invoice {invoice['invoice_id']} status updated successfully.")
                else:
                    print("Invalid status. Please enter 'paid', 'unpaid', or 'overdue'.")
            print(f"Current Due Date: {invoice['due_date']}")
            new_due_date = input("Enter new due date (YYYY-MM-DD) (or press Enter to keep current): ").strip()
            if new_due_date:
                try:
                    datetime.strptime(new_due_date, "%Y-%m-%d")
                    invoice['due_date'] = new_due_date
                    print(f"Invoice {invoice['invoice_id']} updated successfully.")
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
            save_invoices(invoices)
            log_event(f"Invoice {invoice['invoice_id']} updated")
    if not found:
        print("Invoice not found.")
        return


def remove_invoice():
    invoices = load_invoices()
    if not invoices:
        print("No invoices found.")
        return

    search_id = input("Enter the invoice ID to remove: ").lower().strip()

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
            print("\n────────────────────────────────────────────────────────────────")
            confirm = input(f"Are you sure you want to remove invoice {invoice['invoice_id']}? (yes/no): ").strip().lower()
            if confirm == "yes":
                invoices.remove(invoice)
                save_invoices(invoices)
                log_event(f"Invoice {invoice['invoice_id']} deleted")
                print(f"Invoice {invoice['invoice_id']} removed successfully.")
                return
            elif confirm == "no":
                print("Operation cancelled.")
                return
            else:
                print("Invalid input. try again.")
    if not found:
        print("Invoice not found.")
        return


def record_payment():
    invoices = load_invoices()
    if not invoices:
        print("No invoices found.")
        return

    search_id = input("Enter the invoice ID to record payment for: ").lower().strip()
    found = False
    for invoice in invoices:
        if invoice['invoice_id'].lower() == search_id:
            found = True
            if invoice['status'] == 'paid':
                print(f"invoice amount is allready paid.")
                return
            print("\n────────────────────────────────────────────────────────────────")
            print(f"    Invoice ID: {invoice['invoice_id']}")
            print(f"    Job ID: {invoice['job_id']}")
            print(f"    Customer ID: {invoice['customer_id']}")
            print(f"    Amount: {invoice['amount']}")
            print(f"    Invoice Date: {invoice['invoice_date']}")
            print(f"    Due Date: {invoice['due_date']}")
            print(f"    Status: {invoice['status']}")
            print("\n────────────────────────────────────────────────────────────────")

            try:
                ask_payment = float(input("Enter payment amount: "))
                if ask_payment <= 0:
                    print("Invalid amount.")
                    return
                if ask_payment != invoice['amount']:
                    print("Payment amount must exactly match the invoice amount.")
                    return
            except ValueError:
                print("Invalid payment amount. Please enter a number.")
                return

            payment_date = input("Enter the payment date (YYYY-MM-DD): ").strip()
            try:
                payment_date_obj = datetime.strptime(payment_date, "%Y-%m-%d")
                if payment_date_obj.date() > datetime.now().date():
                    print("Payment date cannot be in future.")
                    return
            except ValueError:
                print("Invalid date. Please use YYYY-MM-DD")
                return

            payments = load_payments()
            payment_number = len(payments) + 1
            payment_id = f"PAY{payment_number:03d}"

            payment_data = {
                "payment_id": payment_id,
                "invoice_id": invoice['invoice_id'],
                "customer_id": invoice['customer_id'],
                "amount": ask_payment,
                "payment_date": payment_date,
                "status": "completed"
            }
            payments.append(payment_data)
            save_payments(payments)
            invoice['status'] = "paid"
            save_invoices(invoices)

            log_event(f"Payment {payment_data['payment_id']} recorded for Invoice {payment_data['invoice_id']}")
            
            print(f"Payment {payment_id} recorded successfully.")
            print(f"Invoice {invoice['invoice_id']} marked as paid.")
    if not found:
        print("No invoice found.")
        return


def view_payments():
    payments = load_payments()
    if not payments:
        print("No payments found.")
        return

    for payment in payments:
        print("\n────────────────────────────────────────")
        print(f"Payment ID    : {payment['payment_id']}")
        print(f"Invoice ID    : {payment['invoice_id']}")
        print(f"Customer ID   : {payment['customer_id']}")
        print(f"Amount        : {payment['amount']}")
        print(f"Payment Date  : {payment['payment_date']}")
        print(f"Status        : {payment['status']}")
        print("────────────────────────────────────────")


def search_payment():
    payments = load_payments()

    if not payments:
        print("No payments found.")
        return

    search_id = input("Enter payment ID to search: ").strip().lower()

    for payment in payments:
        if payment["payment_id"].lower() == search_id:
            print("\n────────────────────────────────────────")
            print(f"Payment ID    : {payment['payment_id']}")
            print(f"Invoice ID    : {payment['invoice_id']}")
            print(f"Customer ID   : {payment['customer_id']}")
            print(f"Amount        : {payment['amount']}")
            print(f"Payment Date  : {payment['payment_date']}")
            print(f"Status        : {payment['status']}")
            print("────────────────────────────────────────")
            return

    print("Payment not found.")


def payment_status():
    invoices = load_invoices()

    if not invoices:
        print("No invoices found.")
        return

    search_id = input("Enter invoice ID to check payment status: ").strip().lower()

    for invoice in invoices:
        if invoice["invoice_id"].lower() == search_id:
            print("\n────────────────────────────────────────")
            print(f"Invoice ID    : {invoice['invoice_id']}")
            print(f"Customer ID   : {invoice['customer_id']}")
            print(f"Amount        : {invoice['amount']}")
            print(f"Due Date      : {invoice['due_date']}")
            print(f"Status        : {invoice['status']}")
            print("────────────────────────────────────────")
            return

    print("Invoice not found.")