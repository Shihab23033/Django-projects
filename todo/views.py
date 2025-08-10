from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import ToDo
from .forms import ToDoForm

def todo_list(request):
	todos = ToDo.objects.all().order_by('-created_at')
	form = ToDoForm()
	return render(request, 'todo/todo_list.html', {'todos': todos, 'form': form})

def add_todo(request):
	if request.method == 'POST':
		form = ToDoForm(request.POST)
		if form.is_valid():
			todo = form.save()
			if request.headers.get('x-requested-with') == 'XMLHttpRequest':
				return JsonResponse({'id': todo.id, 'description': todo.description, 'is_complete': todo.is_complete, 'created_at': todo.created_at.strftime('%Y-%m-%d %H:%M')})
			return redirect('todo_list')
	return JsonResponse({'error': 'Invalid request'}, status=400)

def update_todo(request, pk):
	todo = get_object_or_404(ToDo, pk=pk)
	if request.method == 'POST':
		form = ToDoForm(request.POST, instance=todo)
		if form.is_valid():
			todo = form.save()
			if request.headers.get('x-requested-with') == 'XMLHttpRequest':
				return JsonResponse({'id': todo.id, 'description': todo.description, 'is_complete': todo.is_complete})
			return redirect('todo_list')
	return JsonResponse({'error': 'Invalid request'}, status=400)

def delete_todo(request, pk):
	todo = get_object_or_404(ToDo, pk=pk)
	if request.method == 'POST':
		todo.delete()
		if request.headers.get('x-requested-with') == 'XMLHttpRequest':
			return JsonResponse({'success': True})
		return redirect('todo_list')
	return JsonResponse({'error': 'Invalid request'}, status=400)
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ToDoForm
from .models import ToDo

def edit_todo(request, pk):
	todo = get_object_or_404(ToDo, pk=pk)
	if request.method == 'POST':
		form = ToDoForm(request.POST, instance=todo)
		if form.is_valid():
			form.save()
			return redirect('todo_list')
	else:
		form = ToDoForm(instance=todo)
	return render(request, 'todo/edit_todo_form.html', {'form': form, 'todo': todo})