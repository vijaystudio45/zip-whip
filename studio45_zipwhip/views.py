from django.shortcuts import render
from django.http import HttpResponse
import requests


def sending_zipwhip_messages(request):
   url = "https://api.zipwhip.com/message/send"
   payload={'session':'Enter Your Session Key Here','contacts':'Enter Your Contact Id Here','body':'Enter Your text Here'}
   headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
   }
   response = requests.request("POST", url, headers=headers, data=payload)
   if response == 200:
      return HttpResponse('Task delivered')
   else:
      return HttpResponse('Unable To authenticated Zip Api')
# Create your views here.
