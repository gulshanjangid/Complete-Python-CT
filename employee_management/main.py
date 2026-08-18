from models.employee import Employee
from services.employee_manager import EmployeeManager

from utils.helpers import (
    get_integer,
    get_float,
    get_non_empty_string,
    get_email,
    get_skills,
    pause
)


# =========================================================
# CREATE MANAGER
# =========================================================

manager = EmployeeManager()


# =========================================================
# MENU
# =========================================================

def show_menu() -> None:

    print("\n")
    print("=" * 50)
    print("       EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Sort Employees")
    print("7. Employee Statistics")
    print("8. View Departments")
    print("9. View Skills")
    print("10. Exit")

    print("=" * 50)


# =========================================================
# ADD EMPLOYEE
# =========================================================

def add_employee() -> None:

    print("\n===== ADD EMPLOYEE =====")

    employee_id = get_integer(
        "Enter Employee ID: ",
        minimum=1
    )

    if manager.get_employee(employee_id) is not None:

        print("Employee ID already exists.")

        return

    name = get_non_empty_string(
        "Enter Name: "
    )

    age = get_integer(
        "Enter Age: ",
        minimum=18,
        maximum=100
    )

    email = get_email(
        "Enter Email: "
    )

    department = get_non_empty_string(
        "Enter Department: "
    )

    salary = get_float(
        "Enter Salary: ",
        minimum=0
    )

    skills = get_skills(
        "Enter Skills (comma separated): "
    )

    employee = Employee(
        employee_id=employee_id,
        name=name,
        age=age,
        email=email,
        department=department,
        salary=salary,
        skills=skills
    )

    if manager.add_employee(employee):

        print("\nEmployee added successfully!")

    else:

        print("\nUnable to add employee.")


# =========================================================
# VIEW EMPLOYEES
# =========================================================

def view_employees() -> None:

    print("\n===== ALL EMPLOYEES =====")

    employees = manager.get_all_employees()

    if not employees:

        print("No employees found.")

        return

    for employee in employees:

        print("-" * 80)

        print(employee)

    print("-" * 80)


# =========================================================
# SEARCH EMPLOYEE
# =========================================================

def search_employee() -> None:

    print("\n===== SEARCH EMPLOYEE =====")

    print("1. Search by ID")
    print("2. Search by Name")
    print("3. Search by Department")

    choice = input(
        "Enter choice: "
    ).strip()

    if choice == "1":

        employee_id = get_integer(
            "Enter Employee ID: "
        )

        employee = manager.get_employee(
            employee_id
        )

        if employee:

            print("\nEmployee Found:")
            print(employee)

        else:

            print("Employee not found.")

    elif choice == "2":

        name = get_non_empty_string(
            "Enter Name: "
        )

        employees = manager.search_by_name(name)

        display_search_results(employees)

    elif choice == "3":

        department = get_non_empty_string(
            "Enter Department: "
        )

        employees = manager.search_by_department(
            department
        )

        display_search_results(employees)

    else:

        print("Invalid choice.")


def display_search_results(
    employees: list[Employee]
) -> None:

    if not employees:

        print("No employees found.")

        return

    print(f"\nFound {len(employees)} employee(s):")

    for employee in employees:

        print("-" * 80)
        print(employee)


# =========================================================
# UPDATE EMPLOYEE
# =========================================================

def update_employee() -> None:

    print("\n===== UPDATE EMPLOYEE =====")

    employee_id = get_integer(
        "Enter Employee ID: "
    )

    employee = manager.get_employee(
        employee_id
    )

    if employee is None:

        print("Employee not found.")

        return

    print("\nCurrent information:")
    print(employee)

    print("\nEnter new information:")

    name = get_non_empty_string(
        "Enter Name: "
    )

    age = get_integer(
        "Enter Age: ",
        minimum=18,
        maximum=100
    )

    email = get_email(
        "Enter Email: "
    )

    department = get_non_empty_string(
        "Enter Department: "
    )

    salary = get_float(
        "Enter Salary: ",
        minimum=0
    )

    skills = get_skills(
        "Enter Skills (comma separated): "
    )

    success = manager.update_employee(
        employee_id=employee_id,
        name=name,
        age=age,
        email=email,
        department=department,
        salary=salary,
        skills=skills
    )

    if success:

        print("\nEmployee updated successfully!")

    else:

        print("\nUnable to update employee.")


