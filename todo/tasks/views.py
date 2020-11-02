from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

# Create your views here.
def index(request):
	if request.method == 'POST':
		form = TodoForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect('index')
		else:
			print('Invalid form')
	else:
		todos = Todo.objects.all()
		return render(request,'todo.html',{'todos':todos})

def delete(request, todo_id):
	todo = Todo.objects.get(id=todo_id)
	todo.delete()
	return redirect('index')

def edit(request, todo_id):
	if request.method == 'POST':
		todo = Todo.objects.get(id=todo_id)
		form = TodoForm(request.POST or None, instance=todo)
 
		if form.is_valid():
			form.save()
			messages.success(request, ('Task has been edited!'))
			return redirect('index')
	else:
		todo = Todo.objects.get(id=todo_id)
		todos = Todo.objects.all()
		return render(request, 'edit_todo.html', {'todo': todo,'todos':todos})