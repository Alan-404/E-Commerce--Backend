import random
from common.consts import length_id
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

patterns = "1234567890qwertyuiopasdfghjklzxcvbnm"

def create_id(length=length_id):
    id = ""
    for _ in range (length):
        id += random.choice(patterns)

    return id


def store_media(file,user_id):
    default_storage.save(f"./storage/{user_id}.png", ContentFile(file.read()))