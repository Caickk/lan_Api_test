import requests
from django.http import JsonResponse

def consumir_view(request):
    try:
        resposta = requests.get('http://servidor2:8000/api/dados/')
        return JsonResponse(resposta.json())
    except Exception as e:
        return JsonResponse({'erro': str(e)})
