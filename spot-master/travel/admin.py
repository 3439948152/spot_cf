from django.contrib import admin

# Register your models here.
from .models import SpotInfo,CommentTag

class SPOTadimin(admin.ModelAdmin):
    list_display = ['poiId','poiName','price','coordinate','shortFeatures','sightLevelStr',
                    'tagNameList','distanceStr','commentCount','commentScore','heatScore']
class tagsadmin(admin.ModelAdmin):
    list_display = ['id','tags']

admin.site.register(SpotInfo,SPOTadimin)
admin.site.register(CommentTag,tagsadmin)
admin.site.site_header='后台管理系统'
admin.site.site_title='SPOT'
