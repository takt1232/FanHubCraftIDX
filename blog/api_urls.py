from rest_framework.routers import DefaultRouter
from .views import PostSerializerViewSet, UserSerializerViewSet, PostLikesSerializerViewSet

router = DefaultRouter()
router.register(r'posts', PostSerializerViewSet, basename='posts')
router.register(r'users', UserSerializerViewSet, basename='users')
router.register(r'postlikes', PostLikesSerializerViewSet, basename='postlikes')

urlpatterns = router.urls