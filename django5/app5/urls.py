from django.urls import path , re_path , include
from app5 import views


app_name = 'app5'

urlpatterns = [

re_path(r'^register/$',views.register,name='register'),
re_path(r'^user_login/$',views.user_login,name='user_login')

]
