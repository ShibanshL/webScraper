from django.http import HttpResponse, JsonResponse
from .models import webScrModel, sendArrayModal
from .serializers import webScrSerializer,sendArrayModalSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_201_CREATED


tikData = []


# Create your views here.
def myGetReq(response):
    return JsonResponse({'Name':'congrats this is working!!!'}, safe=False)

@api_view(['GET','POST'])
def test_List(request):
    if request.method == 'GET':
        # return JsonResponse({"GET_WORKING":True})
        localObj = webScrModel.objects.all()
        localSerializer = webScrSerializer(localObj,many=True)
        return Response(localSerializer.data)
    if request.method == 'POST':
        localObj = webScrModel.objects.all()

        serializer = webScrSerializer(data=request.data, many=True)

        if serializer.is_valid():
         
            # return JsonResponse({'DATA':request.data}, status = status.HTTP_201_CREATED)
            return Response(fetchData(request.data), status = status.HTTP_201_CREATED)

@api_view(['GET','DELETE'])
def paramsSent(request, key_id):
    
    print(request)
    # if request.method == 'GET':
    #     localObj = webScrModel.objects.filter(id=int(key_id))
    #     localSerializer = webScrSerializer(localObj,many=True)
    #     return JsonResponse(localSerializer.data, safe=False)
    if request.method == 'DELETE':
        # localObj = webScrModel.objects.filter(id=int(key_id)).delete()
        # localSerializer = webScrSerializer(localObj,many=True)
        return JsonResponse({'JJ':'FUK U'})
    

@api_view(['POST','GET'])
def getArray(request):
    if request.method == 'POST':
        # localObj_W = webScrModel.objects.all()
        # localSerializer_W = webScrSerializer(localObj_W,many=True)
        localOBJ = sendArrayModal.objects.all()
        localSerializer = sendArrayModalSerializer(data=request.data)
        print('Data',request.data)
        if localSerializer.is_valid():
            localSerializer.save()
            return Response(localSerializer.data, safe=False)
        return Response({'Name':localSerializer.errors} ,status=404)
    
    if request.method == 'GET':
        localOBJ = sendArrayModal.objects.all()
        localSerializer = sendArrayModalSerializer(localOBJ, many=True)
        return Response({'Data':localSerializer.data})
    



from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time





def fetchData(e):

    testData = []

    options = webdriver.EdgeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    # options.binary_location = "/usr/bin/google-chrome"

    service_Local = Service(executable_path='/edge/msedgedriver')

    # driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    driver = webdriver.Edge(service=service_Local, options=options)

    for sym in e:
        oktest(sym['Symbol'], driver, testData)


    driver.quit()

    return testData


def oktest(e, dr, td):

    dr.get('https://www.binance.us/price')

    time.sleep(5)

    input = dr.find_element(By.XPATH,'/html/body/div[4]/div/main/div/div/div/div[2]/div/div[1]/input')

    if input: input.send_keys(e)

    data_1 = dr.find_element(By.XPATH,'//div[@class="search-result"]')

    if data_1:
        if data_1.text.split('\n')[0] == "No results found" :
            td.append({
                'SYMBOL':e.upper()+"/ USDT",
                'NAME':"No Such Data",
                'PRICE':"No Such Data",
                'PERCENTAGE':"No Data",
                "DATA_REC":e
            })
        if data_1.text.split('\n')[0] != "No results found" :
            td.append({
                'SYMBOL':data_1.text.split('\n')[0],
                'NAME':data_1.text.split('\n')[1],
                'PRICE':data_1.text.split('\n')[2],
                'PERCENTAGE':data_1.text.split('\n')[3],
                "DATA_REC":e
            })
    



