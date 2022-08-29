from django.contrib import admin
from django.urls import path, include
from blog_app.views import list_article
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', list_article, name='list_article'),
    path('blog/', include('blog_app.urls')),
    path('users/', include('users.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
