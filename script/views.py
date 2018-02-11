from script.models import Treatment, Symptom, Disease, Consultation, Patient
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, TemplateView

from script.forms import IdentityForm, ConditionForm, DiseaseForm, TreatmentForm


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

            return redirect('script:script_condition_create')

        context = {'form':document, 'patient_medical_id':patient_medical_id}
        return render(request, self.template_, context)

class IdentityList(ListView):
    template_ = 'script/patient_list.html'
    def get(self, request):
        patient_list = Consultation.objects.all()
        return render(request, self.template_, {'patient_list':patient_list})


class ConditionCreate(CreateView):

    template_ = 'script/condition_form.html'


    def get(self, request):

        document = ConditionForm()
        context = {'form':document}
        return render(request, self.template_, context)


    def post(self, request):
        document = ConditionForm(request.POST)

        patient_medical_condition = None

        if document.is_valid():

            patient_document_authentication = document.save(commit=False)
            patient_document_authentication.user = request.user
            patient_document_authentication.save()

            patient_medical_condition = document.cleaned_data['identity']
            document = ConditionForm()

            return redirect('script:script_disease_create')

        context = {'form':document, 'patient_medical_condition':patient_medical_condition}
        return render(request, self.template_, context)



class DiseaseCreate(CreateView):

    template_ = 'script/disease_form.html'


    def get(self, request):

        document = DiseaseForm()
        context = {'form':document}
        return render(request, self.template_, context)


    def post(self, request):
        document = DiseaseForm(request.POST)

        patient_medical_disease = None

        if document.is_valid():

            patient_document_authentication = document.save(commit=False)
            patient_document_authentication.user = request.user
            patient_document_authentication.save()

            patient_medical_disease = document.cleaned_data['identity']
            document = DiseaseForm()

            return redirect('script:script_treatment_create')

        context = {'form':document, 'patient_medical_disease':patient_medical_disease}
        return render(request, self.template_, context)


class TreatmentCreate(CreateView):

    template_ = 'script/treatment_form.html'


    def get(self, request):

        document = TreatmentForm()
        context = {'form':document}
        return render(request, self.template_, context)


    def post(self, request):
        document = TreatmentForm(request.POST)

        patient_medical_treatment = None

        if document.is_valid():

            patient_document_authentication = document.save(commit=False)
            patient_document_authentication.user = request.user
            patient_document_authentication.save()

            patient_medical_treatment = document.cleaned_data['identity']
            document = DiseaseForm()

            return redirect('script:script_treatment_create')

        context = {'form':document, 'patient_medical_treatment':patient_medical_treatment}
        return render(request, self.template_, context)
