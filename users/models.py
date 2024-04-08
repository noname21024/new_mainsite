from django.db import models
from django.contrib.auth.models import User
from core.models import Mangas, Chapters
from PIL import Image



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.width > 300 or img.height > 300:
            out_size = (300, 300)
            img.thumbnail(out_size)
            img.save(self.image.path)