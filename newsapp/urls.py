from django.urls import path
from . import views

urlpatterns = [
    path('news/<uuid:card_id>/', views.news_card, name='news_card'),
    path('news/<uuid:card_id>/vote/<str:action>/', views.vote, name='vote'),
]
