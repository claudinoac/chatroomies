from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse


class SignUpView(TemplateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse("chatroom:chatroom_view", args=[1]))
        return render(request, 'registration/signup.html', {'form': form})
