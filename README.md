# 팀 룰렛 프로그램 (League of Legends 내전용)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 소개

🎮 **팀 룰렛 프로그램**은 리그 오브 레전드(LOL) 내전 이벤트를 보다 재미있고 간편하게 진행하기 위해 개발된 가벼운 도구입니다.

내전 중 룰렛, 사다리타기 등 다양한 방식으로 팀을 나누는 번거로움을 줄이고,  
**라인 배정**과 **티어 설정**을 한 번에 해결할 수 있도록 제작되었습니다.

- 팀원별로 라인을 중복 없이 랜덤 배정
- 팀원별로 티어(1~6)를 랜덤 설정
- 6티어일 경우 추가 라인 배정
- 직관적이고 빠른 사용성
- 가벼운 PC 프로그램 (Python Tkinter GUI 기반)

---

## 주요 기능

- 🧩 팀당 5명 입력 (총 2팀)
- 🎲 탑, 정글, 미드, 원딜, 서폿 라인 중 랜덤 배정
- 🔢 1~6 티어 랜덤 지정 (6티어 시 추가 라인 제공)
- 📋 결과를 한눈에 보기 좋게 표로 출력
- 📎 **결과 복사 버튼**으로 바로 클립보드 복사 가능
<img src="https://postfiles.pstatic.net/MjAyNTA0MjZfMTI3/MDAxNzQ1NjY4MTI3Njg5.dO_wrgb6ate9G9tbW1T-o6hwG_3uGDWxjBSj816H_tAg.HURDynXAfelnZ-78YQMCY4jZJflEz68Q7K-P8lWkKogg.PNG/%EB%A3%B0%EB%A0%9B.PNG?type=w966" width="400px">

---

## 설치 및 실행 방법

### 1. Python 설치
- Python 3.10 이상 설치 (3.12은 추천하지 않음)
- [Python 3.10 다운로드 링크](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)

설치할 때 꼭 `Add Python to PATH` 옵션 체크!

### 2. 프로젝트 파일 다운로드
- `abeul_roulette.py` 파일을 다운로드합니다.

### 3. 필요한 라이브러리 설치
별도로 설치해야 할 외부 라이브러리는 없습니다.  
**Tkinter**와 **random** 모듈은 Python 기본 패키지에 포함되어 있습니다.

### 4. 실행
다운로드 받은 폴더에서 터미널(cmd) 열고:

```bash
python abeul_roulette.py
