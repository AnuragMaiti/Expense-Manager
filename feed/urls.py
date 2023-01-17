from django.urls import path
from .views import HomePageView,ExpensesPageView,FundsPageView,ProjectionsPageView,TargetsPageView

app_name = 'feed'

urlpatterns = [
    path('',HomePageView.as_view(), name ='home_page'),
    path('expenses/',ExpensesPageView.as_view(), name ='expenses_page'),
    path('funds/',FundsPageView.as_view(), name ='funds_page'),
    path('projections/',ProjectionsPageView.as_view(), name ='projections_page'),
    path('targets/',TargetsPageView.as_view(), name ='targets_page'),
]