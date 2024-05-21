from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonForm
from .models import Person


def person_list(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            Person.objects.create(**form.cleaned_data)
            return redirect('person_list')
    else:
        form = PersonForm()

    persons = Person.objects.all()
    return render(request, 'index.html', {'persons': persons, 'form': form})


def update_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm(instance=person)

    return render(request, 'update_person.html', {'form': form, 'person': person})


def delete_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'delete_person.html', {'person': person})
