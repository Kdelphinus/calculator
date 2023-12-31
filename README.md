# 세뱃돈 계산기

## 개요
- 기간: 23.09.30 ~ 23.10.03
- 문제: [항해 플러스: 제1회 코육대](https://hanghaeplus-coyukdae.oopy.io/)
- 언어: Python3.10

## 사용 방법

### 1. `계산기` 실행 파일 실행

- 더블 클릭으로 실행

### 2. `코드`로 실행

```shell
$ pip install -r requirements.txt
$ python3 src/main.py
```

## 요구 사항

- [x] 디스플레이는 0으로 시작
- [x] 연산자는 숫자 사이에서만 입력되는 케이스만 들어옴
- [x] 소수점 이하는 버리고 정수로 표시
- [x] 세뱃돈은 원화로 주어지며, 최대 10자리 숫자까지만 입력
- [x] 10자리 숫자를 넘어가는 결과값은 `Infinity` 로 표시
- [x] 연산자 다음에 `=`을 입력하면 `alert`를 표시
- [x] 실수로 입력한 것을 모두 지우는 `AC`
- [x] 마지막에 입력한 값만 지울 수 있는 `C`
- [x] 0 나누기 0과 같은 예외 결과값은 `숫자 아님`으로 표시
- [x] 연산자를 연달아 선택할 경우 마지막에 선택한 연산자가 적용되어야 한다.

## 문제

- 한 글자씩 출력하기에 `C`로 지워도 출력은 지워지지 않는다.
