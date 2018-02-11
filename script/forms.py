from django import forms
from script.models import Treatment, Symptom, Disease, Consultation, Patient


class IdentityForm(forms.ModelForm):

    NIS = forms.CharField(

        widget = forms.TextInput(

                attrs = {

                        'placeholder': 'Enter NIS',
                                'class' : 'form-control'
                }
        )
    )


    first_name = forms.CharField(
            widget = forms.TextInput(

                    attrs = {

                            'placeholder': 'Enter First Name',
                            'class' : 'form-control'
                    }
            )
    )



    last_name = forms.CharField(
            widget = forms.TextInput(

                    attrs = {

                              'placeholder': 'Enter Last Name',
                             'class' : 'form-control'
                    }
            )
    )

    contact = forms.CharField(
        widget = forms.TextInput(

                attrs = {

                        'placeholder':'Enter Contact',
                                'class':'form-control'
                }
        )
    )

    born = forms.DateField(

            widget = forms.TextInput(
                    attrs = {

                        'placeholder' : 'Enter Birth',
                            'class':'form-control'

                    }
            )
    )

    location = forms.CharField(
        widget = forms.TextInput(

                attrs = {

                        'placeholder':'Enter location',
                                'class':'form-control'
                }
        )
    )

    email_address = forms.CharField(
        widget = forms.TextInput(

                attrs = {

                        'placeholder':'Enter email address',
                                'class':'form-control'
                }
        )
    )

    class Meta:

        model = Patient

        fields = ['NIS', 'first_name', 'last_name', 'born', 'location', 'contact', 'email_address', 'gender']


class ConditionForm(forms.ModelForm):

    identity = forms.CharField(

        widget = forms.TextInput(

                attrs = {

                        'placeholder': 'Enter name of symptom',
                                'class' : 'form-control'
                }
        )
    )

    description = forms.CharField(

        widget = forms.Textarea(

                attrs = {

                        'placeholder': 'Describe symptoms',
                                'class' : 'form-control'
                }
        )
    )


    class Meta:

        model  = Symptom

        fields = ['identity','description']


class DiseaseForm(forms.ModelForm):

    identity = forms.CharField(

        widget = forms.TextInput(

                attrs = {

                        'placeholder': 'Enter name of disease',
                                'class' : 'form-control'
                }
        )
    )

    description = forms.CharField(

        widget = forms.Textarea(

                attrs = {

                        'placeholder': 'Describe disease',
                                'class' : 'form-control'
                }
        )
    )


    class Meta:

        model  = Disease

        fields = ['identity','description']


class TreatmentForm(forms.ModelForm):

    identity = forms.CharField(

        widget = forms.TextInput(

                attrs = {

                        'placeholder': 'Enter name of treatment',
                                'class' : 'form-control'
                }
        )
    )

    description = forms.CharField(

        widget = forms.Textarea(

                attrs = {

                        'placeholder': 'Describe treatment',
                                'class' : 'form-control'
                }
        )
    )


    class Meta:

        model  = Treatment

        fields = ['identity','description']
