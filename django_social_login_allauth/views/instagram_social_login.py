from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from allauth.socialaccount.models import SocialAccount
from django.http import JsonResponse

@login_required
def instagram_profile(request):

    # print("request.user: ", dir(request.user))
    # print(request)
    user_info = {
        "username": request.user.username,
        "is_active": request.user.is_active,
        "get_username": request.user.get_username(),
        "password": request.user.password,
    }

    user_info_json = json.dumps(user_info, indent=4, ensure_ascii=False)
    print(user_info_json)
    return render(request, 'instagram_profile.html', {'user': user_info})
