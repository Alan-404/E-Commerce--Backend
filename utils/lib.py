import random
from common.consts import length_id
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

patterns = "1234567890qwertyuiopasdfghjklzxcvbnm"

def create_id(length=length_id):
    id = ""
    for _ in range (length):
        id += random.choice(patterns)

    return id


def store_media(file,user_id, cluster=""):
    if os.path.exists(f"./storage/{cluster}") == False:
        os.mkdir(f"./storage/{cluster}")
    default_storage.save(f"./storage/{cluster}/{user_id}.jpg", ContentFile(file.read()))