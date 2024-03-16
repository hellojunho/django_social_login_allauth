# Django의 allauth 라이브러리를 활용한 소셜 로그인 기능 구현
[django-allauth](https://docs.allauth.org/en/latest/index.html)에 접속해서 `QuickStart`와 `Reqular Accounts/Providers/Provides Sepcitics` 를 참조하자.  

## Google

**settings.py**  
```
INSTALLED_APPS [
    ...

    # google
    'allauth.socialaccount.providers.google',

    ...
]

SOCIALACCOUNT_PROVIDERS = {
    ...

    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }

    ...
}
```

## Facebook
**settings.py**  
```
INSTALLED_APPS [
    ...

    # facebook
    'allauth.socialaccount.providers.facebook',

    ...
]

SOCIALACCOUNT_PROVIDERS = {
    ...

    'facebook': {
        'METHOD': 'oauth2',  # Set to 'js_sdk' to use the Facebook connect SDK
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'ko_KR',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v13.0',
        'GRAPH_API_URL': 'https://graph.facebook.com/v13.0',
    },

    ...
}
```

## Instagram
**settings.py**  
```
INSTALLED_APPS [
    ...

    # instagram
    'allauth.socialaccount.providers.instagram',

    ...
]
```


## Kakao
**settings.py**  
```
INSTALLED_APPS [
    ...

    # kakao
    'allauth.socialaccount.providers.kakao',

    ...
]
```


## Naver

## urls.py
```
from django.contrib import admin
from django.urls import path, include
from .views import google_profile, kakao_profile, instagram_profile


urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/google/profile/', google_profile, name="google_profile"),
    path('accounts/kakao/profile/', kakao_profile, name="kakao_profile"),
    path('accounts/instagram/profile/', instagram_profile, name='instagram_profile'),
]
```  
- 각 플랫폼 소셜 로그인 기능별로 url을 다르게 설정했습니다.  
- templates/ 위치의 html 파일에 접근해 현재 로그인되어있는 플랫폼의 정보를 확인할 수 있도록 합니다.

# 진행상황
## 2024-03-16
- `Google`, `Facebook`, `Instagram`, `Kakao` 로그인 성공  
- Google: `templates/google_profile.html`에서 사용자 이름, 이메일 확인 가능
- Facebook: 
- Instagram: `templates/instagram_profile`에서 사용자 인스타 아이디(예: @example_11) 확인 가능, 게시물 확인은 아직 미완성
- Kakao: 

# 오류해결
## 1. Redirect URI
- 플랫폼마다 다르지만, `Facebook`, `Instagram`은 `https`만 취급함 -> 로컬에서 테스트하다보니 굉장히 불편  
- ssl 인증서를 발급받고, `python manage.py runsslserver`로 진행  
- 유효한 OAuth redirect uri는 `도메인` 주소로 해야하더라..  
    - https://127.0.0.1:8000/~ 이게 아니라 `https://localhost:8000/~` 이걸로..!
    - 이걸 몰라서 일주일이 넘도록 삽질했다...


# 참고자료
## allauth관련
- [allauth 공식 홈페이지](https://docs.allauth.org/en/latest/#)  

## ssl server 관련
- [django-sslserver pypi 홈페이지](https://pypi.org/project/django-sslserver/0.12/)  
- [Django에 https 설정하기](https://dttmmit.tistory.com/120)  