from django.shortcuts import render, redirect
from django.contrib import messages
from .form import TodoForm
from .models import Todo
from datetime import datetime

# Create your views here.

def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        # form = TodoForm(request.POST)
        name = request.POST.get('names')
        detaile = request.POST.get('details')
        todo_content = Todo(title=name,details=detaile) #  ,date=datetime.today()
        # if todo_content.is_valid():
        todo_content.save()
        return redirect('todo')
    # form = TodoForm()
    
    page = {
        # 'forms' : form,
        'list' : item_list,
        'titles' : "AAAA STARK (TODO_LIST)",
    }
    return render(request,'todo/index.html',page)

def remove(request,item_id):
    item = Todo.objects.get(id = item_id)
    item.delete()
    messages.info(request, "TODO LIST IS DELETE!")
    return redirect('todo')
