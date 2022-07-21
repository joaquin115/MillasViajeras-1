import datetime
from django.test import TestCase

from .models import Publicaciones, Persona
# Create your tests here.

class PublicacionesTest(TestCase):

    def setUp(self):
        Publicaciones.objects.create(pais="Argentina", titulo="Paseando por Recoleta", descripcion="Gran viaje por Argentina", fecha_viaje=datetime.datetime.today())

    def test_publicacion_pais(self):
        publicacion = Publicaciones.objects.get(pais="Argentina")
        self.assertEqual(publicacion.titulo, "Paseando por Recoleta")

    def test_publicacion_descripcion(self):
        publicacion = Publicaciones.objects.get(titulo="Paseando por Recoleta")
        self.assertEqual(publicacion.descripcion, "Gran viaje por Argentina")    