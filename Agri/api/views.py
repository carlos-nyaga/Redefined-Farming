from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# Create your views here.


counties = ['Central', 'Eastern', 'NorthEastern', 'Western' ]
@csrf_exempt
@api_view(["GET", "POST"])
def index(request):
    if request.method == "POST":
        session_id = request.POST.get('sessionId', None)
        service_code = request.POST.get('serviceCode', None)
        phone_number = request.POST.get('phoneNumber', None)
        text = request.POST.get('text', 'default')

        response = ""

        if text == ' ':
            response = "Hello Welcome to Redefined Farming. Please Enter your name: \n"
            response += text
        
        elif text:
            response = "Hello {} \n".format(text)
            response += "Kindly Enter your County \n"

        elif text in counties :
            response = "Nice.. Now what part of {} County are you located ? \n".format(text)
            response += ""
        
        elif text in regions:
            response += "Awesome. And is your land: \n"
            response += "1. Tilled \n"
            response += "2. Untilled \n"
        
        elif text == "1":
            pass
        
        elif text == "2":
            pass
        
       
    

        return response
 