import re


def get_integer(
    message: str,
    minimum: int | None = None,
    maximum: int | None = None
) -> int:
    """
    Safely get an integer from user.
    """

    while True:

        try:

            value = int(input(message))

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Value must be at most {maximum}.")
                continue

            return value

        except ValueError:

            print("Please enter a valid integer.")


def get_float(
    message: str,
    minimum: float | None = None
) -> float:
    """
    Safely get a floating-point number.
    """

    while True:

        try:

            value = float(input(message))

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            return value

        except ValueError:

            print("Please enter a valid number.")


def get_non_empty_string(
    message: str
) -> str:
    """
    Get non-empty string from user.
    """

    while True:

        value = input(message).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_email(message: str) -> str:
    """
    Validate email address.
    """

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    while True:

        email = input(message).strip()

        if re.match(pattern, email):
            return email

        print("Please enter a valid email.")


def get_skills(message: str) -> set[str]:
    """
    Convert comma-separated skills into a set.
    """

    while True:

        value = input(message).strip()

        if value:

            skills = {
                skill.strip()
                for skill in value.split(",")
                if skill.strip()
            }

            if skills:
                return skills

        print("Please enter at least one skill.")


def pause() -> None:
    """
    Pause the CLI.
    """

    input("\nPress Enter to continue...")