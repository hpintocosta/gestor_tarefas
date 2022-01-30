from django import forms
from .models import Group, Tarefa



class AdicionarTarefa(forms.ModelForm):
    grupo = forms.ChoiceField(choices=[],initial="Outras")

    def __init__(self, *args, **kwargs):
        super(AdicionarTarefa, self).__init__(*args, **kwargs)
        self.fields['grupo'].choices =[(i['group'], i['group']) for i in Group.objects.values('group').distinct()]

    class Meta:
        model = Tarefa
        fields = ('titulo','description','categorie','status','grupo')


class EditarTarefaForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(EditarTarefaForm, self).__init__(*args, **kwargs)
        self.fields['grupo'].choices = [(i['group'], i['group']) for i in Group.objects.values('group').distinct()]

    CATEGORIE_OPTIONS = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa ser feito', 'Precisa ser feito')
    )
    STATUS_OPTIONS = (
        ('concluida', 'Concluida'),
        ('ativa', 'Ativa')
    )

    titulo = forms.CharField(max_length=500)
    description = forms.CharField(widget=forms.Textarea,required=False)
    categorie = forms.ChoiceField(choices=CATEGORIE_OPTIONS)
    status = forms.ChoiceField(choices=STATUS_OPTIONS)
    grupo = forms.ChoiceField(choices=[])


class AdicionarGrupo(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('group',)
