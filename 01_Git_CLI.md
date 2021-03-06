# Today I Learned
1. Git & GitHub
2. GUI & CLI
3. CLI 명령어

## 1. Git & GitHub
- Git : 분산버전관리시스템 <-> SVN (중앙집중식)
  - 백업 (add, commit ...)
  - 복구
  - 협업 (push, pull, clone ...)
- GitHub : Git 저장소, 다른 사람과 함께 Git을 관리할 수 있음

## 2. GUI & CLI
- GUI (Graphic User Interface) : 직관적인 조작방식
- CLI (Command Line Interface) : 텍스트 터미널을 통해 사용자와 컴퓨터가 상호작용
  - 입력 / 출력
  - 터미널 / 셸(shell)

## 3. CLI 명령어
1. touch
- 파일 생성
`$ touch a.txt`
- 숨김 파일을 만들기 위해서는 .을 파일명 앞에 붙임
`$ touch .a.txt`

2. mkdir (make directory)
- 폴더 생성
`$ mkdir folder`
- 띄어쓰기로 구분하여 여러 폴더 한번에 생성 가능
`$ mkdir folder1 folder2`
- 폴더 이름 사이 공백을 넣으려면 따옴표로 묶어서 입력
`$ mkdir 'new folder`

3. ls (list segments)
- 현재 작업 중인 디렉토리의 폴더/파일 목록
- -a : 숨긴 파일/폴더까지 전부 보여줌
`$ ls -a `
- -l : long 옵션, 파일 정보 상세히 보여줌
`$ ls -l` 
- 옵션 함께 적용 가능
`$ ls -a -l` 

4. mv (move)
- 폴더/파일 이동 및 이름 변경
- 다른 폴더로 파일 이동
`$ mv a.txt folder`
- 파일 이름 변경
`$ mv a.txt b.txt`

5. cd (change directory)
- 현재 작업 중인 디텍토리 변경
- 홈 디렉토리로 이동
`$ cd`
- 부모 디렉토리로 이동 (위로 가기)
`$ cd ..`
- 전 디렉토리로 이동 (뒤로 가기)
`cd -`
- 현재 작업 중인 디렉토리 내 해당 폴더로 이동
`$ cd folder`
- 절대 경로를 통한 디렉토리 변경 (주소)
- 상대 경로를 통한 디렉토리 변경 (상대위치)

6. rm (remove)
- 폴더/파일 완전 삭제
- 파일 삭제
`$ rm a.txt`
- txt파일 전체 삭제
`$ rm *.txt`
- 폴더 삭제
`$ rm folder`
  - -r : recursive(재귀)옵션 : 폴더 안까지 재귀적으로 전부 삭제
  
7. start (mac에서는 open)
- 폴더/파일 열기
`$ start a.txt`
