# django_social_login_allauth/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from allauth.socialaccount.models import SocialAccount
from django.http import JsonResponse


@login_required
def google_profile(request):
    google_user_info = {
        'username': request.user.first_name + request.user.last_name,
        'email': request.user.email,
    }

    google_user_info_json = json.dumps(google_user_info, indent=4, ensure_ascii=False)
    print(google_user_info_json)

    return render(request, 'google_profile.html', {'user': request.user})


@login_required
def kakao_profile(request):
    user_info = {
        "username": request.nickname
    }

    user_info_json = json.dumps(user_info, indent=4, ensure_ascii=False)
    print(user_info_json)
    return render(request, 'kakao_profile.html', {'user': request})


from allauth.socialaccount.models import SocialAccount
import requests
@login_required
def instagram_profile(request):
    if request.user.is_authenticated:
        try:
            # 인스타그램 소셜 계정 정보 가져오기
            instagram_account = SocialAccount.objects.get(provider='instagram', user=request.user)
            # 인스타그램 액세스 토큰 가져오기
            access_token = instagram_account.socialtoken_set.first().token
            # 인스타그램 아이디 가져오기
            instagram_id = instagram_account.extra_data.get('username', None)

            # Instagram Basic Display API를 통해 사용자의 게시물 가져오기
            api_url = f'https://graph.instagram.com/me/media?fields=id,caption,media_url,permalink&access_token={access_token}'
            response = requests.get(api_url)
            
            if response.status_code == 200:
                # API 응답을 JSON으로 파싱하여 사용자 정보와 게시물 정보 추출
                data = response.json().get('data', [])
                
                # 사용자의 게시물 정보를 담을 리스트
                posts = []
                
                # 각 게시물에 대해 필요한 정보 추출
                for post in data:
                    post_info = {
                        'id': post.get('id', ''),
                        'caption': post.get('caption', ''),
                        'media_url': post.get('media_url', ''),
                        'permalink': post.get('permalink', '')
                    }
                    posts.append(post_info)
                
                # 사용자 정보와 게시물 정보를 딕셔너리로 저장
                user_info = {
                    'username': instagram_id,
                    'posts': posts
                }
                
                # 템플릿에 사용자 정보와 게시물 정보 전달하여 렌더링
                return render(request, 'instagram_profile.html', {'user': user_info})
            else:
                return render(request, 'instagram_profile.html', {'error': 'Instagram API 요청에 실패했습니다.'})
        
        except SocialAccount.DoesNotExist:
            return render(request, 'instagram_profile.html', {'error': '인스타그램 계정이 연결되어 있지 않습니다.'})
    
    else:
        return render(request, 'instagram_profile.html', {'error': '사용자가 인증되지 않았습니다.'})