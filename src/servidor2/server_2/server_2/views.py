from django.http import JsonResponse

def dados_view(request):
    return JsonResponse({"mensagem": "Olá do servidor2!"})
