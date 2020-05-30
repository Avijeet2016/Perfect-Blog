from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm, ContactForm, AboutForm
from blog.models import Post 
from .models import Contact, About
from django.contrib import messages


@login_required
def profile(request):
	user = request.user 
	posts = Post.objects.filter(author=request.user)
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST or None, instance=request.user)
		p_form = ProfileUpdateForm(request.POST or None, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
	else:
		u_form = UserUpdateForm()
		p_form = ProfileUpdateForm()
	
	context = {
		'u_form': u_form,
		'p_form': p_form, 
		'user': user, 
		'posts': posts,
	}
	return render(request, 'users/profile.html', context)


def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Data have been submitted successfully')
            return redirect('blog:home')
    else:
        contact_form = ContactForm()
    context = {'contact_form': contact_form, }
    return render(request, 'users/contact.html', context)


def contact_list(request):
    contacts = Contact.objects.order_by('-created_on')
    context = {'contacts': contacts, }
    return render(request, 'admin/contact_list.html', context)


def contact_details(request, id):
    contact = Contact.objects.get(id=id)
    context = {'contact': contact, }
    return render(request, 'admin/contact_details.html', context)


def create_about(request):
	if request.user.is_authenticated:
		about_form = AboutForm()
		if request.method == 'POST':
			about_form = AboutForm(request.POST, request.FILES)
			if about_form.is_valid():
				about_form.save()
				messages.success(request, 'Data have been submitted successfully!')
				return redirect('blog:home')
		context = {'about_form': about_form, }
		return render(request, 'admin/create_about.html', context)


def show_about(request):
	a_obj = About.objects.latest('id')
	context = {'a_obj': a_obj, }
	return render(request, 'users/show_about.html', context)



