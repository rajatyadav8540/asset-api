from django.urls import path
from .views import AssetView, RunChecksView

urlpatterns = [
    path('assets/', AssetView.as_view(), name='assets'),
    path('run-checks/', RunChecksView.as_view(), name='run-checks'),
]
