from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.views import APIView
# Create your views here.

@csrf_exempt
class IndexView(APIView):
    def post(self,request):
        session_id = request.data.get('sessionId')
        service_code = request.data.get('serviceCode')
        phone_number = request.data.get('phoneNumber')
        text = request.data.get('text')

        response = ""

        if text == "":
            response = "Welcome Kindly Enter Your Name: \n"
            # response .= "1. My Account \n"
            response += "1. My Phone Number"

        elif text == "1":
            response = "END My Phone number is {0}".format(phone_number)

        return HttpResponse(response)
 