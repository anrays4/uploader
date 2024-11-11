import random
from django.db import models
import os


def get_filename_deposit(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_deposit_image_path(instance, filename):
    name, ext = get_filename_deposit(filename)
    random_id = random.randint(1, 100000)
    final_name = f'{random_id}-{instance}'
    return f"uploaded/{final_name}"


class UploadedFile(models.Model):
    file = models.FileField(upload_to=upload_deposit_image_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
