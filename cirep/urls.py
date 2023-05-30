from django.contrib.auth.views import LoginView
from django.urls import include, path
from rest_framework import routers

import report.views
from django.contrib import admin

import user.views
from administrator.views.dashboard import render_dashboard

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('routes/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('accounts/', include('user.urls')),
    path('reports/', include('report.urls')),
    path('administrador/', include('administrator.urls')),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('', render_dashboard)
]