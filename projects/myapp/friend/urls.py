# 장고 기본 라이브러리
from django.urls import path

# 현재 패키지에서 views를 import
from.import views

urlpatterns = [
    # 해당하는 주소가 입력된다면,
    path('', views.index),
    path('add_friend/', views.add_friend),
    path('create_friend/', views.create_friend),
    path('show_all/', views.show_all),
    path('searchName/', views.searchName),
    # <int:id> path converter(str, int, slug, uuid, path)
    path('delete_friend/<int:id>/', views.delete_friend),
    path('update_friend/<int:id>/', views.update_friend),
]