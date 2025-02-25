import unittest
from django.test import TestCase
from django.urls import reverse

class NavigationBarTest(TestCase):

    def test_navigation_bar_displayed(self):
        # Realiza una solicitud GET a la página principal
        response = self.client.get(reverse('home'))  # Asegúrate de que 'home' es la URL correcta para la página que contiene la barra de navegación
        
        # Verifica si la respuesta contiene el ID o clase de la barra de navegación
        self.assertContains(response, 'id="navbar"')  # Asegúrate de que el ID coincide con el de tu barra de navegación
