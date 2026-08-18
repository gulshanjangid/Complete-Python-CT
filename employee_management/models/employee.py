from typing import Any


class Employee:
    """
    Represents a single employee.
    """

    def __init__(
        self,
        employee_id: int,
        name: str,
        age: int,
        email: str,
        department: str,
        salary: float,
        skills: set[str] | None = None
    ) -> None:

        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.email = email
        self.department = department
        self.salary = salary
        self.skills = skills if skills is not None else set()

    def to_dict(self) -> dict[str, Any]:
        """
        Convert Employee object into dictionary.
        """

        return {
            "id": self.employee_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "department": self.department,
            "salary": self.salary,
            "skills": list(self.skills)
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Employee":
        """
        Create Employee object from dictionary.
        """

        return cls(
            employee_id=int(data["id"]),
            name=str(data["name"]),
            age=int(data["age"]),
            email=str(data["email"]),
            department=str(data["department"]),
            salary=float(data["salary"]),
            skills=set(data.get("skills", []))
        )

    def __str__(self) -> str:
        """
        String representation of employee.
        """

        return (
            f"ID: {self.employee_id} | "
            f"Name: {self.name} | "
            f"Age: {self.age} | "
            f"Email: {self.email} | "
            f"Department: {self.department} | "
            f"Salary: ₹{self.salary:.2f} | "
            f"Skills: {', '.join(sorted(self.skills))}"
        )