
![](https://velog.velcdn.com/images/yoiseau_/post/7e037c87-a017-4aa5-85fe-cba87d898c67/image.png)


# MOMENTO 
**MOMENTO**는 나만의 여행일정을 공유하고 여행상품을 예약&구매 할 수 있는 플랫폼으로
앱 트리플을 클론코딩한 Django 프로젝트입니다.

<br>

## 주요 기능
** 1.로그인&회원가입 **
- Google 소셜 로그인을 지원합니다.

** 2.나만의 여행 일정 생성 **
- 도시, 여행기간, 여행스타일을 선택하여 일정을 작성할 수 있습니다.
- **MOMENTO**에서 예약한 항공권, 숙소를 일정에 불러올 수 있습니다.
- 여행기간을 날짜별로 볼 수 있고 날짜별로 장소를 추가하고 메모를 작성할 수 있습니다.
- 날짜별로 등록한 장소는 PIN을 사용해 이동경로를 확인할 수 있습니다.
- 일정에 등록한 장소 또는 투어/티켓에 대한 리뷰를 작성할 수 있습니다.
- 작성한 일정은 다른사람과 공유할 수 있습니다.
- 작성한 일정을 여행기 게시글로 작성할 수 있습니다.

** 3.여행기 작성 **
- **여행기**는 다른 사람들과 여행지에 대해 공유할 수 있는 커뮤니티 형식의 게시판 입니다.
- 작성한 여행일정을 통해 여행기를 작성할 수 있습니다.
- 여행기 게시글에는 자신이 작성한 여행일정과 여행지에 대한 상세한 내용을 다른사람들과 공유할 수 있습니다.
- 여행기 게시글에는 좋아요와 댓글을 사용할 수 있습니다.

** 4.가고싶은 장소 저장 **
- 여행 시 가고싶은 장소 또는 투어/티켓을 미리 저장했다가 추후 찾아볼 수 있는 즐겨찾기 기능입니다.

** 5.마이페이지(내 여행&내 저장&내 리뷰&내 예행기&내 예약) **
- 프로필 이미지와 닉네임을 수정할 수 있습니다.
- **내 여행**에서 지난 여행일정과 다가올 여행일정을 표시합니다.
- **내 저장**에서 여행 시, 저장해뒀던 장소 또는 투어/티켓들을 확인 수 있습니다.
- **내 리뷰**에서 여행일정에 등록된 장소 또는 투어/티켓에 대한 리뷰를 작성하거나 작성한 리뷰를 확인할 수 있습니다.
- **내 여행기**에서 여행일정에 대한 여행기를 작성하거나 작성한 여행기를 확인할 수 있습니다.
- **내 예약**에서 MOMENTO에서 예약한 항공&숙소&투어/티켓 예약내역을 확인할 수 있습니다.

** 6.항공권 **
- 항공API를 통해 항공권 예약을 할 수 있습니다.

** 7.숙소 **
- 숙소 상품을 예약할 수 있습니다.
- 숙소 상품을 도시&기간&인원으로 검색할 수 있습니다.
- 숙소 상품을 국내 도시별로 필터링하여 볼 수 있습니다.
- 숙소 상품 숙소유형으로 필터링하여 볼 수 있습니다.
- 국내 여행지를 추천하는 기능을 제공합니다.
- 추천 여행지에 맞는 숙소를 검색할 수 있습니다.

** 8.투어/티켓 **
- 투어/티켓 상품을 예약할 수 있습니다.
- 투어/티켓 상품을 도시&상품명으로 검색할 수 있습니다.
- 투어/티켓 상품을 국내 도시별로 필터링하여 볼 수 있습니다.
- 투어/티켓 상품을 카테고리별로 필터링하여 볼 수 있습니다.

** 9.AI 일정 추천 **
- 도시&여행기간&동행자&여행스타일을 선택하면 AI가 여행일정을 추천해주는 기능입니다.
- 추천받은 일정을 내 여행에 저장할 수 있습니다.

** 10.배낭톡 **
- 도시별 여행자 커뮤니티 게시판 입니다.
- 여행기간 최신순으로 게시글을 확인할 수 있습니다.
- 주제에 따른 게시글을 필터링할 수 있습니다.
- 배낭톡은 회원만 작성 가능합니다.
- 배낭톡에 대한 이용규칙 게시글을 제공합니다.
- 배낭톡에 대한 문의를 작성할 수 있습니다.

** 11.Chatbot **
- 여행지에 대한 정보를 제공하는 챗봇 입니다.
- 챗봇은 ChatGPT API의 RAG 방식으로 정보를 제공합니다.
- 여행기에 관련된 정보를 DB에 저장하여 ChatGPT와 연결하였습니다.
- DB에서 찾을 수 없는 질문인 경우, 업데이트가 되지 않았다고 안내됩니다.

** 12.공지사항&고객센터 **
- **MOMENTO**를 사용하면서 필요한 정보를 제공합니다.
- 자주 묻는 질문 게시판과 트리플 사용 설명서를 확인할 수 있습니다.
- 1대1 문의를 통해 사용자 의견을 수집합니다.

** 9.홈페이지 **
- 국내여행&여행시작 탭 구분
- 국내여행 탭
	- 항공권&숙소&투어/티켓 페이지로 이동합니다.
	- AI일정추천 기능을 사용할 수 있습니다.
    - 인기여행기 게시글을 볼 수 있습니다.
    - 통합검색 기능을 사용할 수 있습니다.
    - 여행일정을 작성할 수 있습니다.
- 여행시작 탭
	- 여행에 대한 통합검색(도시,장소,숙소,투어/티켓)을 할 수 있습니다.
    - 항공권&숙소&투어/티켓 페이지로 이동합니다.
    - 배낭톡 게시판을 볼 수 있습니다.
    - Chatbot 기능을 사용할 수 있습니다.
	- 인기여행기 게시글을 볼 수 있습니다.
	- 트리플사용설명서 게시글을 볼 수 있습니다.
- 로그인
	- 로그인할 수 있습니다.
    - Google 소셜 로그인을 통해 회원가입할 수 있습니다.

<br>

## ERD
[**ERD**](https://www.erdcloud.com/d/z8SRaoeiWuxRxhHBN) 를 보려면 클릭하세요.

<br>

## 설치 및 실행 방법
**1.저장소 클론**
```
git clone https://github.com/anjiyoo/momento.git

cd MOMENTO
```

**2.가상환경 설치**
```
python -m venv venv
```

**3.필요한 패키지 설치**
```
pip install -r requirements.txt
```

**4.데이터베이스 마이그레이션**
```
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic 
```

**5.서버실행**
```
python manage.py runserver
```

<br>

## 크레딧
이 프로젝트는 다음과 같은 오픈소스패키지를 사용합니다.
- python
- Django
- PostgreSQL
- Bootstrap5

<br>

 **GitHub** <br>
@anjiyoo  ·  @ansghltjd  ·  @nyeonseoioio  ·  @yangchanghun  ·  @HalalGuys1232