from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.gif', upload_to='profile_pics')
    bio = models.TextField(max_length=600, default="", blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save(**kwargs)

        img = Image.open(self.image.path)

        print(self.image)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

