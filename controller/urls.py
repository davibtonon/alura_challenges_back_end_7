from django.urls import path
from controller.views import DepoimentosViewSet

urlpatterns = [
    path('/depoimentos', DepoimentosViewSet)
]