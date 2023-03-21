from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from api.views import(
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostViewSet
)

app_name = 'api'

route_v1 = DefaultRouter()

route_v1.register(r'groups', GroupViewSet)
route_v1.register(r'posts', PostViewSet)
route_v1.register(
    r'follow',
    FollowViewSet,
    basename='follow'
)
route_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/', include(route_v1.urls)),
    path(
        'v1/api-token-auth/',
        views.obtain_auth_token,
        name='api-token'
    ),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
