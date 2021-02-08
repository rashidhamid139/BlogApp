import os
from unittest import TestCase, mock
from django.test import TestCase

# Create your tests here.
class SettingsTests(TestCase):
    @mock.patch.dict(os.environ, {"FROBNICATION_COLOUR": "ROUGE" })
    def test_frobnication_colour(self):
        colour  = "ROUGE"
        self.assertEqual( colour, Colour.ROUGE)