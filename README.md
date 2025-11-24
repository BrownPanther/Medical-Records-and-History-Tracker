#  Medical Records & History Tracker (Python Console App)

This project is a console based Medical Records & History Tracker that I made using core Python only (no fancy GUI).
Basically, it lets you store outpatient visit details – like patient info, hospital name, date, issue, diagnosis etc – and then you can view / sort / search / do analytics on it.

It also saves the records into an Excel-compatible CSV file so the data stays even after closing the program.


## Features

Some things the project can do:

• add a medical record
• edit a record
• delete a record
• view all the records in a table
• sort records by:
    patient name
    hospital name
    month / year
    complaint / issue

• search by patient / hospital / issue keyword
• analytics:
    visits per hospital
    visits per year
    most common issue
    patients with multiple visits
    auto save + load using csv (openable in Excel)


It’s basically like a mini medical history managing system.

## Technologies and tools used

Programming language - Python
Data handling = Lists, dicts, sorting, searching, loops, conditions etc
Storage - CSV file (works in Excel)
Libraries used - None (only Python defaults- csv)
Runtime - Python3


## Steps to install & run

• Download/clone this project folder
• Make sure that all ".py" files stay in the same folder
• Open a terminal or command prompt window in the same folder
• Run the project using:

```bash
python main.py
```



When you exit the program using the menu, the CSV file will be updated automatically.
To see records in Excel, just open the "medical_records.csv" file.

## How to test the project?

Use the features in this order:


Step 1:	Add 3–5 new medical records
Step 2:	Edit any one of them
Step 3:	Delete any one of them
Step 4:	View all the records
Step 5:	Sort by patient name/ hospital/ year/ complaint
Step 6:	Search using keywords
Step 7:	Open Analytics and compare the outputs
Step 8:	Exit using the main menu, then re-run the program to confirm that CSV loading works.

Optional step: open "medical_records.csv" in Excel and check the rows manually.