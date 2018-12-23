from django.http import JsonResponse
from . import models


def auth(request):
    username = "-1"
    password = ""
    if request.method == 'GET':
        username = request.GET.get("username", "-1")
        password = request.GET.get("password", "")
    elif request.method == 'POST':
        username = request.POST.get("username", "-1")
        password = request.POST.get("password", "")
    return JsonResponse({'status': models.auth(username, password)})


def add_prescription(request):
    username = "-1"
    password = ""
    user = ""
    prescription = ""
    if request.method == 'GET':
        username = request.GET.get("username", "-1")
        password = request.GET.get("password", "")
        user = request.GET.get("user", "-1")
        prescription = request.GET.get("prescription", "")
    elif request.method == 'POST':
        username = request.POST.get("username", "-1")
        password = request.POST.get("password", "")
        user = request.POST.get("user", "-1")
        prescription = request.POST.get("prescription", "")
    return JsonResponse({'status': models.add_prescription(username, password, user, prescription)})


def get_prescription(request):
    username = "-1"
    password = ""
    user = ""
    if request.method == 'GET':
        username = request.GET.get("username", "-1")
        password = request.GET.get("password", "")
        user = request.GET.get("user", "-1")
    elif request.method == 'POST':
        username = request.POST.get("username", "-1")
        password = request.POST.get("password", "")
        user = request.POST.get("user", "-1")
    return models.get_prescription(username, password, user)
