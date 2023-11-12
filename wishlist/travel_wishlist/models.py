from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage

# Create your models here.
class Place(models.Model):#this subclass describes Place table in db with 2 columns #The order of variables also seems to determine how they show up in the admin console
    name = models.CharField(max_length=200)#constraint
    visited = models.BooleanField(default=False)#assuming that users haven't visited places they add
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)#ForeignKey()is built into django models, 'auth.User' is the name of the other table (must be string), null=False is a constraint, cannot be null,
                                                                                                                                        #on_delete=models.CASCADE deletes all Places associated with a user if they are deleted
    notes = models.TextField(blank=True, null=True)#TextField has unlimited characters, unlike CharField, notes can be blank/empty, because they aren't required
    date_visited = models.DateField(blank=True, null=True)#can be blank/empty, because they aren't required
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True)#ImageField() needs 1 extra attribute. upload_to='user_images/ points to directory where images are uploaded. can be blank/empty

    def save(self, *args, **kwargs):#override django save method
        old_place = Place.objects.filter(pk=self.pk).first()#find old Place that is being updated if there is one
        if old_place and old_place.photo:
            if old_place.photo != self.photo:
                self.delete_photo(old_place.photo)#call method to #delete old place photo
        super().save(*args, **kwargs)#now call django generic save method

    def delete_photo(self, photo):#delete old photo if exists
        if default_storage.exists(photo.name):
            default_storage.delete(photo.name)

    def delete(self, *args, **kwargs):#if the Place object is deleted, any photos are also deleted in /media/user_images 
        if self.photo:
            self.delete_photo(self.photo)
        super().delete(*args, **kwargs)


    def __str__(self):
        photo_str = self.photo.url if self.photo else 'no photo'#url in this case referes to the filename of the photo. Need if self.photo else 'no photo' to ensure self.photo is not None. Same for self.notes.
        notes_str = self.notes[100:] if self.notes else 'no notes'#truncate to first 100 characters
        return f'{self.pk}: {self.name} visited? {self.visited} on {self.date_visited}. Notes: {notes_str}. Photo {photo_str}'#will not be displayed to user, but for the developer in admin console. Doesn't need extensive formatting, 
                                                                                                                                                                                #just useful information











