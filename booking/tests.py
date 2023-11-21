from django.test import TestCase
from .forms import BookingForm

# Create your tests here.
class BookingPageTest(TestCase):

    def test_booking_form_date_field_label(self):
        form = BookingForm()
        self.assertTrue(
            form.fields['timeslot'].label is None or form.fields['timeslot'].label =='timeslot')