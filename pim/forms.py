from django.forms import ModelForm

from models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['given_name','middle_name','last_name']
