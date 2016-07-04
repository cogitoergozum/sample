from __future__ import unicode_literals

import datetime
from django.db import models

# Create your models here.
def nameField(**kargs):
    kargs.setdefault('max_length',60)
    kargs.setdefault('blank',False)
    kargs.setdefault('default','')
    return models.CharField(**kargs)



class Student(models.Model):
    id_number = models.CharField(max_length=20, unique=True)
    given_name = nameField()
    last_name=nameField()
    middle_name=nameField(blank=True)

    @property
    def fullname(self):
        mi = " %c." % self.middle_name[0] if self.middle_name else ''


        return "%s, %s%s" % (self.last_name,self.given_name,mi)

class Ledger(models.Model):
    date = models.DateField(default=datetime.date.today)
    particulars = models.CharField(max_length=200)
    reference_number = models.CharField(max_length=80)
    credit = models.CharField(max_length=30)
    debit = models.CharField(max_length=30)



    def __unicode__(self):
        return self.fullname



