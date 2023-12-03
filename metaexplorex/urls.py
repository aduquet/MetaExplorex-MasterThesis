"""
URL configuration for metaexplorex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import *  
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chart1/', chart_data_api, name='chart-data'),  
    path('chart2/', chart_data2_api, name='chart-data2'),  
    path('chart3/', chart_data3_api, name='chart-data3'),  
    path('chart4/', chart_data4_api, name='chart-data4'),  
    path('chart5/', chart_data5_api, name='chart-data5'),  
    path('chart6/', chart_data6_api, name='chart-data6'),  
    path('chart7/', chart_data7_api, name='chart-data7'),  
    path('process_chart_data/', process_chart_data, name='process_chart_data'), 
    path('submit-form/', DashboardView.as_view(), name='submit-form'),

#     path('', HomeView.as_view(), name='homepage'),
#     path('file/', FileUploadView.as_view(), name='fileuploadpage'),
#     path('charts/', ChartsView.as_view(), name='chartspage')
]
