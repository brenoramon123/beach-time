import re
import unicodedata

from .validators import validate_email


def cpf_cnpj_only_numbers(cpf_cnpj: str) -> str:
    """
    Função para remover formatação de CPF e CNPJ.
    """

    cpf_cnpj = re.sub('[^0-9]', '', cpf_cnpj)
    return cpf_cnpj


def only_numbers(string: str) -> str:
    """
    Função que remove caracteres especiais e letras.
    """
    if string is not None:
        string = re.sub('[^0-9]', '', string)
        return string


def only_numbers_letters(string: str) -> str:
    """
    Função que define uma expressão regular para encontrar caracteres especiais e
    usa a função sub() do módulo re para substituí-los por uma string vazia.
    """

    string = re.sub(r'[^a-zA-Z0-9\s]', '', string)
    return string


def license_plate_only_alphanumeric(plate: str) -> str:
    """
    Função que remove espaços em branco e caracteres especiais da placa
    e converte todos os caracteres para maiúsculo.
    """

    plate = plate.upper()
    license_plate: str = re.sub(r'[^A-Z0-9]', '', plate)

    return license_plate


def remove_excess_spaces(text: str) -> str:
    """
    Remove espaços em branco extras.
    """

    if text is None:
        return ''

    text_without_extra_space: str = re.sub(r'\s+', ' ', text)
    return text_without_extra_space.strip()


def mask_username_email(email) -> str:
    """
    Função que mascara o 'username' de email do usuário.
    """
    if validate_email(email):
        username, domain = email.split('@')
        if len(username) <= 6:
            username_mask = (
                username[:1] + '*' * (len(username) - 2) + username[-1:]
            )
            email_username_mask = f'{username_mask}@{domain}'
            return email_username_mask
        # Mask part of the user name (keeping at least 3 characters)
        username_mask = (
            username[:3] + '*' * (len(username) - 6) + username[-3:]
        )
        email_username_mask = f'{username_mask}@{domain}'
        return email_username_mask
    else:
        return 'Email inválido!'


def convert_to_db_date(date: str) -> str:
    """
    Função que converte a data para o formato aceito pelo banco de dados.
    """

    return '-'.join(reversed(date.split('/')))


def strip_accents(s):
    return ''.join(
        c
        for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    )
