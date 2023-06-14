from django.urls import path
from .views import render_posts, post_detail

app_name = 'blog'


""" aqui deben estaer rutas creadar en views.py """


urlpatterns = [
    path('', render_posts, name='post'),
    path('<int:post_id>', post_detail, name='post_detail')
]