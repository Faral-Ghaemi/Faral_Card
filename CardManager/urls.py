from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),

    path('start-work/', views.StartWorkView.as_view(), name='start_work'),
    path('end-work/', views.EndWorkView.as_view(), name='end_work'),
    # path('admin/', admin.site.urls),
]
