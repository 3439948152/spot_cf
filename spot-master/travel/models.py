from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class SpotInfo(models.Model):
    '''景点表'''
    poiId = models.IntegerField(primary_key=True)
    poiName = models.CharField('景点名', db_column='poiName', null=False, blank=False, default='', max_length=255)
    price = models.FloatField(null=True)
    coordinate = models.CharField('坐标', db_column='coordinate', null=False, blank=False, default='', max_length=255)
    priceTypeDesc = models.CharField('是否免费', db_column='priceTypeDesc', null=True, blank=True, default='', max_length=255)
    shortFeatures = models.CharField('景点短特征', db_column='shortFeatures', null=True, blank=True, default='', max_length=255)
    sightLevelStr = models.CharField('星级', db_column='sightLevelStr', null=True, blank=True, default='', max_length=4)
    tagNameList = models.CharField('标签', db_column='tagNameList', null=True, blank=True, default='', max_length=255)
    distanceStr = models.CharField('距离市区距离', db_column='distanceStr', null=True, blank=True, default='', max_length=255)
    commentCount = models.IntegerField(null=True)
    commentScore =models.FloatField(null=True)
    heatScore = models.FloatField(null=True)
    coverImageUrl = models.CharField('图片链接', db_column='coverImageUrl', null=True, blank=False, default='', max_length=255)

    def __dir__(self):
        return self.poiName

    class Meta:
        managed = True
        db_table = 'poi111222'
        verbose_name = '景点'
        verbose_name_plural = '景点信息管理'
class CommentTag(models.Model):
    """tag"""
    id = models.IntegerField(primary_key=True)
    tags = models.TextField('标签', db_column='tags', max_length=255)

    class Meta:
        managed = True
        db_table = 'tag111222'
        verbose_name = '景点标签'
        verbose_name_plural = '标签管理'

    def __str__(self):
        return self.id


