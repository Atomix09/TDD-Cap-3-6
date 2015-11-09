from django.conf.urls import url

from lists import views

urlpatterns = [
    url(r'^$', views.pagina_inicio, name='inicio'),
    # url(r'^admin/', include(admin.site.urls)),
]