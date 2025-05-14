import requests
from django.http import JsonResponse

def consumir_view(request):
    try:
        resposta = requests.get('http://servidor2:8000/api/dados/')
        return JsonResponse(resposta.json())
    except Exception as e:
        return JsonResponse({'erro': str(e)})

def ping_servidor2(request):
    #configurar host alvo
    #considerando pc na maquina de ip 6
    r = requests.get('http://172.16.103.6:8000/api/dados/')
    return JsonResponse(r.json())