from django.db import models

class Tarefa(models.Model):

    CATEGORIE_OPTIONS = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('sem prioridade', 'Sem prioridade')
    )
    STATUS_OPTIONS = (
        ('concluida', 'Concluida'),
        ('ativa', 'Ativa')
    )

    titulo = models.CharField(max_length=500, default="")
    description = models.TextField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    categorie = models.CharField(choices=CATEGORIE_OPTIONS ,max_length=100, default='importante')
    status = models.CharField(choices=STATUS_OPTIONS ,max_length=200, default='ativa')
    grupo = models.CharField(max_length=200,blank=True)

class Group(models.Model):
    group = models.CharField(max_length=200, default="")




