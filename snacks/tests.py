from django.test import SimpleTestCase
from django.urls import reverse

class SnacksTestCase(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_about_page_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about.html')
        self.assertTemplateUsed(response, 'base.html')
