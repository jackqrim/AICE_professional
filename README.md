# AICE Professional Course

AI와 머신러닝을 위한 전문 교육 과정 자료입니다.

## 📋 필수 패키지 설치

### 방법 1: requirements.txt 사용 (권장)
```bash
pip install -r requirements.txt
```

### 방법 2: 개별 패키지 설치
```bash
# 핵심 패키지들
pip install numpy pandas matplotlib scikit-learn
pip install nltk konlpy transformers tensorflow
pip install beautifulsoup4 openpyxl gensim requests
```

## 🔧 일반적인 설치 오류 해결

### BeautifulSoup 설치 오류
`ModuleNotFoundError: No module named 'bs4'` 오류가 발생하는 경우:

1. 터미널을 엽니다: `Ctrl + ` ` (백틱)
2. 다음 명령어를 실행합니다:
   ```bash
   pip install beautifulsoup4
   ```
3. VSCode에서 올바른 Python 인터프리터가 선택되어 있는지 확인:
   - `Ctrl + Shift + P` → "Python: Select Interpreter" 선택

자세한 내용은 `BeautifulSoup_Installation_Guide.ipynb` 파일을 참조하세요.

## 📁 폴더 구조

- `2-1/`: 자연어 처리 관련 노트북
- `2-2/`: 컴퓨터 비전 및 딥러닝 관련 노트북
- `BeautifulSoup_Installation_Guide.ipynb`: BeautifulSoup 설치 및 사용 가이드

## 🐍 Python 환경 설정

가상환경 사용을 권장합니다:

```bash
# 가상환경 생성
python -m venv aice_env

# 가상환경 활성화 (Windows)
aice_env\Scripts\activate

# 가상환경 활성화 (macOS/Linux)
source aice_env/bin/activate

# 패키지 설치
pip install -r requirements.txt
```
