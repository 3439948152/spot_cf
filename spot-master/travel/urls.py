from django.urls import path,include
from .views import SPOTView,tagsView,buttonView,recommand,test_view

urlpatterns=[
    path('spot/',SPOTView.as_view()),
    path('tags/',tagsView.as_view()),
    path('commit/',buttonView.as_view()),
    path('recommend/',recommand.as_view()),
    path('1/',test_view),
]
'''
http://127.0.0.1:8000/travel/spot  
为poi111222里的所有数据，数据格式如下
{"poiId":76447,"poiName":"都江堰景区","price":80.0,"coordinate":"103.6088460217681,31.003751525385034","priceTypeDesc":"门票",
"shortFeatures":"延续两千年的水利工程","sightLevelStr":"5A","tagNameList":"亲近大自然,游山玩水","distanceStr":"距市中心3.9km",
"commentCount":29585,"commentScore":4.7,"heatScore":8.9,
"coverImageUrl":"https://youimg1.c-ctrip.com/target/100g0z000000nd29yD334.jpg"}


http://127.0.0.1:8000/travel/tags/
为tag111222里所有数据
{"id":76447,"tags":"了解古人的智慧,世界文化遗产,了解历史文化,中国目前保存最完整的古代水利工程,一家人出游的好去处,
爱国教育的好地方,被誉为独奇千古的镇川之宝,城外最著名的莫过于都江堰和青城山,在岷江边喝喝茶享受片刻宁静,漫步在江边细细品味,游览线路的标识牌少点,"} 

http://127.0.0.1:8000/travel/commit/
携程评论链接，
[{"poiId":76447,"url":"https://m.ctrip.com/webapp/you/comment/district/4229-11.html?openapp=5&poiId=76447"}



http://127.0.0.1:8000/travel/1
显示upload.html页面，输入poiid,点击提交，得出十个景点的json数据
'''