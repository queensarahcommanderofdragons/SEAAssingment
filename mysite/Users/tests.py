from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User

class UserRegistrationTest(TestCase):

    def test_user_registration(self):
        # Set up the data for a new user
        response = self.client.post('/register/', {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })

        # Check if the response redirects to the login page (status code 302)
        self.assertEqual(response.status_code, 302)

        # Check if the user was created successfully
        user_exists = User.objects.filter(username='testuser').exists()
        self.assertTrue(user_exists)

