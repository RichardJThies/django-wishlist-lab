from django.db import models

# Create your models here.
class Place(models.Model):#this subclass describes Place table in db with 2 columns
    name = models.CharField(max_length=200)#constraint
    visited = models.BooleanField(default=False)#assuming that users haven't visited places they add

    def __str__(self):
        return f'{self.name} visited? {self.visited}'#will not be displayed to user, but for the developer in admin console. Doesn't need extensive formatting, just useful information











