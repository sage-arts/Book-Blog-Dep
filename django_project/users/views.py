from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import DetailView
from .models import Profile

def register(request):
     if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
          form.save()
          username = form.cleaned_data.get('username')
          messages.success(request, f'Account created for {username}. You can now login!')
          return redirect('login')
     else:
         form = UserRegisterForm()
     context = {
         'form': form, 
         'title': 'register'
     }
     return render(request, 'users/register.html', context)

class ProfileDetailView(DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'profile detail'
        return context

@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated')
            return redirect('profile_detail', pk=request.user.profile.id)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form, 
        'title': 'profile'
    }
    return render(request, 'users/profile_update.html', context)