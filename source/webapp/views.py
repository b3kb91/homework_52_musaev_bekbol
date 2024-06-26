from django.shortcuts import render
from django.http import HttpResponseRedirect

from webapp.models import ToDo, status_choices


def index(request):
    todos = ToDo.objects.order_by('-date_completion')
    return render(request, 'index.html', context={"todos": todos})


def create_todo(request):
    if request.method == "GET":
        return render(request, "create_todo.html", {"status_choices": status_choices})
    else:
        date_completion = request.POST.get("date_completion")
        if date_completion == '':
            date_completion = None
        description_detail = request.POST.get("description_detail")
        if description_detail == '':
            description_detail = None

        ToDo.objects.create(
            description_detail=description_detail,
            description=request.POST.get("description"),
            status=request.POST.get("status"),
            date_completion=date_completion
        )
        return HttpResponseRedirect("/")


def todo_delete(request):
    try:
        todo = ToDo.objects.get(id=request.GET.get("id"))
        todo.delete()
        return HttpResponseRedirect("/todo/")
    except ToDo.DoesNotExist:
        return HttpResponseRedirect("/")


def todo_detail(request):
    try:
        todo = ToDo.objects.get(id=request.GET.get("id"))
    except ToDo.DoesNotExist:
        return HttpResponseRedirect("/")
    return render(request, "todo_detail.html", context={"todo": todo})
