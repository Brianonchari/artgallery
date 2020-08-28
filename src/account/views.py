from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import AccountAuthenticationForm, AccountUpdateForm,RegistrationForm, CreateProfileForm
from account.models import Account

# Create your views here.
def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():

				form.save()
				email = form.cleaned_data.get('email')
				raw_password = form.cleaned_data.get('password1')
				account = authenticate(email = email, password = raw_password)
				login(request, account)

				return redirect('home')

		else:

				context['registration_form'] = form
	else: #GET request

			form = RegistrationForm()
			context['registration_form'] = form
	return render(request, 'account/register.html', context)

  
def logout_view(request):
	logout(request)
	return redirect('/')


def login_view(request):
	context = {}
	user = request.user
	if user.is_authenticated: 
		return redirect("home")
	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("home")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	# print(form)
	return render(request, "account/login.html", context)



def account_view(request):
	context = {}
	if not request.user.is_authenticated:
			return redirect("login")

	else:
			account = Account.objects.all()
			context['account'] = account

	
	# if request.POST:
	# 	form = AccountUpdateForm(request.POST, instance=request.user)
	# 	if form.is_valid():
	# 		form.initial = {
	# 				"email": request.POST['email'],
	# 				"username": request.POST['username'],
	# 		}
	# 		form.save()
	# 		context['success_message'] = "Updated"
	# else:
	# 	form = AccountUpdateForm(

	# 		initial={
	# 				"email": request.user.email, 
	# 				"username": request.user.username,
	# 			}
	# 		)

	# context['accounts'] = form

	# blog_posts = BlogPost.objects.filter(author=request.user)
	# context['blog_posts'] = blog_posts

	return render(request, "account/account.html", context)

	def must_authenticate_view(request):
		return render(request,'account/must_authenticate.html',{})

# fields = ['full_name', 'profile_image', 'artist_category', 'bio', ]
def create_profile_view(request):

	context = {}
	form = CreateProfileForm(request.POST or None, request.FILES or None)
	if form.is_valid():

			form.save()
			full_name = form.cleaned_data.get('full_name')
			profile_image = form.cleaned_data.get('profile_image')
			category = form.cleaned_data.get('artist_category')
			bio = form.cleaned_data.get('bio')

		# form.save()
		# full_name = form.cleaned_data['full_name']
		# profile_img = form.cleaned_data['profile_image']
		# category = form.cleaned_data['artist_category']
		# bio = form.cleaned_data['bio']
		# p = Profile(full_name=name,profile_image= profile_img, artist_category = category, bio = bio)
		# p.save()


		# form.save()

			context['form'] = form

	return render(request, "account/edit_accountls.html", context)

