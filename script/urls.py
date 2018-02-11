from django.conf.urls import url
from script.views import IdentityList, IdentityCreate


urlpatterns = [

   url(r'^patient/$', IdentityList.as_view(), name="script_patient_list"),
   url(r'^patient/create/$', IdentityCreate.as_view(), name="script_patient_create"),

]
