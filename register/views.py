from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def register_view(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Saves to SQLite3
            return redirect('success')
    else:
        form = StudentForm()
    return render(request, 'register_form.html', {'form': form})

def success_view(request):
    students = Student.objects.all()
    return render(request, 'success.html', {'students': students})
