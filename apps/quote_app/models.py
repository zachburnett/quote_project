from __future__ import unicode_literals

from django.db import models

# Create your models here.
class QuoteManager(models.Manager):
    def quoteVal(self, postdata):
        results = {'status': False, 'errors': []}
        if not postdata['quote'] or len(postdata['quote']) < 4:
            results['errors'].append('your quote needs to be atleast 4 characters long')
            results['status'] = True
        if not postdata['quoted_by'] or len(postdata['quoted_by']) < 3:
            results['errors'].append('the name has to be atleast 3 characters long')
        if results['status'] == False:
            if len(self.filter(quote = postdata['quote'], quoted_by= postdata['quoted_by'])) == 0:
                results['Quote'] = self.create(quote = postdata['quote'], quoted_by = postdata['quoted_by'], )
            else:
                results['errors'].append('quote has already been created')
                results['status'] = True
        print"*" *50
        return results  

    

class Quote(models.Model):  
    quote = models.CharField(max_length = 255)
    quoted_by = models.CharField(max_length = 255)
    objects = QuoteManager()
    def __str__(self):
        return "{},{}".format(self.quoted_by, self.quote)