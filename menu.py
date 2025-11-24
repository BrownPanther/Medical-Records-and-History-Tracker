# menu.py
# prints the menu

def mainMenu():
    print("\n====== Medical Records & History Tracker ======")
    print("1. Manage the Records")
    print("2. View / Sort / Search Records")
    print("3. Analytics and Summary")
    print("4. Exit")

def recordMenu():
    print("\n--- Record Management ---")
    print("1. Add a Record")
    print("2. Edit a Record")
    print("3. Delete a Record")
    print("4. View All the Records")
    print("5. Back to the Main Menu")

def viewsortMenu():
    print("\n--- View / Sort / Search ---")
    print("1. View All Records (Unsorted)")
    print("2. Sort by Patient Name")
    print("3. Sort by Hospital Name")
    print("4. Sort by Visit Month")
    print("5. Sort by Visit Year")
    print("6. Sort by Complaint")
    print("7. Search by Patient Name")
    print("8. Search by Hospital Name")
    print("9. Search by Complaint Keyword")
    print("10. Back to the Main Menu")

def analyticsMenu():
    print("\n--- Analytics & Summary ---")
    print("1. Visits per Hospital")
    print("2. Visits per Year")
    print("3. Most Common Complaints")
    print("4. Patients with Multiple Visits")
    print("5. Back to the Main Menu")
