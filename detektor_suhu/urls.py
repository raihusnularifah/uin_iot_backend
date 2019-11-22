from rest_framework import routers

from detektor_suhu.views import StatsViewSet

router = routers.DefaultRouter()
router.register('stats', StatsViewSet)

urlpatterns = []
urlpatterns += router.urls
