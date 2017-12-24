# 북한남 갤러리 프로젝트
북한남 갤러리 대관 및 홍보 웹 사이트 구축

## 핵심기능
- 푸쉬 알림
- 캘린더(장고 스케줄러)
- 메일 인증 백엔드(링크 클릭시 회원가입 및 로그인 완료)
- 결제(아임포트)
- 이메일 커스텀 도메인(메일건)
- SSL (http로 접속해도 https로 )
- 예약(시간 단위 자동화 기능), 크론탭 활용
- 어드민 커스텀

## 개발환경
- Framework: Vue.js(프론트엔드) + DRF(백엔드)
- Language: Python 3.6.1
- DataBase: SQLite3(로컬용) + PostgreSQL(배포용)

## 설치

project root 상위에서
`npm install -g bower`

project root에서
`./manage.py bower install`
`./manage.py collectstatic`


