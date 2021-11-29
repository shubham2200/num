from django.shortcuts import render
from .models import number,Person,words
from .forms import PersonCreationForm
from django.contrib import messages
# Create your views here.

def home(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'userr is is saved successfully... ')
            return render(request, 'home.html')
        else:
            return render(request, 'home.html')
    else:
        return render(request, 'home.html', {'form': form})
    return render(request,'home.html')

def data(request):
    person = Person.objects.all()
    print(person)
    return render(request,'user_D.html',{'person':person})