from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class HomePageTests(TestCase):
    def test_home_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_home_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response,'This is home page')
    
    def test_home_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed('home.html')