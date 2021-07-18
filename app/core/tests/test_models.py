from django.test import Testcase
from django.contrib.auth import get_user_model

class ModelTests(Testcase):

    def test_create_user_with_email_sucessful(self):
        email = "abc@gmail.com"
        password = "test123"
        user = get_user_model().obejects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email. email)
        self.assertTrue(user.check_password(password))        
