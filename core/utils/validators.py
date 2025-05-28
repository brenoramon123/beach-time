import re


def validate_email(email: str) -> bool:
    """
    Valida emails. Retorna True ou False.
    """

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(pattern, email):
        return True
    else:
        return False
