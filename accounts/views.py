from datetime import datetime

from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render

from .forms import UserProfileForm


def user_profile(request):
    if not request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = request.user.id
            obj.save()
    else:
        try:
            form = UserProfileForm(
                data=model_to_dict(request.user.userprofile)
            )
        except User.userprofile.RelatedObjectDoesNotExist:
            form = UserProfileForm()

    now = datetime.now()
    return render(
        request,
        "accounts/profile.html",
        {"now": now.isoformat(), "email": request.user.email, "form": form},
    )
