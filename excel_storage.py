# excel_storage.py
# Save and load medical records to/from a CSV file

import csv
import os
from data import Records

fname="medical_records.csv"

def loadRecords(filename=fname):
    Records.clear()
    try:
        with open(filename, "r",encoding="utf-8") as f:
            data = csv.DictReader(f)
            for row in data:
                try:
                    row["id"]=int(row["id"])
                    row["age"]=int(row["age"])
                    checkbool =row["follow_up"].lower().strip()
                    if checkbool in ("yes", "true", "1"):
                        row["follow_up"]=True
                    else:
                        row["follow_up"]=False
                    Records.append(row)  
                except ValueError:
                    continue    
    except FileNotFoundError:
        return

def saveRecords(filename=fname):
    with open(filename, mode="w", encoding="utf-8", newline="") as f:
        fieldnames=["id","patient_name","age","gender","hospital_name","visit_date","complaint","diagnosis","doctor_name","follow_up",]
        writer=csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        for Rec in Records:
            writer.writerow({"id":Rec["id"],"patient_name":Rec["patient_name"],"age":Rec["age"],"gender":Rec["gender"],"hospital_name": Rec["hospital_name"],
                "visit_date": Rec["visit_date"],"complaint":Rec["complaint"],"diagnosis": Rec["diagnosis"],"doctor_name":Rec["doctor_name"],
                "follow_up": "Yes" if Rec["follow_up"] else "No",})
    print("\nRecords saved to ",filename)
