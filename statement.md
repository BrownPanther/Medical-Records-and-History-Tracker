# Statement of the Project

## Problem Statement
Managing medical records manually often leads to missing information or data, difficulty in finding past visit history, and lack of centralized tracking for patient details, diagnosis, hospital consultation and follow-up requirements. There is a need for an easy and efficient system that gives users the ability to store, update, search and review medical visit information without the complexity or frustration of a full hospital management system.

## Scope of the Project
This project focuses on developing a console-based **Medical Records & History Tracker** using core Python.  
The scope includes operations like adding, editing, deleting, and loading medical records, along with search, sort and simple analytics. The project ensures data preservation by using CSV storage, so the records are available after the program is closed and opened again.  
The project does not include high level features such as authentication, networking, or integration with genuine medical databases, however these can be added later as enhancement features.

## Target Users
The system is designed for:
1. People who want to maintain their personal medical visit history
2. Students/beginners learning CRUD development in Python
3. Small clinics/hospitals or households that would need simple digital storage instead of physical paper based records
4. People who want to easily track hospital visits and follow-up    requirements

## High Level Features
- Add new medical record with data like the patient name, age, hospital, doctor, diagnosis and follow-up.
- Edit or update existing records using record ID.
- Delete wasteful or outdated records.
- Show all saved records in a readable tabular format.
- Sort records by patient name, hospital, visit month, visit year or complaint.
- Search records by patient name, hospital name or complaint keyword.
- Show analytics such as visits per hospital, visits per year, most common complaints and patients with multiple visits.
- Automatically save and load medical records using a CSV file.

