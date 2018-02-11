from django import forms
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class Create_user(UserCreationForm):

	email = forms.EmailField(required = True)


	class Meta:

		model = get_user_model()

		fields = (

			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
		)

		def save(self, commit = True):
			user = super(Create_user, self).save(commit = False)
			user.first_name = self.cleaned_data['first_name']
			user.last_name = self.cleaned_data['last_name']
			user.email = self.cleaned_data['email']

			if commit:

				user.save()

			return user

class Update_user(UserChangeForm):

	class Meta:

		model = get_user_model()

		fields = (

			'email',
			'first_name',
			'last_name',
			'password',


		)
