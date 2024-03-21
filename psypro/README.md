### **프로젝트 주제** : Flask를 이용한 심리테스트 제작

- 사용자가 정보를 입력한 후 진행되는 심리테스트의 결과를 데이터베이스에 저장하고
  이를 시각화하는 프로젝트

### **프로젝트 목표**

- **백엔드 (Flask 애플리케이션)**
  - 사용자 모델과 테스트 결과 모델을 포함한 데이터베이스 설계
    - ERD 작성을 통해 만들고자 하는 데이터베이스의 논리적 구조 설계
    - 스키마 작성을 통해 만들고자 하는 데이터베이스의 물리적 구조 설계
  - 사용자 정보 및 테스트 응답을 저장하는 API
    - API 문서 만들기
  - 테스트 결과를 분석하고 시각화 데이터를 생성하는 로직

### 1. 엔티티(Entity)

- **Participant**

  - `id`: 정수, 기본 키(Primary Key)
  - `name`: 문자열(100자 이내), nullable=False
  - `age`: 정수, nullable=False
  - `gender`: 문자열(10자 이내), nullable=False
  - `created_at`: 날짜 및 시간, nullable=False

- **Answer**
  - `id`: 정수, 기본 키(Primary Key)
  - `question_id`: 정수, nullable=False
  - `k_answer`: 문자열(100자 이내), nullable=False
  - `participant_id`: 정수, `Participant`의 `id`를 외래 키(Foreign Key)로 참조, nullable=False

### 2. 관계(Relationship)

- **Participant**와 **Answer** 사이에는 1:N(일대다) 관계가 있습니다. 한 명의 참가자(Participant)는 여러 개의 답변(Answer)을 가질 수 있으며, 각 답변은 특정 참가자에게 속합니다. 이 관계는 `Answer` 테이블의 `participant_id` 필드를 통해 `Participant`의 `id`를 외래 키로 참조함으로써 구현.

### ERD 구조 설계도

```
[Participant]               [Answer]
| id            | 1      |---| participant_id |
| name          |        | N | question_id    |
| age           |        |   | k_answer       |
| gender        |        |   | id             |
| created_at    |
```

이 다이어그램은 `Participant`와 `Answer` 엔티티 사이의 관계를 간략하게 나타냅니다. 각각의 테이블은 속성(필드)들로 구성되어 있고, `Answer` 테이블은 `Participant` 테이블의 `id`를 `participant_id`로 참조하는 외래 키를 통해 1:N 관계를 형성한다.

## 개인 프로젝트 1 Day

### 기본 가상환경 설정하고, db와 app.py, routes.py, models.py 작성

1. **Flask Blueprint 설정**: `Blueprint`를 사용하여 앱을 모듈화. 이를 통해 애플리케이션의 다른 부분과 라우트를 쉽게 통합할 수 있다.

2. **참여자 정보 입력**: 사용자로부터 참여자의 이름, 나이, 성별을 입력받아 데이터베이스에 저장.

3. **설문 응답 제출**: 사용자로부터 설문 응답을 받아 데이터베이스에 저장. 참여자 ID가 쿠키에 저장되어 있다고 가정.

4. **결과 시각화**: Plotly Express를 사용하여 데이터베이스에 저장된 설문 응답 데이터를 기반으로 결과를 시각화. 날짜별 참가자 수와 각 문제에 대한 응답 비율을 바 차트와 파이 차트로 표시.

5. **데이터베이스 설정**: SQLite를 사용하여 애플리케이션의 데이터를 저장. Flask-SQLAlchemy와 Flask-Migrate를 사용하여 데이터베이스와 모델을 관리.

6. **CORS 설정**: `CORS(app)`를 사용하여 Cross-Origin Resource Sharing을 활성화합니다. 이는 다른 도메인에서도 API에 접근할 수 있게 해줌..

7. **참여자(Participant) 및 응답(Answer) 모델**: 데이터베이스에 저장될 참여자와 응답 데이터의 구조를 정의.

### index.html에서 기본 정보 입력하고 POST /particippants 로 넘어가지 않는다.

- 오후내내 어디서 안넘어가는지 보다 포기.
- 내일 다시 정신 차리고 해봐야겠다
- <img width="1236" alt="Screenshot 2024-03-21 at 4 16 19 PM" src="https://github.com/Seou0912/0321_Flask_PsychologicalTest/assets/151927766/9c505669-517b-49dd-826f-4ac16e9b04bd">
<img width="1095" alt="Screenshot 2024-03-21 at 4 18 06 PM" src="https://github.com/Seou0912/0321_Flask_PsychologicalTest/assets/151927766/dd397d03-704a-4e62-864a-020c33999d33">

