from django.urls import path

from.import views

urlpatterns = [
   path('', views.index),
   # 주문하기
   path('add_order/', views.add_order),
   # 주문 리스트 확인
   path('order_list/', views.order_list),
   # 주문 수정
   path('<int:id>/update_order/', views.update_order),
   # 주문 삭제
   path('<int:id>/delete_order/', views.delete_order),
]