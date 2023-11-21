from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import FootballDatas, FootballView, LinkView
urlpatterns = [
    path('', FootballView.as_view()),
    path('api/scores', FootballDatas.as_view()),
    path('api/links', LinkView.as_view()),
    path('api/schema', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger', SpectacularSwaggerView.as_view(url_name='schema')),
]
