# 다신 마주치고 싶지 않은 에러 모음


## module import error

partially initialized module 'copy' has no attribute 'deepcopy' (most likely due to a circular import)
> 파일명과 불러오려는 모듈명이 같으면 발생하는 오류

>> copy.py 파일에서 import copy를 했을 때 발생함
--> 파일명 변경 시 해결

<br/><br/>

