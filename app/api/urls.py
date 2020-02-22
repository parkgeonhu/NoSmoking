from django.urls import re_path, path

# from .views import MyProfile, MyOrderListView , MakeOrderView, StoreMenuView, StoreOrderListView, LoginView, LogoutView, StoreListView, UpdateOrderStatusView

from .views import RecordView

urlpatterns = [
	# # 자신의 정보 GET
	# path('users/me', MyProfile.as_view()),
	path('users/record', RecordView.as_view()),
]