from django.urls import path,include
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)

urlpatterns = [
    path('employee',views.EmployeeList.as_view()),
    path('forms',views.get_name,name='employee_template'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

