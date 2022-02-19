from django.urls import path
from . import views

app_name="News"

urlpatterns = [
    path('',views.showList,name="home"),
    path('contact/',views.contact_us, name="contact"),
    path('list/',views.showList,name="list"),
    path('create/',views.create_news, name = "create"),
    path('<slug>',views.Detail, name="Detail"), #put slug always end line of dic

]

