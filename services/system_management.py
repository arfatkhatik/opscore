import os
import shutil
from datetime import datetime
from utils.file_manager import (load_employees, load_assignments,load_customers,load_invoices,load_jobs,load_payments)
import json

def system_management_menu():
    while True:
        print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                    SYSTEM MANAGEMENT                         ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   [1] View System Information                                ║
║   [2] Manage Directories                                     ║
║   [3] View Logs                                              ║
║   [4] System Configuration                                   ║
║   [5] Create Backup                                          ║
║   [6] Restore Backup                                         ║
║                                                              ║
║   [0] Back to Main Menu                                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")
        choice = input("Enter your choice: ")
        if choice == "1":
            system_information()
        elif choice == "2":
            directory_management()

        elif choice == "3":
            view_logs()

        elif choice == "4":
            system_configuration()

        elif choice == "5":
            create_backup()

        elif choice == "6":
            restore_backup()

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")


def system_information():
    employees = load_employees()
    customers = load_customers()
    jobs = load_jobs()
    assignments = load_assignments()
    invoices = load_invoices()
    payments = load_payments()
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                   SYSTEM INFORMATION                         ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
""")
    print("    System name       : OPSCORE")
    if os.path.exists("data"):
        print("  \n    Data Directory    : Available")
    else:
        print("    Data Directory    : Missing")

    if os.path.exists("logs"):
        print("    Logs Directory    : Available")
    else:
        print("    Logs Directory    : Missing")

    if os.path.exists("backups"):
        print("    Backup Directory  : Available")
    else:
        print("    Backup Directory  : Missing")

    print(f"\n    EMPLOYEES         : {len(employees)} ")
    print(f"    CUSTOMERS         : {len(customers)}")
    print(f"    JOBS              : {len(jobs)}")
    print(f"    ASSIGNMENTS       : {len(assignments)}")
    print(f"    INVOICES          : {len(invoices)}")
    print(f"    PAYMENTS          : {len(payments)}")

    print("""
╚══════════════════════════════════════════════════════════════╝
""")

    input("Press Enter to return to System Management...")


def directory_management():
    while True:
        print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║                    MANAGE DIRECTORIES                        ║
    ║                                                              ║
    ╠══════════════════════════════════════════════════════════════╣
    ║                                                              ║
    ║   [1] View Directory Contents                                ║
    ║   [2] Check Directory Status                                 ║
    ║   [3] Create Directory                                       ║
    ║   [4] Remove Directory                                       ║
    ║                                                              ║
    ║   [0] Back to System Management                              ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
        choice = input("Enter your choice: ")
        if choice == "1":
            view_directory()
        elif choice == "2":
            view_status()
        elif choice == "3":
            create_directory()
        elif choice == "4":
            remove_directory()
        elif choice == "0":
             break
        
        else:
            print("Invalid choice. Please try again.")

def view_directory():
    while True:    
        print("""
    Select Directory

    [1] data
    [2] logs
    [3] backups
    [0] Back

    """)
        choice = input("Enter your choice: ")
        if choice == "1":
            files = os.listdir("data")
            for file in files:
                print(file)
        elif choice == "2":
            files = os.listdir("logs")
            for file in files:
                print(file)
        elif choice == "3":
            files = os.listdir("backups")
            for file in files:
                print(file)
        elif choice == "0":
            break
        else:
            print("Invalid option. please try again")

def view_status():
    while True:
        print("""
Select Directory

    [1] data
    [2] logs
    [3] backups
    [0] Back

