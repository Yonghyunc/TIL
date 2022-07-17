# Today I Learned

## 0. 주의사항
1. init한 폴더 내의 폴더 init 하지 말 것 (서브모듈)
2. Vscode 열 때 버전을 관리하는 폴더에서 열기
3. 깃허브 내 수정 먼저 하지 말 것 (Local -> Remote)

## 1. Git 초기 설정
1. 이름, 메일주소 설정
- 최초 한번만
  - `$ git config --global user.name "이름"`
  - `$ git config --global user.email "메일 주소"`

- 확인
  - `$ git config --global --list`

## 2. Git 버전 관리
3가지 공간 
1. Working Directory
2. Staging Area
3. Repository : 커밋 저장

## 3. README.md
- 프로젝트의 대문 (첫 설명)

## 4. .gitignore
- 특정 파일/폴더에 대해 Git이 버전 관리를 하지 못하도록 지정
- 민감 정보, 개발 언어에서 사용되는 파일 등
- !!! 제외하고 싶은 파일은 반드시 git add 전에 .gitignore에 작성해야 함 !!!
- 버전관리를 이미 한 파일은 숨길 수가 없음
- gitignore.io 참고

## 5. Git 기본 명령어
1. 일반 폴더 -> 로컬 저장소 (깃 폴더)
- `$ git init`

2. 버전 상태 출력 (가장 중요한 코드!!!)
- `$ git status`

3. WD -> SA
- `$ git add [file]`
- 전체 `$ git add .`

4. SA -> Repository (Commit)
- 변경사항을 하나의 버전(커밋)으로 저장
- `$ git commit -m "커밋 메시지"`

## 6. 원격 저장소
1. GitHub에서 원격 저장소 생성

2. 로컬 저장소와 원격 저장소 연결

3. git remote (길)
- 로컬 저장소에 원격 저장소를 등록, 조회, 삭제
  1. 등록
  - git remote add <이름> <주소>
  ` $ git remote add origin https://github.com/Yonghyunc/TIL.git`
  2. 조회
  - `$ git remote -v`
  3. 삭제
  - git remote rm <이름>
  `$ git remote rm origin`

4. 원격 저장소에 커밋 업로드 (보내기)
- git push <저장소 이름> <브랜치 이름>
- `$ git push origin master`
- `$ git push -u origin master` 이후에는 `$ git push` 만 작성해도 됨

## 7. 원격 저장소 가져오기
1. git clone
- 원격 저장소를 가져와(복제) 로컬 저장소를 생성
- 로컬 저장소를 생성할 위치에서 git bash 열어서 `$ git clone <원격 저장소 주소>`
- git clone 이 하는 것
  1. 폴더 생성
  2. git init
  3. git remote add
  4. 버전, 파일 생성

2. git pull
- 원격 저장소의 변경 사항을 로컬 저장소에 업데이트
- git pull <저장소 이름> <브랜치 이름>
- `$ git pull origin master`
