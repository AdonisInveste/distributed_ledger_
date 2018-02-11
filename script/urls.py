from django.conf.urls import url
from script.views import IdentityList, IdentityCreate, ConditionCreate, DiseaseCreate, TreatmentCreate


urlpatterns = [
   url(r'^patient/$', IdentityList.as_view(), name="script_patient_list"),
   url(r'^patient/create/$', IdentityCreate.as_view(), name="script_patient_create"),
   url(r'^patient/condition/create/$', ConditionCreate.as_view(), name="script_condition_create"),
   url(r'^patient/condition/disease/create/$', DiseaseCreate.as_view(), name="script_disease_create"),
   url(r'^patient/condition/disease/treatment/create/$', TreatmentCreate.as_view(), name="script_treatment_create"),
]
