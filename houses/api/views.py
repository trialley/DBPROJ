from django_filters import rest_framework
from rest_framework import generics
from rest_framework import pagination
from .serializers import HouseSerializer
from ..models import House
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as rfilters
from django_filters import rest_framework as filters
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

class HouseFilter(filters.FilterSet):
    """
    房屋过滤搜索
    """
    # min_read = rest_framework.NumberFilter(field_name='read_num', lookup_expr='gte')
    # max_read = rest_framework.NumberFilter(field_name='read_num', lookup_expr='lte')
    house_property_include = filters.CharFilter(
        field_name='house_property', lookup_expr='icontains',help_text=_('包含属性'))
    size_min = filters.NumberFilter(
        field_name="house_size", lookup_expr='gte', help_text=_('最小面积'))
    size_max = filters.NumberFilter(
        field_name="house_size", lookup_expr='lte', help_text=_('最大面积'))
    time_min = filters.DateTimeFilter(
        field_name="house_add_time", lookup_expr='gte', help_text=_('最早添加时间'))
    time_max = filters.DateTimeFilter(
        field_name="house_add_time", lookup_expr='lte', help_text=_('最晚添加时间'))
    house_id = filters.NumberFilter(
        field_name="house_id", lookup_expr='exact', help_text=_('房屋id'))
    class Meta:
        model = House
        fields = ['house_id','size_min','time_min','time_max', 'size_max','house_property_include']


class HousePagination(pagination.PageNumberPagination):
    """
    房屋列表页，分页，搜索，过滤，排序,取某一个具体商品的详情
    """
    page_size = 12
    # 向后台要多少条

    page_size_query_param = 'page_size'
    # 定制多少页的参数
    page_query_param = "page"
    max_page_size = 100

class Houselist(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    pagination_class = HousePagination
    filter_class = HouseFilter#添加过滤器
    filter_backends = (DjangoFilterBackend,
                       rfilters.SearchFilter, rfilters.OrderingFilter)

class HouseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
