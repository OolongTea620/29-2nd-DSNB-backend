from django.urls import path
from orders.views import OrderBookView,OrderHistoryView
urlpatterns = [
    path( '', OrderBookView.as_view()), #get이면...책 주문전 이메일 확인, post면 주문 하기
    path('/delete/<int:order_id>',OrderBookView.as_view()),
    path( '/history', OrderHistoryView.as_view()), #회원 주문 내역 보내는 페이지, 쿼리 없으면 무조건 첫페이지
    path( '/history/<int:order_id>', OrderHistoryView.as_view()) #상세 내역 페이지
]