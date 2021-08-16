from django.shortcuts import render, redirect
from aluno.models import Aluno
from aluno.forms import AlunoForm
from indicado.models import Indicado
from django.contrib.auth.decorators import login_required

USUARIO = dict()

@login_required(login_url='login')
def home(request):
    
    indicados = Indicado.objects.filter(id_usuario=request.user)
    if Aluno.objects.filter(id_usuario=request.user):
        return render(request, 'accounts/inicio.html', {'indicados': indicados})
    else:
        return redirect('create_aluno', profile=str(request.user))

@login_required(login_url='login')
def indicacoes(request):    
    indicados = Indicado.objects.filter(id_usuario=request.user)
    if Aluno.objects.filter(id_usuario=request.user):
        return render(request, 'indicacoes.html', {'indicados': indicados})
    else:
        return redirect('create_aluno', profile=str(request.user))
    

@login_required(login_url='login')
def create_aluno(request, **kwargs):
    global USUARIO
    USUARIO['USER'] = str(request.user)
    USUARIO['ID'] = request.user.id

    if Aluno.objects.filter(id_usuario=request.user):
        aluno = Aluno.objects.get(id_usuario=request.user)
        return redirect('home')
    else: 
        form = AlunoForm(request.POST or None)   
        if request.method == 'POST':
            print(form.__dict__)            
            if form.is_valid():
                # se form é valido mas não está salvando, 
                # é porque o banco está limitando a quantidade de caracteres a ser salvo
                #modificar essa informação em models
                form.save()
                return redirect('home')         
        return render(request, 'aluno-form.html', {'form': form})

@login_required(login_url='login')
def update_aluno(request, user):
    if str(user) == str(request.user):
        aluno = Aluno.objects.get(id_usuario=user)
        alunos = Aluno.objects.get(id=aluno.id)
        form = AlunoForm(request.POST or None, instance=alunos)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    else:
        return redirect('home')
    
    return render(request, 'aluno-form.html', {'form': form, 'aluno': alunos})

@login_required(login_url='login')
def visualizar_perfil(request, user):
    indicados_cont = len(Indicado.objects.filter(id_usuario=request.user))
    matriculados_cont = len(Indicado.objects.filter(status="Matriculado"))
    pendentes_cont = len(Indicado.objects.filter(status="Pendente"))

    if str(user) == str(request.user): #impedindo que usuários vejam perfis de outros usuários
        if Aluno.objects.filter(id_usuario=request.user):
            aluno = Aluno.objects.get(id_usuario=user)
        else:
            return redirect('create_aluno', profile=str(request.user))
    else:
        return redirect('home')

    return render(request, 'profile.html', {'aluno': aluno, 'indicados_cont': indicados_cont, 'matriculados_cont': matriculados_cont, 'pendentes_cont': pendentes_cont})

@login_required(login_url='login')
def delete_aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('home')
    return render(request, 'aluno-delete-confirm.html', {'aluno': aluno})
