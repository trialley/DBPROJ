from django.urls import path
from . import views

app_name = 'houses'   # 指定命名空间

urlpatterns = [
    path('', views.Houselist.as_view(), name='report_list'),
    path('<pk>/', views.HouseDetail.as_view(), name='report_list_detail'),
]
