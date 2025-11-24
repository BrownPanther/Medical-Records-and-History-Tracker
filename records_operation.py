# records_operation.py
# adding, editing, deleting, listing medical records.

from data import Records, Gender
from utilities import (
    int_input,
    non_empty_str,
    choice_input,
    date_string,
    yes_no,
)

def next_record_id():
    if not Records:
        return 1
    maxID =Records[0]["id"]
    for rec in Records:
        if rec["id"]>maxID:
            maxID=rec["id"]
    return (maxID+1)


def create_record():
    print("\n------ Add New Medical Record ------")
    patient_name = non_empty_str("Patient name: ")
    age=int_input("Age: ")
    gender=choice_input("Gender (Male/Female/Other): ",Gender)
    hospital_name=non_empty_str("Hospital name: ")
    visit_date=date_string("Visit date (YYYY-MM-DD): ")
    complaint=non_empty_str("Complaint: ")
    diagnosis=non_empty_str("Diagnosis/Treatment summary: ")
    doctor_name = non_empty_str("Doctor's name: ")
    follow_up = yes_no("Is follow-up required")

    recordID = next_record_id()
    record = {"id":recordID,"patient_name":patient_name,"age":age,"gender":gender,"hospital_name":hospital_name,"visit_date":visit_date,
        "complaint":complaint,"diagnosis":diagnosis,"doctor_name":doctor_name,"follow_up":follow_up,}
    Records.append(record)
    print("Record added with ID: ",recordID)


def list_records(records=None):
    print("\n------ Medical Records ------")
    if records is None:
        records=Records
    if not records:
        print("No records found.")
        return
    print("{:<4} {:<15} {:<3} {:<6} {:<15} {:<12} {:<15} {:<15} {:<8}".format("ID", "Patient", "Age", "Gender", "Hospital", "Visit Date","Complaint", "Doctor", "FollowUp"))
    print("-" * 110)
    for rec in records:
        print("{:<4} {:<15} {:<3} {:<6} {:<15} {:<12} {:<15} {:<15} {:<8}".format(rec["id"],rec["patient_name"][:15],rec["age"],rec["gender"],rec["hospital_name"][:15],rec["visit_date"],rec["complaint"][:15],rec["doctor_name"][:15],"Yes" if rec["follow_up"] else "No"))

def recor_by_id(recordID):
    for rec in Records:
        if rec["id"]==recordID:
            return rec
    return None


def edit_record():
    print("\n------ Edit Record ------")
    if not Records:
        print("No records to edit.")
        return
    list_records()
    recordID = int_input("Enter record ID to edit: ")
    rec = recor_by_id(recordID)
    if rec is None:
        print("Record not found.")
        return
    print("Leave input empty to keep current value.")
    newname=input(f"Patient name [{rec['patient_name']}]: ").strip()
    if newname!="":
        rec["patient_name"]=newname

    newage=input(f"Age [{rec['age']}]: ").strip()
    if newage!="":
        if newage.isdigit():
            rec["age"]=int(newage)
        else:
            print("Invalid age, keeping old value.")

    newgender=input(f"Gender [{rec['gender']}]: ").strip()
    if newgender!="":
        if newgender.capitalize() in Gender:
            rec["gender"]=newgender.capitalize()
        else:
            print("Invalid gender, keeping old value.")

    newhosp=input(f"Hospital [{rec['hospital_name']}]: ").strip()
    if newhosp!="":
        rec["hospital_name"]=newhosp

    newdate = input(f"Visit date [{rec['visit_date']}]: ").strip()
    if newdate != "":
        parts = newdate.split("-")
        if len(parts) == 3 and all(p.isdigit() for p in parts):
            rec["visit_date"] = newdate
        else:
            print("Invalid date format, keeping old value.")

    newcomplaint = input(f"Complaint [{rec['complaint']}]: ").strip()
    if newcomplaint != "":
        rec["complaint"] = newcomplaint

    newdiag = input(f"Diagnosis [{rec['diagnosis']}]: ").strip()
    if newdiag != "":
        rec["diagnosis"] = newdiag

    newdoc = input(f"Doctor [{rec['doctor_name']}]: ").strip()
    if newdoc != "":
        rec["doctor_name"] = newdoc

    newfollow = input(f"Follow-up required (y/n) [{ 'y' if rec['follow_up'] else 'n' }]: ").strip().lower()
    if newfollow in ("y", "yes"):
        rec["follow_up"] = True
    elif newfollow in ("n", "no"):
        rec["follow_up"] = False
    print("Record updated.")


def delete_record():
    print("\n------ Delete Record ------")
    if not Records:
        print("No records to delete.")
        return

    list_records()
    recordID = int_input("Enter record ID to delete: ")
    indexDel = -1
    for i, rec in enumerate(Records):
        if rec["id"] == recordID:
            indexDel = i
            break

    if indexDel == -1:
        print("Record not found.")
    else:
        deleted=Records.pop(indexDel)
        print(f"Deleted record ID {deleted['id']} for patient {deleted['patient_name']}.")
