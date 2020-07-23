# README.md

`Flask`는 우리에게 많은 자유를 준다.

하지만 이 자유는 책임을 질 수 있을 때 빛나는 법이다.

어떻게하면 플라스크가 주는 자유로움을 책임감 있게 사용할 수 있을지 고민했다.

그래서 이 `Boilerplate`를 만들게 되었다.

필자가 고려한 점은 다음과 같다.

- pytest를 사용하는데 있어서 편리한가?
- 테스트 환경과 배포 환경 분리가 편리한가?
- 디버깅이 편리한가?
- 일관된 프로젝트 규칙이 있는가?
- 프로젝트에서 필요한 부분만 이식하기 편리한 구조인가?

# 참고 사항

`Django`에서 프로젝트를 생성하고 app단위로 구조를 가져가는 것과 같은 맥락으로 프로젝트 기본 구성을 했다.

- 개발/배포 환경을 분리
    - [flask development-production](https://flask.palletsprojects.com/en/1.1.x/config/#development-production)

