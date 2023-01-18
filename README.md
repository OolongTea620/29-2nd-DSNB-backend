# DSNB-backend

### 목차

### 프로젝트 설명
![여기에로고](DSNBlogo.png)  
세계 문학 관련 서비스를 제공하는 종합 컨텐츠 플랫폼입니다.   
콘텐츠의 미리보기 서비스를 지원합니다.   
다른 유저에게 세계 문학을 선물할 수 있습니다.

### 개발 기간
2022.02.14 - 2022.02.25

### 사용 기술
`Python(3.9)`, `Django(4.5.1)`, `Mysql`, `AWS-EC2`, `AWS-RDS`

### 개발 환경
Ubuntu 22.04  
IDE : VSCode

#### 프로젝트 구조
```text
.
|-- README.md
|-- my_settings.py // 생성하여 사용      
|-- pull_request_template.md
|-- requirements.txt
|-- manage.py // 실행파일
|-- books
|   |-- admin.py   
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   |-- utils.py
|   `-- views.py
|-- core
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   `-- views.py
|-- dsnb
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
|-- orders
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   `-- views.py
|-- reviews
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   `-- views.py
`-- users
    |-- admin.py
    |-- apps.py
    |-- models.py
    |-- tests.py
    |-- urls.py
    |-- utils.py
    `-- views.py

```

### 실행 방법
#### 설치, 셋팅
1. conda 가상환경 설치 필요 : [conda설치방법](https://m.blog.naver.com/jonghong0316/221683053696)
```zsh
// conda 가상환경 실행
>>$ conda activate 

// requirements.txt에 적힌 파일 설치
>>$ conda install --file requirements.txt 
```

2. mysql 설치 필요

3. security config 설정 

root에 my_settings.py 파일 생성
```python
SECRET_KEY="", //Django project 처음 생성 시 settings.py내부에 주어짐 
DATABASES="", // 데이터 베이스 접속 url  
ALGORITHM="" // 암호화 알고리즘명 대문자로적을 것 
```

4. dependency 설정

requirements.txt에 적힌 파이썬 모듈 설치
- conda 실행 상태에서 명령어
```zsh
>>$ conda env create -f requirements.txt
```
- pip인 경우
```zsh
>>$ pip install -r requirements.txt
```
### app 실행

#### 실행
```zsh
// 경로 (root),  manage.py 위치 , 8080번 포트로 실행
>>$ python manage.py runserver 8080 
```

### 개발명세서

[//]: # (!&#40;개발명세서.pdf&#41;[])

### 구현 설명
#### 1. 문학 작품 조회 기능
- 국가 별 문학 작품 리스트 조회 API 
  - 필터링 지원 (가격 높은|가격 낮은순|출판순|리뷰순)
- 문학 작품 검색 API

#### 2. 문학 작품 소개 상세 페이지
- 작품 상세 조회 API (작품 할인 시, 할인 가격 반영)

#### 3. 문학 작품 통계 조회 기능 
- 문학 작품 판매(결제)순 랭킹 조회 API
  -Django ORM : `Window`를 사용, 매출순으로 랭킹 구현
- 베스트셀러 리스트 API (문학 작품에 있는 리뷰 수로 정렬)

#### 4. 문학 작품 구입 관련 기능 일부
- 유저 보유 포인트 조회 API

### 결과