from django.shortcuts import render,redirect, get_list_or_404,get_object_or_404
from aluno.models  import Aluno
from django.contrib import messages
from aluno.forms import AlunoForm

# Chamar a url para renderizar a página html.
# Classe para salvar os conteúdos no banco de dados.
def AddAluno(request):
    template_name = 'aluno/add_aluno.html'
    context = {}
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            # f = form.save(commit=False)
            form.save()
            messages.success(request, "Usuário salvo com sucesso!")
        else:
            messages.error(request, "Erro ao salvar dados!")
    form = AlunoForm()
    context['form'] = form
    return render(request,template_name,context)

def lista_alunos(request):
    template_name = 'aluno/lista_alunos.html'
    alunos = Aluno.objects.all().reverse()
    context = {
       'alunos':alunos 
    }
    return render(request, template_name, context)
