from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa, Group
from .forms import AdicionarTarefa, EditarTarefaForm, AdicionarGrupo


def nova_tarefa(request):
    if request.method == 'POST':
        form = AdicionarTarefa(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('nova_tarefa')
    else:
        form = AdicionarTarefa()
    return render(request, 'tarefas/nova_tarefa.html', {'form': form})


def tarefas_pendentes_list(request):
    tarefas_pendentes = Tarefa.objects.filter(status='ativa')
    if request.method == 'POST':
        form = AdicionarTarefa(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas_pendentes_list')
    else:
        form = AdicionarTarefa()
    return render(request, 'tarefas/tarefas_pendentes.html', {'tarefas_pendentes': tarefas_pendentes, 'form': form})


def concluidas_list(request):
    tarefas_concluidas = Tarefa.objects.filter(status='concluida')
    if request.method == 'POST':
        form = AdicionarTarefa(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('concluidas_list')
    else:
        form = AdicionarTarefa()
    return render(request, 'tarefas/tarefas_concluidas.html', {'tarefas_concluidas': tarefas_concluidas, 'form': form})


def concluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'concluida'
    tarefa.due_date = date.today()
    tarefa.save()
    return redirect('tarefas_pendentes_list')


def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()
    return redirect('tarefas_pendentes_list')


def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        form = EditarTarefaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            tarefa.titulo = cd['titulo']
            tarefa.description = cd['description']
            tarefa.categorie = cd['categorie']
            tarefa.status = cd['status']
            tarefa.grupo = cd['grupo']
            tarefa.save()
            return redirect('tarefas_pendentes_list')
    else:
        form = EditarTarefaForm(
            initial={'titulo': tarefa.titulo, 'description': tarefa.description, 'categorie': tarefa.categorie,
                     'status': tarefa.status, 'grupo':tarefa.grupo})
    return render(request, 'tarefas/editar_tarefa.html', {'tarefa': tarefa, 'form': form})


def novo_grupo(request):
    groups = Group.objects.filter()
    if request.method == 'POST':
        form = AdicionarGrupo(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('novo_grupo')
    else:
        form = AdicionarGrupo()
    return render(request, 'tarefas/novo_grupo.html', {'groups': groups,'form': form})

def excluir_grupo(request, grupo_id):
    grupo = get_object_or_404(Group, id=grupo_id)
    grupo.delete()
    return redirect('novo_grupo')