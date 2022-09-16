from django.contrib.auth import get_user_model
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
    """  """
    all_users = get_user_model().objects.all()
    context = {'allusers': all_users}
    return render(request, 'edit_employee.html', context)


def removeEmployee(request):
    pass


def editEmployee(request):
    pass
