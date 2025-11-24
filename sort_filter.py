# sorting_filtering.py
from data import Records
from records_operation import list_records
from utilities import non_empty_str

def sort_by_patient_name():
    sortedRecs=sorted(Records,key=lambda r:r["patient_name"].lower()) #used lambda function to improve readability
    list_records(sortedRecs)

def sort_by_hospital_name():
    sortedRecs=sorted(Records, key=lambda r: r["hospital_name"].lower())
    list_records(sortedRecs)


def get_yr_month(date):
    # date is  "YYYY-MM-DD"
    parts = date.split("-")
    if len(parts)!=3:
        return ("0000", "00")
    return (parts[0], parts[1])


def sort_by_visit_month():
    sortedRecs=sorted(
        Records,
        key=lambda r: (get_yr_month(r["visit_date"])[1], get_yr_month(r["visit_date"])[0]))
    list_records(sortedRecs)


def sort_by_visit_year():
    sortedRecs=sorted(Records,key=lambda r: get_yr_month(r["visit_date"])[0])
    list_records(sortedRecs)


def sort_by_issue():
    sortedRecs=sorted(Records, key=lambda r: r["complaint"].lower())
    list_records(sortedRecs)


def search_by_patient_name():
    patName=non_empty_str("Enter patient name (in full or in parts): ").lower()
    searchRes=[]
    for rec in Records:
        if patName in rec["patient_name"].lower():
            searchRes.append(rec)
    print("\n=== Search Results (Patient Name) ===")
    list_records(searchRes)


def search_by_hospital_name():
    hosp=non_empty_str("Enter hospital patName (full or part): ").lower()
    searchRes=[]
    for rec in Records:
        if hosp in rec["hospital_name"].lower():
            searchRes.append(rec)
    print("\n=== Search Results (Hospital Name) ===")
    list_records(searchRes)


def search_by_issue_keyword():
    keywrd=non_empty_str("Enter complaint keyword: ").lower()
    searchRes=[]
    for rec in Records:
        if keywrd in rec["complaint"].lower():
            searchRes.append(rec)
    print("\n=== Search Results (Issue Keyword) ===")
    list_records(searchRes)