""")

        choice = input("Enter your choice: ")

        if choice == "1":
            directory = "data"

        elif choice == "2":
            directory = "logs"

        elif choice == "3":
            directory = "backups"

        elif choice == "0":
            break

        else:
            print("Invalid option. Please try again.")
            continue

        print("\nDIRECTORY STATUS:")
        print(f"\nDirectory name: {directory}")

        if os.path.exists(directory):
            print("Exists        : Yes")

            if os.path.isdir(directory):
                print("Type          : Directory")
                print(f"Items         : {len(os.listdir(directory))}")
            else:
                print("Type          : Not a Directory")
                print("Items         : 0")

        else:
            print("Exists        : No")
            print("Type          : Not Found")
            print("Items         : 0")

        input("\nPress Enter to continue...")


def create_directory():
    ask_name = input("Enter name to create directory: ")

    exists = os.path.exists(ask_name)

    if exists:
        print("directoty already exist.")
        input("\nPress Enter to continue...")

    elif not exists:
        os.makedirs(ask_name)
        log_event(f"Directory {ask_name} created")
        print(f"directory {ask_name} created successfully.")
        input("\nPress Enter to continue...")


def remove_directory():
    ask_name = input("Enter directory name to remove: ")

    protected_directories = ["data", "logs", "backup"]
    if ask_name.lower() in protected_directories:
        print("This is a protected OPSCORE directory and cannot be removed.")
        input("\nPress Enter to continue...")
        return
    exists = os.path.exists(ask_name)

    if exists:
        confirmation = input("do you really want to remove directory? (yes/no): ")
        if confirmation == "yes":
            os.rmdir(ask_name)
            log_event(f"Directory {ask_name} removed")
            print(f"Directory {ask_name} deleted succesfully.")
            input("\nPress Enter to continue...")
        elif confirmation == "no":
            print("removal canceled.")
            input("\nPress Enter to continue...")
        else:
            print("Invalid option selected. please try again.")

    else:
        print("Directory does not exists.")
        input("\nPress Enter to continue...")


def view_logs():
    while True:
        print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║                         VIEW LOGS                            ║
    ║                                                              ║
    ╠══════════════════════════════════════════════════════════════╣
    ║                                                              ║
    ║   [1] View All Logs                                          ║
    ║   [2] View Latest Log Entries                                ║
    ║   [0] Back to System Management                              ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
        choice = input("Enter your choice: ")
        if choice == "1":
            view_all_logs()
        elif choice == "2":
            latest_log()
        elif choice == "0":
            break
        else:
            print("Invalid option selected. please try again.")


def view_all_logs():
    exists = os.path.exists("logs/opscore.log")

    if exists:
        with open("logs/opscore.log", "r") as file:
            logs = file.read()
            print("\n========== OPSCORE LOGS ==========\n")
            print(logs)

        input("\nPress Enter to continue...")

    else:
        print("log file does not exists.")
        print("No logs available.")
        input("\nPress Enter to continue...")


def latest_log():
    exists = os.path.exists("logs/opscore.log")

    if exists:
        with open("logs/opscore.log", "r") as file:
            logs = file.readlines()
            logs = logs[-10:]
            print("========== LATEST LOG ENTRIES ==========")
            for log in logs:
                print(log, end="")
        input("\nPress Enter to continue...")

    else:
        print("log file does not exists.")
        print("No logs available.")
        input("\nPress Enter to continue...")


def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    os.makedirs("logs", exist_ok=True)
    with open("logs/opscore.log", "a") as file:
        file.write(f"{timestamp} - {message}\n")

def system_configuration():
    while True:
        print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                    SYSTEM CONFIGURATION                      ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   [1] View Current Configuration                             ║
║   [2] Update Configuration                                   ║
║                                                              ║
║   [0] Back to System Management                              ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")

        choice = input("Enter option number: ")

        if choice == "1":
            view_configuration()
        elif choice == "2":
            update_configuration()
        elif choice == "0":
            break
        else:
            print("Invalid option.")

def view_configuration():
    with open("data/system_config.json", "r") as file:
        config = json.load(file)

        for key, value in config.items():
            print(f"{key}: {value}")

def update_configuration():
    with open("data/system_config.json", "r") as file:
        config = json.load(file)

        print("\n========== UPDATE CONFIGURATION ==========\n")

        for key, value in config.items():
            print(f"{key}: {value}")

        setting = input("Enter the setting name to update: ")

        if setting not in config:
            print("Invalid setting Name.")
            input("Press Enter to continue...")
            return

        new_value = input("Enter new value: ").strip()

        if setting == "low_stock_threshold":
            try:
                new_value = int(new_value)
                if new_value < 0:
                    print("Threshold cannot be negative.")
                    input("\nPress Enter to continue...")
                    return
            except ValueError:
                print("Threshold must be a whole number.")
                input("\nPress Enter to continue...")
                return
        config[setting] = new_value

        with open("data/system_config.json", "w") as file:
            json.dump(config, file, indent=4)

        print("Configuration updated successfully.")
        log_event(f"Configuration setting '{setting}' updated")

        input("\nPress Enter to continue...")

def create_backup():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"backup_{timestamp}"
    backup_path = f"backups/{backup_name}"
    try:
        shutil.copytree("data", backup_path)
        print(f"backup created {backup_path}")
        log_event(f"backup created at {backup_path}")
    except OSError as e:
        print(f"Backup failed {e}")


def restore_backup():
    # 1. Check whether the backups directory exists.
    if not os.path.isdir("backups"):
        print("Backups directory doesn't exist.")
        input("\nPress Enter to continue...")
        return

    # 2. Find available backup directories.
    backups = sorted([
        name for name in os.listdir("backups")
        if name.startswith("backup_")
        and os.path.isdir(os.path.join("backups", name))
    ])

    if not backups:
        print("No backups available.")
        input("\nPress Enter to continue...")
        return

    # 3. Display available backups.
    print("\n========== AVAILABLE BACKUPS ==========\n")

    for index, backup in enumerate(backups, start=1):
        print(index, backup)

    # 4. Validate the user's selection.
    try:
        choice = int(input("Enter backup number to restore: "))

        if choice < 1 or choice > len(backups):
            print("Invalid backup number.")
            input("\nPress Enter to continue...")
            return

    except ValueError:
        print("Please enter a valid number.")
        input("\nPress Enter to continue...")
        return

    selected_backup = backups[choice - 1]
    print(f"Selected backup: {selected_backup}")

    # 5. Ask for confirmation.
    confirm = input("Are you sure you want to restore this backup? (yes/no): ").strip().lower()

    if confirm != "yes":
        print("Restore cancelled.")
        input("\nPress Enter to continue...")
        return

    backup_path = os.path.join("backups", selected_backup)
    data_path = "data"

    # 6. Check the selected backup and current data directories.
    if not os.path.isdir(backup_path):
        print("Selected backup is not a valid directory.")
        input("\nPress Enter to continue...")
        return

    if not os.path.isdir(data_path):
        print("Current data directory doesn't exist.")
        input("\nPress Enter to continue...")
        return

    # 7. Validate required files and JSON syntax.
    required_files = [
        "assignments.json",
        "customers.json",
        "employees.json",
        "invoices.json",
        "jobs.json",
        "payments.json",
        "system_config.json"
    ]

    for filename in required_files:
        file_path = os.path.join(backup_path, filename)

        if not os.path.isfile(file_path):
            print(f"Required backup file is missing: {filename}")
            input("\nPress Enter to continue...")
            return

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                json.load(file)

        except (OSError, json.JSONDecodeError, UnicodeError) as e:
            print(f"Invalid backup file '{filename}': {e}")
            input("\nPress Enter to continue...")
            return

    # 8. Generate unique names for restoration folders.
    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S_%f"
    )

    safety_backup_path = os.path.join(
        "backups", f"pre_restore_{timestamp}"
    )
    temp_data_path = f"data_restore_{timestamp}"
    old_data_path = f"data_before_restore_{timestamp}"

    # 9. Create a safety backup of the current data.
    try:
        shutil.copytree(data_path, safety_backup_path)
        print(f"Safety backup created at {safety_backup_path}")

    except OSError as e:
        print(f"Could not create safety backup: {e}")
        input("\nPress Enter to continue...")
        return

    # 10. Prepare the selected backup in a temporary folder.
    try:
        shutil.copytree(backup_path, temp_data_path)
        print("Backup copied to temporary folder.")

    except OSError as e:
        print(f"Could not prepare backup for restoration: {e}")

        if os.path.exists(temp_data_path):
            try:
                shutil.rmtree(temp_data_path)
            except OSError as cleanup_error:
                print(f"Temporary cleanup failed: {cleanup_error}")

        input("\nPress Enter to continue...")
        return

    # 11. Preserve the current data directory.
    try:
        os.rename(data_path, old_data_path)
        print("Current data folder preserved.")

    except OSError as e:
        print(f"Could not preserve current data: {e}")

        try:
            shutil.rmtree(temp_data_path)
        except OSError as cleanup_error:
            print(f"Temporary cleanup failed: {cleanup_error}")

        input("\nPress Enter to continue...")
        return

    # 12. Install the selected backup.
    try:
        os.rename(temp_data_path, data_path)

    except OSError as e:
        print(f"Restore failed: {e}")

        # Roll back to the previous data directory.
        try:
            os.rename(old_data_path, data_path)
            print("Previous data restored successfully.")

        except OSError as rollback_error:
            print(
                "CRITICAL: Could not restore previous data: "
                f"{rollback_error}"
            )
            print(f"Previous data may still be available at: {old_data_path}")

        # Clean up the temporary folder if it remains.
        if os.path.exists(temp_data_path):
            try:
                shutil.rmtree(temp_data_path)
            except OSError as cleanup_error:
                print(f"Temporary cleanup failed: {cleanup_error}")

        input("\nPress Enter to continue...")
        return

    # 13. Restoration succeeded.
    print("Backup restored successfully.")

    # 14. Log restoration separately so logging errors
    #     do not trigger a rollback of successfully restored data.
    try:
        log_event(
            f"Safety backup created at {safety_backup_path}"
        )
        log_event(f"Backup restored from {backup_path}")
        log_event(
            f"Previous data preserved at {old_data_path}"
        )

    except OSError as e:
        print(
            "Warning: Restore succeeded, but logging failed: "
            f"{e}"
        )

    input("\nPress Enter to continue...")
