from django.db import models


#by inhriting models.Model this is how django knows that this is a model
#to create a database table from this model, we just need to create a migration
#python manage.py makemigrations drinks
#note that the name of your app must be included in the settings.py before making migrations
#the migration describes the change to our data structure but it doesn't apply that to the db
#python manage.py migrate: that will apply any unapplied migrations
class Drink(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=500)

    def __str__(self):
     return self.name