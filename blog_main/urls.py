
from django.contrib import admin
from django.urls import path,include
from blog_main import views
from django.conf.urls.static import static
from django.conf import settings
from blogs import views as Blogviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('category/',include('blogs.urls')),
    path('<slug:slug>/',Blogviews.blogs,name='blogs'),
    path('blog/search/',Blogviews.search,name='search'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
