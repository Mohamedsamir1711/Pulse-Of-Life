from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include
from rest_framework import routers
from .views import RecordViewSet
from .views import result_list, result_detail
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.urls import path
from show_reports.views import OpenApiView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# schema_view = get_schema_view(title='My API')
# docs_view = include_docs_urls(title='My API Documentation')



router = routers.DefaultRouter()
router.register(r'results', RecordViewSet)

urlpatterns = [
    path('api/open/', OpenApiView.as_view()),
    path('',views.show_reports,name='show_reports'),
    path('results/', result_list, name='result_list'),
    path('results/<int:pk>/', result_detail, name='result_detail'),
    path('api/', include(router.urls)),
    # path('schema/', schema_view, name='api-schema'),
    # path('docs/', docs_view, name='api-docs'),
     path(
        'api/results/',
        RecordViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='result-list'
    ),
    path(
        'api/results/<int:pk>/',
        RecordViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='result-detail'
    ),
      path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
