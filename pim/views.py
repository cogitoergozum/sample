from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from models import Person
from forms import PersonForm

# Create your views here.
def index(request):
    #return HttpResponse('Hello, django World!')

    p=Person.objects.all()
    context = {
        'Title': 'Ang Title',
        'text_str': 'Welcome to Django',
        'persons':p,
    }
    return render(request,"base.html", context=context)

def editperson(request,person_id):
    #p=Person.objects.get(pk=person_id)
    p=get_object_or_404(Person, pk=person_id)


    if request.method=="POST":
        form= PersonForm(request.POST,instance=p)
        if form.is_valid():
            form.save()
    else:
        p=Person.objects.first()
        form=PersonForm(instance=p)



    return render(request,'editperson.html',{'form':form,'Title':'Edit Person'})

def listpersons(request):
    persons =Person.objects.all()

    return render(request,'listperson.html',{'persons':persons,'Title':'Edit'})



