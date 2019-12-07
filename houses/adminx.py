from .models import Browse
from .models import Collection
from .models import Deal
from .models import User
from .models import Trader
from .models import Village
from .models import House
from xadmin import views
import xadmin


class BaseSetting:
    enable_themes = True  # 开启主题功能
    use_bootswatch = True

class GlobalSettings:
    """
    后台修改
    """
    site_title = '二手房交易管理系统'
    site_footer = '二手房交易管理系统'

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

 
class HouseXadmin(object):
    #list_display添加后台可显示字段
    #search_fields、list_filter添加搜索框和过滤器
    list_display = ['house_id','house_type','house_size','house_addproj','house_fixtures','house_property','house_garage','house_state','house_add_time']
    search_fields = ['house_id','house_type','house_size','house_addproj','house_fixtures','house_property','house_garage','house_state','house_add_time']
    list_filter = ['house_id','house_type','house_size','house_addproj','house_fixtures','house_property','house_garage','house_state','house_add_time']
xadmin.site.register(House,HouseXadmin)


class VillageXadmin(object):
    #list_display添加后台可显示字段
    #search_fields、list_filter添加搜索框和过滤器
    list_display = ['village_id','village_position','village_name','village_introduce']
    search_fields = ['village_id','village_position','village_name','village_introduce']
    list_filter = ['village_id','village_position','village_name','village_introduce']

xadmin.site.register(Village,VillageXadmin)

class TraderXadmin(object):
    #list_display添加后台可显示字段
    #search_fields、list_filter添加搜索框和过滤器
    list_display = ['trader_id','trader_name','trader_sex','trader_age']
    search_fields = ['trader_id','trader_name','trader_sex','trader_age']
    list_filter = ['trader_id','trader_name','trader_sex','trader_age']
    pass

xadmin.site.register(Trader,TraderXadmin)

class UserXadmin(object):
    #list_display添加后台可显示字段
    #search_fields、list_filter添加搜索框和过滤器
    list_display = ['user_id','user_name','user_sex','user_age','user_tel']
    search_fields = ['user_id','user_name','user_sex','user_age','user_tel']
    list_filter = ['user_id','user_name','user_sex','user_age','user_tel']
    pass

xadmin.site.register(User,UserXadmin)


xadmin.site.register(Deal)
xadmin.site.register(Collection)
xadmin.site.register(Browse)
