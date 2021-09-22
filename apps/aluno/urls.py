from django.urls import path, include
from . import views

app_name = 'aluno'

# Chamar a view.
urlpatterns = [
    path('', views.AddAluno, name='add_aluno'),
    path('lista/', views.lista_alunos, name='lista_alunos'),
]
