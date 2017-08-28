from __future__ import unicode_literals
import bcrypt
from django.db import models
import re
# Create your models here.
class UserManager(models.Manager):
    def regVal(self, postdata):
        results = {'status': True, 'errors':[]}
        if len(postdata['name']) <5:
            results['errors'].append('your full name must be more then 5 characters')
        if len(postdata['alias']) < 3:
            results['errors'].append('your alias must be atleast 3 characters long')
        if not re.match(r'(\w+[.|\w])*@(\w+[.])*\w+',postdata['email']):
            results['errors'].append('please use a valid email')
        if len(postdata['password']) < 5:
            results['errors'].append('your password must be atleast 5 characters long')
        if postdata['password'] != postdata['c_password']:
            results['errors'].append('your passwords dont match')
        if len(self.filter(email= postdata['email'])) >0:
            results['errors'].append('user already exsits')
        if len(results['errors']) >0:
            results['status'] = False
        print results
        return results

    def creator(self, postdata):
        hashed = bcrypt.hashpw(postdata['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(name = postdata['name'],
        alias = postdata['alias'],email = postdata['email'],
        dob = postdata['dob'], password = hashed)
        return user
    def loginVal(self, postdata):
        results = {'status': True, 'errors':[], 'user': None}
        user = self.filter(email = postdata['email'])
        if len(user) < 1:
            results['errors'].append('something went wrong with email')
        else:
            if bcrypt.checkpw(postdata['password'].encode(),user[0].password.encode()) == False:
                results['errors'].append('password did not match')
            if len(results['errors']) > 0 :
                results['status'] = False
            else:
                results['user'] = user[0]
            return results

class User(models.Model):
    name = models.CharField(max_length= 255)
    alias = models.CharField(max_length= 255)
    email = models.CharField(max_length= 255)
    password = models.CharField(max_length= 255)
    dob = models.DateTimeField(auto_now=False)
    quote_own = models.ManyToManyField('quote_app.Quote', related_name='quoter')
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    objects = UserManager()
    def __str__(self):
        return "{},{},{}".format(self.name, self.alias,self.email)