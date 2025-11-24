# analytics.py
# Simple analytics on the in-memory medical records.

from data import Records

def hospVisits():  #tracks hospital counts in records
    print("\n------ Visits per Hospital ------")
    if not Records:
        print("No records.")
        return
    HVcount={} 
    for rec in Records:
        hosp=rec["hospital_name"]
        if hosp not in HVcount:
            HVcount[hosp]=0
        HVcount[hosp]=HVcount[hosp]+1

    for hosp, count in HVcount.items():
        print(hosp, "had", count, "visits")


def visPerYear():  #tracks total visits per year
    print("\n------ Visits per Year ------")
    if not Records:
        print("No records.")
        return
    VPYcount={}
    for rec in Records:
        tempdate=rec["visit_date"]
        if "-" in tempdate:
            yr=tempdate.split("-")[0]
        else:
            yr="Unknown"
        if yr not in VPYcount:
            VPYcount[yr]=0
        VPYcount[yr]=VPYcount[yr] + 1
    for yr, count in VPYcount.items():
        print(yr, "had", count, "visits")


def mostCommonComplaint(): #tracks most common complaint
    print("\n------ Most Common Complaint ------")
    if not Records:
        print("No records.")
        return
    complaintCount={}
    for rec in Records:
        complaint=rec["complaint"]
        if complaint not in complaintCount:
            complaintCount[complaint]=0
        complaintCount[complaint]=complaintCount[complaint] + 1

    #find max manually
    maxComplaint=None
    maxCount=0
    for complaint,count in complaintCount.items():
        if count>maxCount:
            maxCount=count
            maxComplaint=complaint
    if maxComplaint is None:
        print("No complaints found")
    else:
        print(f"Most common complaint: '{maxComplaint}' ({maxCount} time(s))")


def multiVisits():   #tracks patients with multiple visits
    print("\n------ Patients with Multiple Visits ------")
    if not Records:
        print("No records.")
        return
    visitCount={}
    for rec in Records:
        name=rec["patient_name"]
        if name not in visitCount:
            visitCount[name]=0
        visitCount[name]=visitCount[name]+ 1
    found=False
    for name,count in visitCount.items():
        if count>1:
            print(name, "visited", count, "times")
            found=True
    if not found:
        print("No patient has more than one visit in the data.")
