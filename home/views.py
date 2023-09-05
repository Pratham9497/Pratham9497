from django.shortcuts import render, get_object_or_404
from home.models import Task

# Create your views here.
def home(request):
    params = {'success': False, 'name': 'Pratham'}
    if request.method=="POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        print(title, desc)
        obj = Task(title = title, desc = desc)
        obj.save()
        params['success'] = True

    return render(request, 'index.html', params)

def task(request):
    params = {
        'tasks': Task.objects.all()
    }
    return render(request, 'task.html', params)

def ptask(request, taskno):
    params = {'name':'Pratham'}
    if request.method=="POST":
        obj = Task.objects.get(id=taskno)
        if 'delete' in request.POST:
            task = get_object_or_404(Task, pk=taskno)
            obj.delete()
            params = {
                'tasks': Task.objects.all()
            }
            params['task'] = task
            params['delete'] = True
            return render(request, 'task.html', params)
        
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        print(title, desc)
        obj.title = title
        obj.desc = desc
        obj.save()
        params['success'] = True
    
    params['task'] = get_object_or_404(Task, pk=taskno)
    return render(request, 'ptask.html', params)
