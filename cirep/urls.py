from django.urls import include, path
from rest_framework import routers

import report.views
from django.contrib import admin

import user.views

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('accounts/', include('user.urls')),
    path('reports/', include('report.urls')),
]