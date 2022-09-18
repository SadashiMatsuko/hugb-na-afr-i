from django.test import TestCase, Client
from django.urls import reverse
from app.STthLane.employees.views import register, showUsers, removeEmployee, editEmployee
from app.STthLane.news.views import create_article


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.edit_url = reverse('edit')
        self.register_url = reverse('register')
        self.remove_url = reverse('remove-employee', args=[1])
        self.edit_emp_url = reverse('edit-employee', args=[1])
        self.create_article_url = reverse('news:create_article')

    def test_show_users_GET(self):
        response = self.client.get(self.edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_employee.html')

    def test_register_GET(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_remove_employee_GET(self):
        response = self.client.get(self.remove_url)
        self.assertEquals(response.status_code, 302)

    def test_edit_employee_GET(self):
        response = self.client.get(self.edit_emp_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_emp_profile.html')

    def test_show_users_POST(self):
        response = self.client.post(self.edit_url)
        self.assertEquals(response.status_code, 200)

    def test_register_POST(self):
        response = self.client.post(self.register_url)
        self.assertEquals(response.status_code, 200)

    def test_remove_employee_POST(self):
        response = self.client.post(self.remove_url)
        self.assertEquals(response.status_code, 302)

    def test_edit_employee_POST(self):
        response = self.client.post(self.edit_emp_url)
        self.assertEquals(response.status_code, 200)

    def test_create_article_POST(self):
        response = self.client.post(self.create_article_url)
        self.assertEquals(response.status_code, 200)




