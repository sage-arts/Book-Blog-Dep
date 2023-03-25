from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from cloudinary.models import CloudinaryField
# from PIL import Image

class Profile(models.Model):
    GENRE_CHOICES = (
        ('science_fiction', 'Science Fiction'),
        ('mystery', 'Mystery'),
        ('romance', 'Romance'),
        ('fantasy', 'Fantasy'),
        ('adventure', 'Adventure'),
        ('horror', 'Horror'),
        ('dystopian', 'Dystopian'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    genre_interests = MultiSelectField(choices=GENRE_CHOICES, max_choices=4, max_length=40)
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)