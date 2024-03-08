from datetime import datetime

from django.shortcuts import render


def user_profile(request):
    print(request.user)
    now = datetime.now()
    return render(
        request,
        "accounts/profile.html",
        {"now": now.isoformat(), "email": request.user.email},
    )
