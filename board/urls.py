from django.urls import path
from .views import test, test1, ItemLV, itemLV, ItemDV, ItemCV,ItemDeleteView

app_name = 'spring'

urlpatterns = [ 
    path('',ItemLV.as_view(), name='index'),
    path('detail/<int:pk>/',ItemDV.as_view(), name='detail'),
    # {% url 'spring:detail' object.id %}
    path('create/',ItemCV.as_view(), name='create'),
    path('delete/<int:pk>/',ItemDeleteView.as_view(), name='delete'),


    path('f/', itemLV),
    path('lion/<int:pk>/',test1 ),
    path('lion/tiger/',test ),
]