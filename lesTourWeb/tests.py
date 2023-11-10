from django.test import TestCase
from django.urls import reverse

class MiAppVistaTests(TestCase):

    def test_vista_hoteles_funciona_correctamente(self):
        url = reverse('hoteles')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_url_personal_resuelve_correctamente(self):
        url = reverse('personal')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_url_usuario_resuelve_correctamente(self):
        url = reverse('usuario')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)