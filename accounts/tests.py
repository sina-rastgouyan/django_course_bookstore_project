from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your tests here.
class SignUpTest(TestCase):
    user_name = 'template_user'
    email_address = 'test@test.com'

    def test_signup_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed('signup.html')
    
    def test_signup_form(self):
        user = get_user_model().objects.create_user(
            self.user_name, self.email_address
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.user_name)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email_address)
