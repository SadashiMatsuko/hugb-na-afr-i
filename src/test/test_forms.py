from django.test import TestCase
from app.STthLane.employees.forms import RegisterEmployeeForm
from app.STthLane.bookings.forms import CreateBookingForm


class TestForms(TestCase):


    def test_register_employee_form_not_valid_data(self):
        form = RegisterEmployeeForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)

    def test_booking_form(self):
        form = CreateBookingForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)
