from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá mundo! Você está no index do seu site.")
