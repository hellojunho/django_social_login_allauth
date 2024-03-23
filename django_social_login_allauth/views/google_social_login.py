from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from allauth.socialaccount.models import SocialAccount
from django.http import JsonResponse


@login_required
def google_profile(request):

    # 사용자 요청(request) 객체의 속성 확인
    request_attributes = dir(request)
    
    # 확인한 속성을 콘솔에 출력하여 보여줍니다.
    print("=============")
    for attribute in request_attributes:
        print(attribute)

    google_user_info = {
        'username': request.user.first_name + request.user.last_name,
        'email': request.user.email,
    }

    google_user_info_json = json.dumps(google_user_info, indent=4, ensure_ascii=False)
    print(google_user_info_json)

    return render(request, 'google_profile.html', {'user': request.user})
