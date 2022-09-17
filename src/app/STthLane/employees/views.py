from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from employees.forms import RegisterEmployeeForm


# Create your views here.
def register(request):
    """ Is used when registering a new user """
    if request.method == 'POST':
        form = RegisterEmployeeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'register.html', {
        'form': RegisterEmployeeForm()
    })


def showUsers(request):
    """ Gives a list of all users/employees in the database """
    all_users = get_user_model().objects.all()
    context = {'allusers': all_users}
    return render(request, 'edit_employee.html', context)


def removeEmployee(request, user_id):
    """ Is used to remove a specific employee """
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect('edit')


def editEmployee(request, user_id):
    """ Is used to edit a specific employee """
    user = User.objects.get(pk=user_id)
    form = RegisterEmployeeForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('edit')
    return render(request, 'edit_emp_profile.html', {'user': user, 'form': form})
