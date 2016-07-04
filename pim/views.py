from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from models import Student
from forms import StudentForm

# Create your views here.
def index(request):
    #return HttpResponse('Hello, django World!')

    s=Student.objects.all()
    context = {
        'Title': 'Ang Title',
        'text_str': 'Welcome to Django',
        'persons':s,
    }
    return render(request,"base.html", context=context)

def editperson(request,person_id):
    #p=Person.objects.get(pk=person_id)
    p=get_object_or_404(Student, pk=person_id)


    if request.method=="POST":
        form= StudentForm(request.POST,instance=p)
        if form.is_valid():
            form.save()
    else:
        s=Student.objects.first()
        form=StudentForm(instance=p)



    return render(request,'editperson.html',{'form':form,'Title':'Edit Person'})

def listpersons(request):
    persons =Student.objects.all()

    return render(request,'listperson.html',{'persons':persons,'Title':'Edit'})



