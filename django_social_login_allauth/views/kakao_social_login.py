from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from allauth.socialaccount.models import SocialAccount
from django.http import JsonResponse

@login_required
def kakao_profile(request):
    
    user_info = {
        "username": request.nickname
    }

    user_info_json = json.dumps(user_info, indent=4, ensure_ascii=False)
    print(user_info_json)
    return render(request, 'kakao_profile.html', {'user': request})
