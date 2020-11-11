from django.db import models
# Create your models here.

class ScrumManager(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

PRIORITY_CHOICES = (
    ("High", "High"),
    ("Low", "Low"),
    ("Medium", "Medium"),

)


class Project(models.Model):
    name = models.CharField(max_length=20)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    # Scrum Manager can have many Projects, but a particular Project can have only one Scrum Manager
    scrum_manager = models.ForeignKey(ScrumManager, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Developer(models.Model):
    username = models.CharField(max_length=20)
    # Project can have many Developers, but a particular Developer can have only one Project
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.username




