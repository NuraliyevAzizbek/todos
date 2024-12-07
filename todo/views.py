from django.shortcuts import render, redirect
from django.contrib import messages 

from .models import Todo


# Create your views here.
def todo(request):
    done_filter = request.GET.get("done_filter", "")
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        deadline = request.POST.get("deadline")
        Todo.objects.create(title=title, description=description, deadline=deadline)
    todos = Todo.objects.all()
    if done_filter == "isdone":
        todos = todos.filter(is_done = True)
    elif done_filter == "isnotdone":
        todos = todos.filter(is_done = False)
    context = {"todos": todos}
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
        todo = Todo.objects.get(id = pk)
        if request.method == "POST":
            title = request.POST.get("title")
            description = request.POST.get("description")
            deadline = request.POST.get("deadline")
            #update
            todo.title=title
            todo.description=description
            todo.deadline=deadline
            todo.save()
    except Exception as e:
        messages.error(request, f"Xato: {e}")
        return redirect("todo")

    context = {'todo':todo}

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
