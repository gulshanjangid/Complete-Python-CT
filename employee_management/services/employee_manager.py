import json
from pathlib import Path
from typing import Generator

from models.employee import Employee
from utils.decorators import log_action


class EmployeeManager:
    """
    Manages employees and handles file storage.
    """

    def __init__(self, file_path: str = "data/employees.json") -> None:

        self.file_path = Path(file_path)

        # List to store Employee objects
        self.employees: list[Employee] = []

        self.load_employees()

    # =========================================================
    # FILE HANDLING
    # =========================================================

    def load_employees(self) -> None:
        """
        Load employees from JSON file.
        """

        try:

            if not self.file_path.exists():
                self.file_path.parent.mkdir(
                    parents=True,
                    exist_ok=True
                )

                self.save_employees()
                return

            with self.file_path.open(
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

                self.employees = [
                    Employee.from_dict(employee)
                    for employee in data
                ]

        except json.JSONDecodeError:

            print("Error: employees.json contains invalid JSON.")

            self.employees = []

        except OSError as error:

            print(f"File error: {error}")

            self.employees = []

    def save_employees(self) -> None:
        """
        Save employees to JSON file.
        """

        try:

            self.file_path.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            with self.file_path.open(
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    [
                        employee.to_dict()
                        for employee in self.employees
                    ],
                    file,
                    indent=4,
                    ensure_ascii=False
                )

        except OSError as error:

            print(f"Unable to save employees: {error}")

    # =========================================================
    # ADD EMPLOYEE
    # =========================================================

    @log_action
    def add_employee(self, employee: Employee) -> bool:
        """
        Add a new employee.
        """

        # Check duplicate ID
        if self.get_employee(employee.employee_id) is not None:
            return False

        self.employees.append(employee)

        self.save_employees()

        return True

    # =========================================================
    # GET EMPLOYEE
    # =========================================================

    def get_employee(
        self,
        employee_id: int
    ) -> Employee | None:
        """
        Find employee by ID.
        """

        for employee in self.employees:

            if employee.employee_id == employee_id:
                return employee

        return None

    # =========================================================
    # VIEW EMPLOYEES
    # =========================================================

    def get_all_employees(self) -> list[Employee]:
        """
        Return all employees.
        """

        return self.employees

    # =========================================================
    # SEARCH
    # =========================================================

    def search_by_name(
        self,
        name: str
    ) -> list[Employee]:
        """
        Search employees by name.
        """

        return [
            employee
            for employee in self.employees
            if name.lower() in employee.name.lower()
        ]

    def search_by_department(
        self,
        department: str
    ) -> list[Employee]:
        """
        Search employees by department.
        """

        return [
            employee
            for employee in self.employees
            if employee.department.lower() == department.lower()
        ]

    # =========================================================
    # UPDATE
    # =========================================================

    @log_action
    def update_employee(
        self,
        employee_id: int,
        name: str,
        age: int,
        email: str,
        department: str,
        salary: float,
        skills: set[str]
    ) -> bool:
        """
        Update employee information.
        """

        employee = self.get_employee(employee_id)

        if employee is None:
            return False

        employee.name = name
        employee.age = age
        employee.email = email
        employee.department = department
        employee.salary = salary
        employee.skills = skills

        self.save_employees()

        return True

    # =========================================================
    # DELETE
    # =========================================================

    @log_action
    def delete_employee(
        self,
        employee_id: int
    ) -> bool:
        """
        Delete employee by ID.
        """

        employee = self.get_employee(employee_id)

        if employee is None:
            return False

        self.employees.remove(employee)

        self.save_employees()

        return True

    # =========================================================
    # SORT
    # =========================================================

    def sort_by_salary(
        self,
        reverse: bool = False
    ) -> list[Employee]:
        """
        Sort employees by salary.
        """

        return sorted(
            self.employees,
            key=lambda employee: employee.salary,
            reverse=reverse
        )

    def sort_by_name(self) -> list[Employee]:
        """
        Sort employees alphabetically by name.
        """

        return sorted(
            self.employees,
            key=lambda employee: employee.name.lower()
        )

    # =========================================================
    # GENERATOR
    # =========================================================

    def employee_generator(
        self
    ) -> Generator[Employee, None, None]:
        """
        Generate employees one by one.
        """

        for employee in self.employees:
            yield employee

    # =========================================================
    # STATISTICS
    # =========================================================

    def total_employees(self) -> int:
        """
        Return total number of employees.
        """

        return len(self.employees)

    def average_salary(self) -> float:
        """
        Calculate average salary.
        """

        if not self.employees:
            return 0.0

        total = sum(
            employee.salary
            for employee in self.employees
        )

        return total / len(self.employees)

    def highest_salary(self) -> Employee | None:
        """
        Return employee with highest salary.
        """

        if not self.employees:
            return None

        return max(
            self.employees,
            key=lambda employee: employee.salary
        )

    def lowest_salary(self) -> Employee | None:
        """
        Return employee with lowest salary.
        """

        if not self.employees:
            return None

        return min(
            self.employees,
            key=lambda employee: employee.salary
        )

    # =========================================================
    # DEPARTMENTS
    # =========================================================

    def get_departments(self) -> set[str]:
        """
        Return unique departments.

        Set is used because departments should be unique.
        """

        return {
            employee.department
            for employee in self.employees
        }

    # =========================================================
    # SKILLS
    # =========================================================

    def get_all_skills(self) -> set[str]:
        """
        Return all unique skills.
        """

        all_skills: set[str] = set()

        for employee in self.employees:
            all_skills.update(employee.skills)

        return all_skills