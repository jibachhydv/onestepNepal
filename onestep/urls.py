from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),

    # users url
    path('', include('users.urls')),

    # note urls
    path('note/', include('note.urls')),

    # Discussion
    path('ask/', include('discussion.urls')),

    # Extra App
    path('onestep/', include('extrapp.urls')),


    # Django Summer Not
    path('summernote/', include('django_summernote.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


