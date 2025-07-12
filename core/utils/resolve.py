import os
from datetime import datetime
from mimetypes import guess_type as guess_file_type

from django.apps import apps


def image_saving_location(instance, file):
    """
    Função que retorna o local correto para salvar o arquivo,
    usando o nome completo do app que o model está.
    """
    model_app_label = instance._meta.app_label
    full_app_label = apps.get_app_config(model_app_label).name
    full_app_label_list = full_app_label.split('.')

    file_extension = file.split('.')[-1]
    formatted_datetime = datetime.now().strftime('%d-%m-%Y_%H-%M-%S-%f')

    file_type = guess_file_type(file)[0]
    general_file_type = file_type.split('/')[0]
    type_folder = general_file_type

    file_name = f'{formatted_datetime}.{file_extension}'

    return os.path.join(*full_app_label_list, type_folder, file_name)


def file_saving_location(instance, file):
    """
    Função que retorna o local correto para salvar o arquivo,
    usando o nome completo do app passado pelo controller
    na qual foi realizado a requisição.
    """

    full_app_label = file.split('-')[0]
    full_app_label_list = full_app_label.split('.')

    file_type = guess_file_type(file)[0]
    general_file_type = file_type.split('/')[1]
    type_folder = general_file_type

    formatted_datetime = datetime.now().strftime('%d-%m-%Y_%H-%M-%S-%f')
    file_name = file.split('-')[1]
    file_name = f'{formatted_datetime}-{file_name}'

    return os.path.join(*full_app_label_list, type_folder, file_name)
