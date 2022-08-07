from django.contrib import admin
from django.urls import path, include
from blog_app.views import list_article

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', list_article, name='list_article'),
    path('blog/', include('blog_app.urls'))
]
