# Permanently delete a todo
def permanent_delete_todo(request, pk):
	todo = get_object_or_404(ToDo, pk=pk)
	if request.method == 'POST':
		todo.delete()
		return redirect('deleted_todos')
	return JsonResponse({'error': 'Invalid request'}, status=400)
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import ToDo
from .forms import ToDoForm

def todo_list(request):
	sort = request.GET.get('sort', 'created_at')
	direction = request.GET.get('direction', 'desc')
	search = request.GET.get('search', '').strip()
	valid_sorts = {
		'name': 'name',
		'deadline': 'deadline',
		'created_at': 'created_at',
	}
	sort_field = valid_sorts.get(sort, 'created_at')
	order_prefix = '-' if direction == 'desc' else ''
	todos_qs = ToDo.objects.filter(deleted_at__isnull=True)
	if search:
		from django.db.models import Q
		todos_qs = todos_qs.filter(Q(name__icontains=search) | Q(description__icontains=search))
	todos = todos_qs.order_by(f'{order_prefix}{sort_field}')
	# If redirected after POST, show empty form. If POST with errors, show form with errors.
	if request.method == 'POST':
		form = ToDoForm(request.POST)
	else:
		form = ToDoForm()
	return render(request, 'todo/todo_list.html', {
		'todos': todos,
		'form': form,
		'sort': sort,
		'direction': direction,
		'search': search,
	})

def add_todo(request):
	if request.method == 'POST':
		form = ToDoForm(request.POST)
		if form.is_valid():
			todo = form.save()
			if request.headers.get('x-requested-with') == 'XMLHttpRequest':
				return JsonResponse({'id': todo.id, 'description': todo.description, 'is_complete': todo.is_complete, 'created_at': todo.created_at.strftime('%Y-%m-%d %H:%M')})
			# Always redirect to the main list without filters so the new entry is visible
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
		from django.utils import timezone
		todo.deleted_at = timezone.now()
		todo.save()
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

# View to show deleted todos (delete history)
def deleted_todos(request):
	deleted = ToDo.objects.filter(deleted_at__isnull=False).order_by('-deleted_at')

	return render(request, 'todo/deleted_todo_list.html', {'deleted_todos': deleted})

# Restore deleted todo
def restore_todo(request, pk):
	todo = get_object_or_404(ToDo, pk=pk)
	if request.method == 'POST':
		todo.deleted_at = None
		todo.save()
		return redirect('deleted_todos')
	return JsonResponse({'error': 'Invalid request'}, status=400)