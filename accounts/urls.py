
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from accounts import views
urlpatterns = [
        url(r'^signup/$', views.Signup.as_view(), name="signup"),
    url(r'^login/$', obtain_jwt_token, name='login'),
    url(r'^sendSMSverification/$', views.Verification.as_view(), name='sendCode'),
    url(r'^CheckSMSverification/$', views.CheckVerificationCode.as_view(), name='sendCode'),
    url(r'^profile/$', views.Profile.as_view(), name='profile'),
]
