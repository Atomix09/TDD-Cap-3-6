from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import pagina_inicio


class PruebaPaginaInicio(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, pagina_inicio)


    def test_pagina_de_inicio_regresa_correctamente(self):
        request = HttpRequest()
        response = pagina_inicio(request)
        expected_html = render_to_string('Inicio.html')
        self.assertEqual(response.content.decode(), expected_html)

	def test_pagina_de_inicio_puede_guardar_un_POST(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['texto_libro'] = 'Una nueva lista de libro'

		response = pagina_inicio(request)

		self.assertIn('Una nueva lista de libro', response.content.decode())
		expected_html = render_to_string(
			'Inicio.html',
			{'nuevo_texto_libro':  'Una nueva lista de libro'}
			)
		self.assertEqual(response.content.decode(), expected_html)