# django_social_login_allauth/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json

@login_required
def profile(request):
    print(f"email: {request.user}@gmail.com")
    user_info = {
        'username': request.user.first_name + request.user.last_name,
        'email': request.user.email,
    }
    user_info_json = json.dumps(user_info, indent=4, ensure_ascii=False)
    print(user_info_json)
    return render(request, 'profile.html', {'user': request.user})
