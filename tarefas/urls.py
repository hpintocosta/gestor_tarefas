from django.urls import path
from . import views

urlpatterns = [
    path('', views.tarefas_pendentes_list, name='tarefas_pendentes_list'),
    path('new/', views.nova_tarefa, name='nova_tarefa'),
    path('concluidas/', views.concluidas_list,name='concluidas_list'),
    path('novo_grupo/', views.novo_grupo,name='novo_grupo'),
    path('<int:tarefa_id>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
    path('<int:tarefa_id>/excluir/', views.excluir_tarefa, name='excluir_tarefa'),
    path('<int:tarefa_id>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('<int:grupo_id>/excluir_grupo/', views.excluir_grupo, name='excluir_grupo')
]