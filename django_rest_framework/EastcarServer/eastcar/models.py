from django.db import models

# Create your models here.
class RentalCarInfo(models.Model):

    """
    租方汽车信息
    """
    
    carid = models.CharField(max_length=20, default="", verbose_name="车牌")
    srcaddr = models.CharField(max_length=20, default="", verbose_name="出发地点")
    dstaddr = models.CharField(max_length=20, default="", verbose_name="到达地点")
    class Meta:
        verbose_name = "租方汽车信息"
        verbose_name_plural = verbose_name
        ordering = ('carid',)

    def __str__(self):
        return self.carid