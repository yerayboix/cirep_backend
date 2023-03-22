from django.template.defaulttags import url
from django.urls import include, path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from backend import views
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns1 = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('accounts/', include('user.urls')),

]

schema_view = get_swagger_view(title='CIREP API',patterns=urlpatterns1)

internalapis = [
    path('docs/', schema_view),
]

urlpatterns = urlpatterns1 + internalapis
