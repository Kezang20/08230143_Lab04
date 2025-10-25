from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class LearningEntry(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
