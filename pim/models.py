from __future__ import unicode_literals

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

    def __unicode__(self):
        return self.fullname



