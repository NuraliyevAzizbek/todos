from django.shortcuts import render, redirect
from django.contrib import messages 

from .models import Todo
from .forms import FilterTodoForm,AddTodoForm,UpdateTodoForm


# Create your views here.
def todo(request):
    todos = Todo.objects.all()
    form = FilterTodoForm()
    if request.method == "GET":
        form = FilterTodoForm(data=request.GET)
        if form.is_valid():
            todos = form.save()


    add_form = AddTodoForm()
    if request.method == "POST":
        add_form = AddTodoForm(data=request.POST)
        if add_form.is_valid():
            add_form.save()
            
    context = {
        "todos": todos,
        "form":form,
        "add_form":add_form,
        }
    return render(request, "todo.html", context)


def todo_delete(request, pk):
    try:
        todo = Todo.objects.get(id = pk)
        if request.method == "POST":
            todo.delete()
    except Exception as e:
        messages.error(request, f"Xato: {e}")
        return redirect("todo")
    return redirect("todo")


def todo_update(request, pk):
    try:
        update_form = UpdateTodoForm()
        if request.method == "POST":
            update_form = UpdateTodoForm(data=request.POST)
            if update_form.is_valid():
                update_form.save(pk)
                
    except Exception as e:
        messages.error(request, f"Xato: {e}")
        return redirect("todo")

    context = {
        'todo':todo,
        'update_form':update_form,
        }

    return render(request, 'update.html', context)

def todo_isdone(request, pk):
    try:
        todo = Todo.objects.get(id = pk)
        if request.method == "POST":
            if todo.is_done == True:
                todo.is_done = False
            else:
                todo.is_done = True

            todo.save()   
    except Exception as e:
        messages.error(request, f"Xato: {e}")
        return redirect("todo") 
    return redirect("todo")
