from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from django.test import override_settings


class AuthenticationViewTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_view(self):
        client = Client()

        # Test when a user enters valid login credentials
        response = client.post(reverse('login'), {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 302)

        response = client.post(reverse('login'), {'username': self.username, 'password': 'incorrect'})
        self.assertEqual(response.status_code, 200)

    def test_login_view_template(self):
        client = Client()
        response = client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')


@override_settings(AUTH_PASSWORD_VALIDATORS=[])
class UserRegistrationTest(TestCase):
    def test_user_registration(self):
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'email': 'testuser@example.com',
            'firstname': 'John',
            'lastname': 'Doe',
        })
        self.assertEqual(response.status_code, 302)

        user_created = User.objects.filter(username='testuser').exists()
        self.assertTrue(user_created)


class UserLogoutTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_logout(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)