# =========================================================
# DELETE EMPLOYEE
# =========================================================

def delete_employee() -> None:

    print("\n===== DELETE EMPLOYEE =====")

    employee_id = get_integer(
        "Enter Employee ID: "
    )

    employee = manager.get_employee(
        employee_id
    )

    if employee is None:

        print("Employee not found.")

        return

    print("\nEmployee:")
    print(employee)

    confirmation = input(
        "\nAre you sure you want to delete? (y/n): "
    ).lower()

    if confirmation == "y":

        if manager.delete_employee(employee_id):

            print("Employee deleted successfully!")

        else:

            print("Unable to delete employee.")

    else:

        print("Delete cancelled.")


# =========================================================
# SORT EMPLOYEES
# =========================================================

def sort_employees() -> None:

    print("\n===== SORT EMPLOYEES =====")

    print("1. Sort by Name")
    print("2. Sort by Salary - Low to High")
    print("3. Sort by Salary - High to Low")

    choice = input(
        "Enter choice: "
    ).strip()

    if choice == "1":

        employees = manager.sort_by_name()

    elif choice == "2":

        employees = manager.sort_by_salary(
            reverse=False
        )

    elif choice == "3":

        employees = manager.sort_by_salary(
            reverse=True
        )

    else:

        print("Invalid choice.")

        return

    for employee in employees:

        print("-" * 80)
        print(employee)


# =========================================================
# STATISTICS
# =========================================================

def show_statistics() -> None:

    print("\n===== EMPLOYEE STATISTICS =====")

    total = manager.total_employees()

    print(f"Total Employees: {total}")

    if total == 0:

        print("No employee data available.")

        return

    average = manager.average_salary()

    print(f"Average Salary: ₹{average:.2f}")

    highest = manager.highest_salary()

    if highest:

        print(
            f"Highest Salary: "
            f"{highest.name} - ₹{highest.salary:.2f}"
        )

    lowest = manager.lowest_salary()

    if lowest:

        print(
            f"Lowest Salary: "
            f"{lowest.name} - ₹{lowest.salary:.2f}"
        )


# =========================================================
# DEPARTMENTS
# =========================================================

def show_departments() -> None:

    print("\n===== DEPARTMENTS =====")

    departments = manager.get_departments()

    if not departments:

        print("No departments found.")

        return

    for department in sorted(departments):

        print(f"- {department}")


# =========================================================
# SKILLS
# =========================================================

def show_skills() -> None:

    print("\n===== ALL SKILLS =====")

    skills = manager.get_all_skills()

    if not skills:

        print("No skills found.")

        return

    for skill in sorted(skills):

        print(f"- {skill}")


# =========================================================
# MAIN PROGRAM
# =========================================================

def main() -> None:

    while True:

        show_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            add_employee()

        elif choice == "2":

            view_employees()

        elif choice == "3":

            search_employee()

        elif choice == "4":

            update_employee()

        elif choice == "5":

            delete_employee()

        elif choice == "6":

            sort_employees()

        elif choice == "7":

            show_statistics()

        elif choice == "8":

            show_departments()

        elif choice == "9":

            show_skills()

        elif choice == "10":

            print("\nThank you for using Employee Management System!")

            break

        else:

            print("\nInvalid choice. Please try again.")

        pause()


# =========================================================
# PROGRAM START
# =========================================================

if __name__ == "__main__":
    main()