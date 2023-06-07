from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('arts', views.ArtViewSet)
router.register('halls', views.HallViewSet)
router.register('exhibits', views.ExhibitViewSet)
router.register('tours', views.TourViewSet)
router.register('employees', views.EmployeeViewSet)
router.register('employee-positions', views.EmployeePositionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth', include('rest_framework.urls')),
    path('employees/me', views.EmployeeSelfView.as_view()),
    path('cat-fact', views.CatFactView.as_view()),
    path('joke', views.JokeView.as_view())
    # path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
