from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from asosiy.views import *

router = DefaultRouter()
router.register("suvlar", SuvModelViewSet)
router.register("mijozlar", MijozModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('suv/<int:son>',SuvAPI.as_view()),
    path('mijoz/<int:son>',MijozAPI.as_view()),
    path('buyurtmalar/',BuyurtmaAPI.as_view()),
    path('boshqaruvchilar/',AdminlarAPI.as_view()),
    path('boshqaruvchi/<int:son>/',AdminAPI.as_view()),
    path('haydovchilar/',HaydovchilarAPI.as_view()),
    path('haydovchi/<int:son>/',HaydovchiAPI.as_view()),

]
