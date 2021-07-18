from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    def test_create_user_with_email_sucessful(self):
        email = "abc@gmail.com"
        password = "test123"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalize(self):
        email = "abc@GMAILCOM"
        user = get_user_model().objects.create_user(email=email, password="test123")

        self.assertEqual(user.email, email.lower())
