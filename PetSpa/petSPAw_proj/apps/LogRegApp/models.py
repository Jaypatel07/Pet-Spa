from django.db import models
import re
import bcrypt
from datetime import datetime, time, date
from time import strftime


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
now = datetime.now()
class UserManager(models.Manager):
    def reg_validator(self, postData):
        result = {
            'status' : False,
            'errors' : []
        }
        if len(postData['name']) < 3:
            result['errors'].append("Please enter a first name with at least two characters")
        if not EMAIL_REGEX.match(postData['email']):
            result['errors'].append("Please enter a valid email")
        if User.objects.filter(email = postData['email']).count() > 0:
            result['errors'].append("email is already registered!")
        if len(postData['password']) < 8:
            result['errors'].append("Password should be at least eight characters")
        if postData['password'] != postData['confirmpw']:
            result['errors'].append("Passwords do not match")
        if len(result['errors']) == 0:
            result['status'] = True
           
            result['userid'] = User.objects.create(
                name=postData['name'],
                email=postData['email'],
                hashpw=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())).id
        return result

    def log_validator(self, postData):
        existing_user = User.objects.filter(email=postData['email'])
        result = {
            'status' : False,
            'errors' : []
        }
        if existing_user.count() == 0:
            result['errors'].append("Invalid login info")
        else:
            if bcrypt.checkpw(postData['password'].encode(), existing_user[0].hashpw.encode()):
                result['status'] = True
                result['userid'] = existing_user[0].id
            else:
                result['errors'].append("Invalid login info")
        return result
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    hashpw = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    