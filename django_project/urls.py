from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls")),
    path("Fin/", include("Fin.urls")),
    path("FrontSide/", include("Frontside.urls")),
    path("GoalsAndSprints/", include("GoalsAndSprints.urls")),
    path("Reviews/", include("Reviews.urls")),
    path("TeamMeeting/", include("TeamMeeting.urls"))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
