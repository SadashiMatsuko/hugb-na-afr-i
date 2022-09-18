from django.contrib.auth.views import LoginView, LogoutView
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.STthLane.employees.views import register, showUsers, removeEmployee, editEmployee


class TestUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func.__name__, register.__name__)

    def test_edit_url_is_resolved(self):
        url = reverse('edit')
        print(resolve(url))
        self.assertEquals(resolve(url).func.__name__, showUsers.__name__)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func.__name__, "view")

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func.__name__, "view")

    def test_remove_employee_url_is_resolved(self):
        url = reverse('remove-employee', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.__name__, removeEmployee.__name__)

    def test_edit_employee_url_is_resolved(self):
        url = reverse('edit-employee', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.__name__, editEmployee.__name__)



