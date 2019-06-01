from django.db import models
from apps.LogRegApp.models import User
from datetime import datetime, time, date
from time import strftime

class PetManager(models.Manager):
    def pet_validator(self, postData):
        today = datetime.now()

        now= today.strftime("%Y-%m-%d")
       
        result = {
            'status' : False,
            'errors' : []
        }
        if len(postData['name']) < 2:
            result['errors'].append("Name needs to be at least two characters")
        if len(postData['age']) < 1:
            result['errors'].append("Age is required")
        if len(postData['breed']) < 2:
            result['errors'].append("Breed is required")
        if len(result['errors']) < 1:
            result['status'] = True
            newPet = Pet.objects.create(name=postData['name'], age=postData['age'], breed=postData['breed'], comments=postData['comments'], created_by=User.objects.get(id=postData['userid']))
            newPet.pet_members.add(User.objects.get(id=postData['userid']))
            newPet.save()
        return result
    
    def edit(self, postData):
        today = datetime.now()

        now= today.strftime("%Y-%m-%d")
       
        result = {
            'status' : False,
            'errors' : []
        }
        if len(postData['name']) < 2:
            result['errors'].append("Name needs to be at least two characters")
        if len(postData['age']) < 1:
            result['errors'].append("Age is required")
        if len(postData['breed']) < 2:
            result['errors'].append("Breed is required")
        if len(result['errors']) < 1:
            result['status'] = True
        return result
    

class Pet(models.Model):
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=3)
    breed = models.CharField(max_length=255)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pet_members = models.ManyToManyField(User, related_name="joined_pets", null=True)
    created_by = models.ForeignKey(User, related_name="created_pets", null=True)
    objects = PetManager()
    