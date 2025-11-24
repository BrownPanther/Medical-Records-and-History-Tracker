# utilities.py
# reusable functions

def int_input(prompt):
    while True:
        value=input(prompt)
        if value.strip()=="":
            print("Input cannot be empty")
            continue
        try:
            return int(value)
        except ValueError:
            print("Please enter integer value.")


def non_empty_str(prompt):
    while True:
        value =input(prompt)
        if value.strip()== "":
            print("Input cannot be empty.")
        else:
            return value.strip()


def choice_input(prompt, valid_choices):
    v_lower = [v.lower() for v in valid_choices]
    while True:
        value = input(prompt).strip()
        if value == "":
            print("Input cannot be empty.")
            continue
        if value.lower() in v_lower:
            for v in valid_choices:
                if v.lower() == value.lower():
                    return v
        print("Invalid choice. Valid options are:", ", ".join(valid_choices))


def yes_no(prompt):
    while True:
        value = input(prompt + " (y/n): ").strip().lower()
        if value in ("y", "yes"):
            return True
        elif value in ("n", "no"):
            return False
        print("Please enter only y or n.")


def date_string(prompt):
    #format- YYYY-MM-DD
    while True:
        date = input(prompt).strip()
        if date == "":
            print("Input can't be empty.")
            continue
        parts = date.split("-")
        if len(parts) != 3:
            print("Invalid format, please use YYYY-MM-DD.")
            continue
        yr,month,day = parts
        if not (yr.isdigit() and month.isdigit() and day.isdigit()):
            print("Year, month, and day must be numbers")
            continue
        return date


def pause():
    input("\nPress Enter to continue...")
