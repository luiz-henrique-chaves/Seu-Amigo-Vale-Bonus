from django.shortcuts import render, redirect
from indicado.models import Indicado
from indicado.forms import IndicadoForm
from django.contrib.auth.decorators import login_required

#ModelName.objects.filter(id=id).update(status='closed')
#exemplo de manipulação de model

@login_required(login_url='login')
def create_indicado(request, **kwargs):
    indicados_cont = len(Indicado.objects.filter(id_usuario=request.user))
    if indicados_cont < 10:
        form = IndicadoForm(request.POST or None)   
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('indicacoes')
    else:
        return render(request, 'aviso.html')

    return render(request, 'indicado-form.html', {'form': form})

@login_required(login_url='login')
def update_indicado(request, id):
    indicado = Indicado.objects.get(id=id)
    if str(indicado.id_usuario) == str(request.user):
        #impede que o usuário edite informações de indicados de outros alunos
        form = IndicadoForm(request.POST or None, instance=indicado)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        redirect('home')
    return render(request, 'indicado-form.html', {'form': form, 'indicados': indicado })

@login_required(login_url='login')
def delete_indicado(request, id):
    indicado = Indicado.objects.get(id=id)
    if request.method == 'POST':
        indicado.delete()
        return redirect('home')
    return render(request, 'indicado-delete-confirm.html', {'indicado': indicado})
