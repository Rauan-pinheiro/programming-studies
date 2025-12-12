# cadastros/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa
from .forms import PessoaForm

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'cadastros/listar_pessoas.html', {'pessoas': pessoas})

def criar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'cadastros/pessoa_form.html', {'form': form})

def atualizar_pessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'cadastros/pessoa_form.html', {'form': form})

def deletar_pessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('listar_pessoas')
    return render(request, 'cadastros/confirmar_delete.html', {'pessoa': pessoa})