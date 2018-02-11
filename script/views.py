from script.models import Treatment, Symptom, Disease, Consultation, Patient
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, TemplateView

from script.forms import IdentityForm


class IdentityCreate(CreateView):

    template_ = 'script/patient_form.html'


    def get(self, request):

        document = IdentityForm()
        patient = Patient.objects.filter(user = request.user)
        context = {'form':document, 'patient':patient}

        return render(request, self.template_, context)

    def post(self, request):
        document = IdentityForm(request.POST)

        patient_medical_id = None

        if document.is_valid():

            patient_document_authentication = document.save(commit=False)
            patient_document_authentication.user = request.user
            patient_document_authentication.save()

            patient_medical_id = document.cleaned_data['NIS']
            document = IdentityForm()

            return redirect('script:script_patient_list')

        context = {'form':document, 'patient_medical_id':patient_medical_id}
        return render(request, self.template_, context)



class IdentityList(ListView):
    template_ = 'script/patient_list.html'
    def get(self, request):
        patient_list = Consultation.objects.all()
        return render(request, self.template_, {'patient_list':patient_list})
