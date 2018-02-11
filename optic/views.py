from django.shortcuts import render, reverse, redirect
from optic.forms import Create_user, Update_user
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

def root(request):
    return render(request, 'optic/root.html')

def register_view(request):

	if request.method == 'POST':

		form = Create_user(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/optic')

		else:
			return redirect(reverse('optic:logout'))

	else:
		form = Create_user()
		var = {'form' : form}
		return render(request, 'optic/register.html', var)

def user_profile(request):

	var = {'user': request.user}

	return render(request, 'optic/profile.html', var)


def edit_profile(request):

	if request.method == 'POST':

		form = Update_user(request.POST, instance = request.user)


		if form.is_valid():
			form.save()

			return redirect(reverse('optic:user_profile'))

		else:
			return redirect('optic/profile/edit')


	else:

		form = Update_user(instance = request.user)

		var = {'form' : form }

		return render(request, 'optic/edit_profile.html', var)

def edit_password(request):

	if request.method == 'POST':

		form = PasswordChangeForm(data = request.POST, user = request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect(reverse('optic:login'))

		else:

			return redirect('/optic/edit-password')
	else:

		form = PasswordChangeForm(user = request.user)

		var = {'form': form}

		# Create change_password instance a place in the the template context
		return render(request, 'optic/edit_password.html', var)
