from django.db import models
from datetime import datetime
from django.utils import timezone

class House(models.Model):
    house_id = models.AutoField(primary_key=True)  # 显示地设置了一个自增的主键类型
    house_type = models.CharField(max_length=50)
    house_size = models.DecimalField(max_digits=6, decimal_places=2)  # 可存储小数位为2，六位有效数字的类型
    house_addproj = models.CharField(max_length=50)
    house_fixtures = models.CharField(max_length=200)
    house_property = models.CharField(max_length=200)
    house_garage = models.CharField(max_length=50)
    house_state = models.CharField(max_length=50)
    house_add_time = models.DateTimeField( default=timezone.now)


    # django提供的用于管理一个数据表的对象，这里是在配置restful时加上去的
    objects = models.Manager()
    def __str__(self):
        return self.house_state


#-----------------------------------------------------#
#----------------------类的分割线----------------------#
#-----------------------------------------------------#
class Village(models.Model):
    village_id = models.AutoField(primary_key=True)
    village_position = models.DecimalField(max_digits=10, decimal_places=3)
    village_name = models.CharField(max_length=50)
    village_introduce = models.CharField(max_length=200)

    objects = models.Manager()

#-----------------------------------------------------#
#----------------------类的分割线----------------------#
#-----------------------------------------------------#
class Trader(models.Model):
    trader_id = models.AutoField(primary_key=True)
    trader_name = models.CharField(max_length=50)
    trader_sex = models.CharField(max_length=50)  # 允许自定义类型
    trader_age = models.SmallIntegerField()
    
    objects = models.Manager()

#-----------------------------------------------------#
#----------------------类的分割线----------------------#
#-----------------------------------------------------#


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_sex = models.CharField(max_length=50)
    user_age = models.SmallIntegerField()
    user_tel = models.CharField(max_length=50)


#-----------------------------------------------------#
#----------------------类的分割线----------------------#
#-----------------------------------------------------#
class Deal(models.Model):
    deal_id = models.AutoField(primary_key=True)
    house_id = models.IntegerField()
    buyer_id = models.IntegerField()
    seller_id = models.IntegerField()
    trader_id = models.IntegerField()
    deal_time = models.DateTimeField
    deal_price = models.DecimalField(max_digits=20, decimal_places=3)
    deal_fee = models.DecimalField(max_digits=10, decimal_places=3)

#-----------------------------------------------------#
#----------------------类的分割线----------------------#
#-----------------------------------------------------#


class Collection(models.Model):
    user_id = models.IntegerField()
    house_id = models.IntegerField()
    collect_time = models.DateTimeField

#-----------------------------------------------------#
#----------------------类的分割线----------------------#
#-----------------------------------------------------#


class Browse(models.Model):
    user_id = models.IntegerField()
    house_id = models.IntegerField()
    browse_time = models.DateTimeField
