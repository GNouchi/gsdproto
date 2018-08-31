from django.db import models
from django.core.validators import validate_email
import bcrypt
import re
USERNAME_REGEX = re.compile('^[a-zA-Z0-9][a-zA-Z0-9._-]')
EMAIL_REGEX =  re.compile(r'^[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]+$')

class UserManager(models.Manager):
    def regValidator(request, postData):
        result = {'errors': []}
        if len(postData['email']) < 1:
             result['errors'].append("Email is blank")
        if len(postData['password']) < 1 or len(postData['confirm_password'])< 1:
             result['errors'].append("Password is blank")
        if len(postData['password']) > 30 or len(postData['confirm_password']) > 30:
             result['errors'].append("Password maximum is 30 characters")
        if postData['password'] != postData['confirm_password']:
             result['errors'].append("Your Passwords do not match")
        throwaway = User.objects.filter(email = postData['email'])
        if len(throwaway) > 0 :
            result['errors'].append("That email is already registered")    
        if not EMAIL_REGEX.match(postData['email']):
            result['errors'].append("Please choose another email")
            print("email regex fail")

        if len(result['errors']) > 0:
            print(str(len(result['errors'])) + "Errors found, escaping now")
            return result            
            
# ******************************** VALIDATION PASS *************************************
        print("regValidator Pass")
        hash1 = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        hash1= hash1.decode()
        newUser = User.objects.create(
            email = postData['email'],
            password = hash1,
        )
        result['user_id'] = newUser.id
        return result

    def loginValidator(self, postData):
        result = {'errors':[]}
        throwaway = User.objects.filter(email = postData['email'])
        if len(throwaway) > 0:
            if bcrypt.checkpw(postData['password'].encode(),throwaway[0].password.encode() ):
                result['user_id'] = throwaway[0].id
                return result
        result['errors'].append("Password or Email did not match")
        return result  



class User(models.Model):
    username = models.CharField(max_length= 50 , blank = True, null = True)
    email = models.CharField(max_length =100)
    password = models.CharField(max_length = 255)
    objects = UserManager()