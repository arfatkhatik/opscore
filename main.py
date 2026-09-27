
from services.employee_service import employee_menu
from services.customer_service import  customer_menu
def splash_screen():
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                       O P S C O R E                          ║
║                                                              ║
║            Operations & Workforce Intelligence               ║
║                         Platform                             ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   SYSTEM STATUS                                              ║
║                                                              ║
║   ● Core Engine ................. READY                      ║
║   ● Data Storage ................ READY                      ║
║   ● Configuration ............... LOADED                     ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║              Enterprise Operations System                    ║
║                                                              ║
║                    Version 1.0.0                             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝""")
    input("               PRESS ENTER TO GO AHEAD")
if __name__ == "__main__":
    splash_screen()
def menu():
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                       O P S C O R E                          ║
║                                                              ║
║            Operations & Workforce Intelligence               ║
║                         Platform                             ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   MAIN OPERATIONS                                            ║
║                                                              ║
║      [1]   Employee Management                               ║
║      [2]   Customer Management                               ║
║      [3]   Job Management                                    ║
║      [4]   Assignment & Scheduling                           ║
║                                                              ║
║   FINANCE & INSIGHTS                                         ║
║                                                              ║
║      [5]   Invoices & Payments                               ║
║      [6]   Reports & Analytics                               ║
║                                                              ║
║   SYSTEM                                                     ║
║                                                              ║
║      [7]   System Management                                 ║
║      [8]   Backup & Storage                                  ║
║                                                              ║
║      [0]   Exit OPSCORE                                      ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   System Status: ● ONLINE                   Version 1.0.0    ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝ """)
    user_input = input("             ENTER YOUR CHOICE: ")
    return user_input
    

def main():
    splash_screen()

    while True:
        choice = menu()
        if choice == "1":
            employee_menu()
        elif choice == "2":
            customer_menu()
        
        elif choice == "0":
            print("Exiting OPSCORE...")
            break
        else:
            print("That option is not available yet.")
            input("Press ENTER to continue...")


if __name__ == "__main__":
    main()

