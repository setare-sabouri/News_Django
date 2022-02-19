
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import News
from . import views
#below for media
from django.conf import settings
from django.conf.urls.static import static
from News.views import showList

app_name="project"

urlpatterns = [
    path('', showList),
    path('admin/', admin.site.urls, name="admin"),
    path('news/', include('News.urls')),
    path('accounts/',include('accounts.urls')),
    

]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)