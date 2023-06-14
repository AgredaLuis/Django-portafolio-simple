from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    """ se crea un objeto de todos los projects encontrados con Projects.all que busca dentro del modelo  """
    projects = Project.objects.all()

    return render(request, 'home.html', {'projects': projects})