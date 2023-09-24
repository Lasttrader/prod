from django.shortcuts import render
from django.http import HttpResponse 
import requests

# Create your views here.
def index(request):
    #Создаем сообщение для API нашего flask
    message = requests.post('http://localhost:5000/api/api_message/',
                            json={"X":[[10.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 8.0, 3.0, 0.0, 0.12107185807539463, 0.3740520633526504, -0.1691938897666138, -0.5768294699140059, 2.9890440835684733, -0.3204128219555523]]})
    print(message)
    #если сообщение успешно оставлено, выводим его json
    if message.ok:
        print(message.json())
    return HttpResponse(str(message.json()))