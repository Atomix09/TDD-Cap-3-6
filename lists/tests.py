from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import pagina_inicio #1

class PruebaPaginaInicio(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  #2
        self.assertEqual(found.func, pagina_inicio)  #3