from datetime import datetime

from django.forms.models import model_to_dict
from django.shortcuts import render

from .forms import UserProfileForm


def user_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = request.user.id
            obj.save()
    elif request.user and request.user.userprofile:
        form = UserProfileForm(data=model_to_dict(request.user.userprofile))
    else:
        form = UserProfileForm()

    now = datetime.now()
    return render(
        request,
        "accounts/profile.html",
        {"now": now.isoformat(), "email": request.user.email, "form": form},
    )
