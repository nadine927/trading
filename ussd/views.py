from django.http.response import HttpResponse
from django.shortcuts import render
import africastalking
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .iteganya import *
# Create your views here.
def  welcome(request):
    return render(request, 'index.html')

#  python3 -m pip install africastalking
AfricasUsername='nadineuwimana72@gmail.com'
api_key ='b3d0f29af6dc51c715e0329d46fc58cf2eb1fe583aa1b1da7bc117c2b428212a'
africastalking.initialize(AfricasUsername,api_key)

@csrf_exempt
def ussdApp(request):

    if request.method == 'POST':

        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number =request.POST.get("phoneNumber")
        text = request.POST['text']
        level = text.split('*')
        category = text[:3]
        response =""
        #  main menu for our application
        if text == '':
            response =  "CON welcome to online trading \n"
            response += "1. amazina yawe \n"
            response += "2. telephone yawe \n"
            response += "3. kwiyandikisha \n"
        elif text == '1':

            response = "CON ihitamo igihingwa ushaka kugura \n"
            response += "1. shyiramo amafaranga \n"
            response += "2. kwishyura"
        elif text == '1*1':
            product="Ibishyimbo"
            response = "CON shyiramo ingano y'ibyo ushaka  y' "+str(product)+"\n"
        elif category =='1*1' and int(len(level)) == 3 and str(level[2]) in  str(level):
            response = "CON Uwo mubufatanyije \n"
        elif category =='1*1' and int(len(level)) == 4 and str(level[3]) in  str(level):
            response = "CON Shyiramo nimero y'irangamuntu yuwo mufatanyije \n"
        elif category =='1*1' and int(len(level)) == 5 and str(level[4]) in  str(level):
            # save the data into the database
            category='Ibinyomoro'
            sizeOfland=level[2]
            names= level[3]
            idnumber = level[4]
            insert = Idafarmuser(sessiondId=session_id,
            serviceCode = service_code,
            phoneNumber=phone_number,
            level=level,
            category=category,
            sizeOfland=sizeOfland,
            names=names,
            idnumber=idnumber,
            )
            insert.save()
            response = "END Murakoze kwiyandikisha kuri Ida farm \n"


        elif text == '1*2':
            product ="Indimu"
            response ="CON shyiramo ubuso bw'ubutaka bwawe bw' "+str(product)+"\n"
        elif category =='1*2' and int(len(level)) == 3 and str(level[2]) in  str(level):
            response = "CON Uwo mubufatanyije \n"
        elif category =='1*2' and int(len(level)) == 4 and str(level[3]) in  str(level):
            response = "CON Shyiramo nimero y'irangamuntu yuwo mufatanyije \n"
        elif category =='1*2' and int(len(level)) == 5 and str(level[4]) in  str(level):
            category='Indimu'
            sizeOfland=level[2]
            names= level[3]
            idnumber = level[4]
            insert = Idafarmuser(sessiondId=session_id,
            serviceCode = service_code,
            phoneNumber=phone_number,
            level=level,
            category=category,
            sizeOfland=sizeOfland,
            names=names,
            idnumber=idnumber,
            )
            insert.save()
            response = "END Murakoze kwiyandikisha kuri Ida farm \n"
         
        #  ======================== INGENGABIHE==================
        elif text == '2':
            response = "CON Hitamo igihe \n "
            response += "1. Rimwe mukwezi \n"
            response += "2. Kabiri Mukwezi \n"
            response += "3. Buri gihe"
        elif text == '2*1':
            # save the data
            insertData(
                category='Rimwe',
                sessionID=session_id,
                phoneNumber=phone_number
            )
            response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe rimwe mukwezi"
        elif text == '2*2':
            insertData(
                category='Kabiri',
                sessionID=session_id,
                phoneNumber=phone_number
            )
            response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe kabiri mukwezi"
        elif text == '2*3':
            insertData(
                category='Burigihe',
                sessionID=session_id,
                phoneNumber=phone_number
            )
            response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe Buri munsi"

        else:
            response = "END Ukanze ibitaribyo, ongera mukanya"
        return HttpResponse(response)
    else:
        return HttpResponse('we are on ussd app')
