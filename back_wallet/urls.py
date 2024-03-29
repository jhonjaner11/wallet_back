"""back_wallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from plans.api import UserAPI, planList
from rewards.api import rewardList, transactionList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create_user/', UserAPI.as_view(), name = "api_create_user"),
    path('api/plans/', planList.as_view(), name = "api_get_plans"),
    path('api/subscriptions/', planList.as_view(), name = "api_get_subscriptions"),
    path('api/rewards/', rewardList.as_view(), name = "api_get_rewards"),
    path('api/transactions/', transactionList.as_view(), name = "api_get_transactions")
]
