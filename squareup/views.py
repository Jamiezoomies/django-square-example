from django.http import JsonResponse
from square.client import Client
import secrets 
import json

def index(request):
    return render(request, 'squareup/index.html')

def payment(request):

    client = Client(
        access_token='SANDBOX_ACCESS_TOKEN',
        environment='sandbox',
    )
    request_body = json.loads(request.body)

    payments_api = client.payments
    idempotency_key = secrets.token_hex(22)

    body = {}
    body['source_id'] = request_body['nonce']
    body['idempotency_key'] = idempotency_key
    body['amount_money'] = {}
    body['amount_money']['amount'] = 100
    body['amount_money']['currency'] = 'USD'
    
    result = payments_api.create_payment(body)
    error = {}
    if result.is_success():
        return JsonResponse(result.body)
    elif result.is_error():
        return JsonResponse(result.body)
    
    

