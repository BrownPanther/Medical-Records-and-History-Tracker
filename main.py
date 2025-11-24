# main.py
from excel_storage import (loadRecords, saveRecords)
from menu import (mainMenu,recordMenu,viewsortMenu,analyticsMenu)
from records_operation import (create_record, edit_record, delete_record, list_records)
from sort_filter import (sort_by_patient_name,sort_by_hospital_name,sort_by_visit_month,sort_by_visit_year,sort_by_issue,search_by_patient_name,search_by_hospital_name,search_by_issue_keyword)
from analytics import (hospVisits, visPerYear, mostCommonComplaint, multiVisits)
from utilities import (int_input,pause)


def record_management_loop():
    while True:
        recordMenu()
        rmchoice=int_input("Enter your choice: ")
        if rmchoice==1:
            create_record()
            pause()
        elif rmchoice== 2:
            edit_record()
            pause()
        elif rmchoice==3:
            delete_record()
            pause()
        elif rmchoice==4:
            list_records()
            pause()
        elif rmchoice==5:
            break
        else:
            print("Invalid choice.")
            pause()


def view_sort_loop():
    while True:
        viewsortMenu()
        vschoice =int_input("Enter your choice: ")
        if vschoice== 1:
            list_records()
            pause()
        elif vschoice== 2:
            sort_by_patient_name()
            pause()
        elif vschoice ==3:
            sort_by_hospital_name()
            pause()
        elif vschoice== 4:
            sort_by_visit_month()
            pause()
        elif vschoice ==5:
            sort_by_visit_year()
            pause()
        elif vschoice== 6:
            sort_by_issue()
            pause()
        elif vschoice ==7:
            search_by_patient_name()
            pause()
        elif vschoice ==8:
            search_by_hospital_name()
            pause()
        elif vschoice==9:
            search_by_issue_keyword()
            pause()
        elif vschoice==10:
            break
        else:
            print("Invalid choice.")
            pause()


def analytics_loop():
    while True:
        analyticsMenu()
        achoice = int_input("Enter your choice: ")
        if achoice == 1:
            hospVisits()
            pause()
        elif achoice==2:
            visPerYear()
            pause()
        elif achoice==3:
            mostCommonComplaint()
            pause()
        elif achoice ==4:
            multiVisits()
            pause()
        elif achoice== 5:
            break
        else:
            print("Invalid choice")
            pause()

def main():
    loadRecords()
    while True:
        mainMenu()
        mchoice=int_input("Enter your choice: ")
        if mchoice==1:
            record_management_loop()
        elif mchoice==2:
            view_sort_loop()
        elif mchoice==3:
            analytics_loop()
        elif mchoice==4:
            saveRecords()
            print("Exiting Medical Records & History Tracker.")
            break
        else:
            print("Invalid choice.")
            pause()


if __name__ == "__main__":
    main()
