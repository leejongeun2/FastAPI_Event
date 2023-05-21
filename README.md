* routes 폴더
    * events.py: 이벤트 생성, 변경, 삭제 등의 처리를 위한 라우팅
    * users: 사용자 등록 및 로그인 처리를 위한 라우팅

* models 폴더
    1. events.py 이벤트 처리용 모델을 정의 
    2. users.py 사용자 처리용 모델을 정의

* 등록된 사용자는 이벤트를 추가, 변경, 삭제할 수 있으며 애플리케이션이 자동으로 만든 이벤트 페이지에서 생성된 이벤트를 확인할 수 있음
* 등록된 사용자와 이벤트는 모두 공유한 id를 갖는다. 
    * 따라서, 사용자와 이벤트가 중복되는 것을 방지할 수 있다. 

3. api 라우트 시스템 구현
* 먼저 사용자 라우트 시스템을 설계
* 사용자 라우트는 로그인, 로그아웃, 등록으로 구성
    * 인증을 완료한 사용자는 이벤트를 생성, 변경, 삭제할 수 있으며, 인증을 거치지 않은 사용자는 생성된 이벤트를 확인하는 것만 가능

4. main.py에 라우트 등록 후 애플리케이션 실행