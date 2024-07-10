from django.db import models

# Create your models here.


class File(models.Model):
    filename=models.CharField(max_length=400)
    content=models.BinaryField()

    def __str__(self):
        return self.filename