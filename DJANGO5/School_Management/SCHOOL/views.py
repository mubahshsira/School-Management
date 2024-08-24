from django.shortcuts import render, redirect, get_object_or_404
from .models import School
from .school_form import school_form  # Use the correct import name for your form

# Create your views here.
def school_list(request):
    schools = School.objects.all()  # Use 'schools' to match the context variable
    return render(request, 'school_list.html', {'schools': schools})

def school_create(request):
    if request.method == 'POST':
        form = school_form(request.POST)  # Use the correct form class
        if form.is_valid():
            form.save()
            return redirect('school_list')
    else:
        form = school_form()
    return render(request, 'school_create.html', {'form': form})

def school_update(request, id):
    school = get_object_or_404(School, pk=id)  # Use get_object_or_404 for better error handling
    if request.method == 'POST':
        form = school_form(request.POST, instance=school)  # Pass the instance of the object
        if form.is_valid():
            form.save()
            return redirect('school_list')
    else:
        form = school_form(instance=school)
    return render(request, 'school_create.html', {'form': form})

def school_delete(request, id):
    school = get_object_or_404(School, pk=id)  # Use get_object_or_404 for better error handling
    school.delete()
    return redirect('school_list')
