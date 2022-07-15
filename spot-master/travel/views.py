from django.shortcuts import render
from rest_framework.views import APIView

from .serial import SOPTSeriailzer,tagsSeriailzer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from .models import SpotInfo,CommentTag
from travel.CF import main
# Create your views here.
class SPOTView(APIView):
    def get(self, request):
        MM = SpotInfo.objects.all()
        Sdetial = SOPTSeriailzer(instance=MM, many=True)
        json = JSONRenderer().render(Sdetial.data)
        return HttpResponse(json, content_type='application/json')

class tagsView(APIView):
    def get(self, request):
        MM = CommentTag.objects.all()
        Sdetial = tagsSeriailzer(instance=MM, many=True)
        json = JSONRenderer().render(Sdetial.data)
        return HttpResponse(json, content_type='application/json')
class buttonView(APIView):
    def get(self,request):
        m=SpotInfo.objects.values('poiId')

        #如需添加其他类，只需要在values里添加就可
        #m=SpotInfo.objects.values('poiId',"poiName","shortFeatures")
        for i in range(len(m)):
            num=m[i]['poiId']
            m[i]['url']=f'https://m.ctrip.com/webapp/you/comment/district/4229-11.html?openapp=5&poiId={num}'
        json = JSONRenderer().render(m)
        return HttpResponse(json, content_type='application/json')

class recommand(APIView):
    def get(self,request):
        if request.method == "GET":
            json_data=[]
            df=main(poiid=88132)
            for i in range(len(df)):
                m = SpotInfo.objects.filter(poiId=df[i])
                serial = SOPTSeriailzer(instance=m, many=True)
                json_data.append(serial.data)


            json = JSONRenderer().render(json_data)
            return HttpResponse(json, content_type='application/json')


# /views
#推荐视图json
def test_view(request):
    if request.method == 'POST':
        data_from_html = request.POST.get('poiid')
        json_data = []
        df = main(poiid=int(data_from_html))
        for i in range(len(df)):
            m = SpotInfo.objects.filter(poiId=df[i])
            serial = SOPTSeriailzer(instance=m, many=True)
            json_data.append(serial.data)

        json = JSONRenderer().render(json_data)
        return HttpResponse(json, content_type='application/json')

    return render(request, "upload.html")
