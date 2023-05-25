# SSAFY-Final-PJT - 싸피 관통프로젝트

>  개발환경
>
> >Python 3.9.
> >
> > Django 3.2.
> > 
> > Node.js 18.
> >
> > Vue 2

# 0. 팀원

| 팀원| 역할 | 맡은 분야|
|:---|:---|:---|
|최영태|팀장| 백엔드 위주의 작업 및 프론트 보조|
|김수찬|팀원| 프론트 위주의 작업 및 백엔드 보조|

## 0.1 상세 업무 분담 내역
---
<br>

**공통**: 
- 데이터베이스 모델링 
- 컴포넌트 구조 분석
- 시스템 목업

**최영태**: 
| 개발 분야| 역할 |
|:---:|:---|
|BE| - Django 서버 구현<br> - 영화 리뷰에 대한 데이터 베이스 관리<br> - 사용자의 캐시데이터 기반의 영화 추천 알고리즘 제작 <br> - 코사인유사도를 활용한 영화 추천 알고리즘 제작|
|FE| - 사용자와 관련된 CRUD 서비스 구현<br> - 덧글 페이지 및 덧글창 구현|

**김수찬**:
| 개발 분야| 역할 |
|:---:|:---|
|BE| - 영화 정보에 대한 데이터 관리<br> - 코사인유사도를 활용한 영화 추천 알고리즘 제작|
|FE| - Vue 클라이언트 구현 <br> - 로그인 페이지 디자인<br> - 메인페이지 디자인 <br> - 세부 팝업 디자인|

<br>

# 1. 사용 아키텍쳐 
## 1.1 `Back-End` : Django
---
## ERD 구조
![이미지를 넣어주세요]()
### **pre - install : Back-End** 
```
$ cd final-pjt/final-pjt-back
$ python –m venv venv
$ source venv/Scripts/activate
$ python install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate

$ python manage.py loaddata genre_data.json movie_data.json

$ python manage.py runserver
```

## 1.2 `Front-End` : Vue
---
## 컴포넌트 구조
![이미지를 넣어주세요]()

### **pre - install : Front-End** 
```
$ cd final-pjt/final-pjt-front
$ npm install 
$ npm run serve
```

<br>

## 1.3 폴더 구조
---
```
+---back-server
|   +---accounts
|   |   \---migrations
|   +---community
|   |   \---migrations
|   +---final
|   \---movies
|       +---fixtures
|       \---migrations
\---front-server
    +---public
    \---src
        +---api
        |   +---article
        |   +---user
        |   \---movie
        +---assets
        +---layout
        |   \---components
        +---router
        +---store
        |   \---modules
        +---views
        +---components
        |   +---community
        |   +---mainpage
        |   +---modal
        |   \---movie
        \---img
```

# 2. 개요

## 2.1 목표 서비스
```
    1. 영화 데이터 제공 
    2. 원하는 영화 저장 및 사용자 기반의 영화 추천
    3. 영화 추천 알고리즘 기반의 커뮤니티 서비스 
```
## 2.2 상세 네용
> 0. 시작페이지
```
1. 동적 화면 생성
2. Django Rest-Auth를 활용한 회원가입 / 로그인
3. 로그인 정보에 따른 Navbar 표시 변경
```

> 1. 메인페이지
```
1. 인기 영화에 대한 티저 영상 제공
2. 인기영화 제공
3. 개봉예정작 소개
4. 찜한 목록으로 접근
5. 영화 제공에 대한 시각적인 부분 개선
```

> 2. 영화 추천 서비스
```
1. 유저의 찜 목록을 기반으로 한 영화 추천
2. 영화 장르를 기반으로 한 영화 추천
3. 추천 된 영화목록 중 하나를 랜덤 추출 후 영상 제공
```

> 3. 영화 조회 서비스
```
1. 영화 제목을 기반으로 한 영화 조회
2. 영화 장르를 기반으로 한 영화 조회
3. 개봉 연도를 기반으로 한 영화 조회
4. 검색어에 대한 영화의 유사도를 기반으로 한 영화 조회
5. 검색한 영화와의 유사도를 기반으로한 영화 조회
6. 찜한 목록에 대한 영화 목록을 기반으로한 영화 추천
```

> 4. 커뮤니티 서비스
```
1. 영화 리뷰 및 별점 생성
2. 영화별 리뷰에 대한 접근성을 높임
3. 영화 좋아요를 기반으로 한 영화 추천  
4. 게시글을 통해 타 유저의 프로필 확인
5. 리뷰활동을 통해 평점 및 댓글 생성을 통한 의사소통 구현
```

> 5. 개인 프로필 페이지
```
1. 개인간 팔로우 팔로잉 기능
2. 사용자가 찜한 영화 목록 조회
3. 사용자가 생성한 게시글 조회
4. 비밀번호 수정 및 회원탈퇴 기능
```