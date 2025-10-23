# 이미지 변환기 (Image Converter)

> WebP/AVIF 형식으로 이미지를 변환하는 데스크톱 애플리케이션

[![License](https://img.shields.io/badge/license-Proprietary-red.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/)

---

## 📋 프로젝트 개요

**이미지 변환기**는 다양한 이미지 파일(JPEG, PNG, BMP, TIFF, GIF)을 최신 웹 최적화 형식인 **WebP**와 **AVIF**로 변환하는 데스크톱 애플리케이션입니다.

### 핵심 기능
- ✅ **다양한 형식 지원**: JPEG, PNG, BMP, TIFF, GIF → WebP/AVIF
- ✅ **간편한 사용**: 드래그 앤 드롭으로 즉시 변환
- ✅ **안전한 변환**: 원본 백업 옵션 제공
- ✅ **배치 처리**: 여러 파일 동시 변환
- ✅ **컴퓨터 전체 스캔**: PC 전체 이미지 자동 최적화 (Pro 플랜)
- ✅ **상세 로그**: Excel 파일로 변환 이력 관리

### 주요 장점
- 🚀 **웹사이트 성능 향상**: 이미지 크기 30-70% 감소
- ⏱️ **시간 절약**: 자동 배치 처리로 대량 변환 간편
- 🛡️ **안전성**: 변환 실패 시 자동 복구 메커니즘

---

## 🎯 타겟 사용자

- **웹 개발자**: 웹사이트 이미지 최적화 필요
- **디자이너**: 대량 이미지 변환 작업
- **블로거/콘텐츠 크리에이터**: 블로그 이미지 최적화
- **쇼핑몰 운영자**: 상품 이미지 최적화
- **일반 사용자**: PC 저장 공간 절약

---

## 💰 요금제

| 플랜 | 월 요금 | 일일 변환 한도 | 주요 기능 |
|------|---------|---------------|-----------|
| **Free** | 0원 | 5개 파일 | WebP 변환, 개별 파일 |
| **Basic** | 4,900원 | 50개 파일 | WebP/AVIF, 폴더 변환, 예약 작업 |
| **Pro** | 9,900원 | 무제한 | 전체 기능, 컴퓨터 스캔 |

---

## 🛠️ 기술 스택

### 클라이언트 (데스크톱 앱)
- **언어**: Python 3.8+
- **GUI**: PyQt5
- **이미지 처리**: Pillow, pillow-avif-plugin
- **보안**: cryptography, keyring
- **패키징**: PyInstaller

### 백엔드 (서버리스)
- **플랫폼**: AWS
- **컴퓨팅**: Lambda (Python 3.9)
- **API**: API Gateway (REST + JWT)
- **데이터베이스**: DynamoDB
- **모니터링**: CloudWatch

### 결제
- **PG사**: 토스페이먼츠
- **방식**: 자동 결제 (정기 구독)

---

## 📂 프로젝트 구조

```
image-converter/
├── src/                      # 소스 코드
│   ├── core/                 # 핵심 로직
│   │   ├── converter.py      # 이미지 변환 엔진
│   │   ├── scanner.py        # 파일 스캔
│   │   └── logger.py         # 로그 관리
│   ├── auth/                 # 인증 및 구독 관리
│   │   ├── subscription.py   # 구독 관리
│   │   ├── security.py       # 보안 모듈
│   │   └── api_client.py     # API 통신
│   ├── ui/                   # 사용자 인터페이스
│   │   ├── main_window.py    # 메인 윈도우
│   │   ├── settings.py       # 설정 UI
│   │   └── dialogs.py        # 다이얼로그
│   └── utils/                # 유틸리티
│       ├── config.py         # 설정 관리
│       └── helpers.py        # 헬퍼 함수
├── tests/                    # 테스트 코드
├── docs/                     # 프로젝트 문서
│   ├── 프로젝트_개요.md
│   ├── ui_설계.md
│   ├── 로컬_변환기능.md
│   ├── 서버_인증시스템.md
│   └── 배포_전략.md
├── scripts/                  # 유틸리티 스크립트
│   ├── sign_windows.bat      # Windows 코드 서명
│   └── sign_macos.sh         # macOS 코드 서명
├── resources/                # 리소스 파일
│   ├── icons/                # 아이콘
│   └── images/               # 이미지
├── .env.example              # 환경 변수 템플릿
├── .gitignore                # Git 제외 목록
├── requirements.txt          # 파이썬 의존성
├── ImageConverter.spec       # PyInstaller 설정
├── task.md                   # 전체 작업 목록
└── README.md                 # 프로젝트 설명 (본 파일)
```

---

## 🚀 개발 환경 설정

### 1. 저장소 클론

```bash
git clone https://github.com/[username]/image-converter.git
cd image-converter
```

### 2. 가상환경 생성 및 활성화

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. 의존성 설치

```bash
pip install -r requirements.txt
```

### 4. 환경 변수 설정

`.env.example` 파일을 `.env`로 복사하고 실제 값을 입력하세요.

```bash
# Windows
copy .env.example .env

# Linux/macOS
cp .env.example .env
```

`.env` 파일 예시:
```env
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
TOSS_PAYMENTS_SECRET_KEY=your_toss_secret_key
ENCRYPTION_KEY=your_encryption_key
```

### 5. 프로그램 실행

```bash
python src/main.py
```

---

## 🧪 테스트 실행

```bash
# 전체 테스트
pytest

# 테스트 커버리지
pytest --cov=src --cov-report=html
```

---

## 📦 빌드 및 배포

### Windows 빌드

```bash
# PyInstaller로 빌드
pyinstaller ImageConverter.spec

# 코드 서명 (Windows)
.\scripts\sign_windows.bat
```

### macOS 빌드

```bash
# PyInstaller로 빌드
pyinstaller ImageConverter.spec

# 코드 서명 및 공증 (macOS)
bash scripts/sign_macos.sh
```

---

## 🔐 보안 가이드

### 중요 사항
- ❌ **절대 `.env` 파일을 Git에 커밋하지 마세요!**
- ❌ **API 키나 비밀키를 코드에 하드코딩하지 마세요!**
- ✅ **환경 변수로만 민감 정보를 관리하세요.**
- ✅ **커밋 전 보안 검사를 실행하세요.**

### 보안 검사 실행

```bash
# 보안 스캔
python security_check.py

# Git Hooks 설치 (커밋 전 자동 보안 검사)
python setup_git_hooks.py install
```

**자세한 내용**: [01_보안_가이드라인.md](./01_보안_가이드라인.md)

---

## 📚 문서

### 기획 및 요구사항
- [이미지변환기_기획서.md](./이미지변환기_기획서.md) - 전체 기획 내용
- [서버리스_구독서비스_연동방안.md](./서버리스_구독서비스_연동방안.md) - 서버 아키텍처
- [추가사항.md](./추가사항.md) - 배포 및 마케팅 전략

### 보안 및 운영
- [01_보안_가이드라인.md](./01_보안_가이드라인.md) - 보안 정책 및 가이드

### 작업 관리
- [task.md](./task.md) - 전체 작업 목록 및 일정

### 기술 문서
- [docs/프로젝트_개요.md](./docs/프로젝트_개요.md) - 프로젝트 전반 개요
- [docs/ui_설계.md](./docs/ui_설계.md) - UI/UX 설계 가이드
- [docs/로컬_변환기능.md](./docs/로컬_변환기능.md) - 이미지 변환 엔진 설계
- [docs/서버_인증시스템.md](./docs/서버_인증시스템.md) - 인증 시스템 아키텍처
- [docs/배포_전략.md](./docs/배포_전략.md) - 배포 및 코드 서명 가이드

---

## 🗓️ 개발 일정

| 단계 | 기간 | 주요 산출물 |
|------|------|------------|
| **Phase 1: 프로젝트 초기 설정** | 1주 | GitHub, 보안 설정, 프로젝트 구조 |
| **Phase 2: 핵심 기능 개발** | 4주 | 변환 엔진, 인증, UI |
| **Phase 3: 백엔드 구축** | 3주 | AWS Lambda, DynamoDB, API |
| **Phase 4: 패키징 및 배포** | 2주 | 실행 파일, 코드 서명 |
| **Phase 5: 테스트 및 QA** | 2주 | 테스트, 버그 수정 |
| **Phase 6: 베타 테스트** | 2주 | 베타 배포, 피드백 |
| **Phase 7: 정식 출시** | 1주 | 정식 버전, 마케팅 |
| **총 개발 기간** | **15주** | |

**자세한 일정**: [task.md](./task.md)

---

## 🤝 기여하기

현재 이 프로젝트는 **Private Repository**로 운영되며, 내부 개발팀만 접근 가능합니다.

---

## 📞 연락처

- **개발팀**: dev@imageconverter.com
- **고객 지원**: support@imageconverter.com
- **공식 웹사이트**: https://imageconverter.com

---

## 📄 라이선스

Copyright © 2025 ImageConverter. All rights reserved.

이 소프트웨어는 독점 소프트웨어이며, 무단 복제, 배포, 수정을 금지합니다.

---

## 🎯 프로젝트 목표

### 단기 (6개월)
- ✅ Windows/macOS 버전 출시
- ✅ 한국어 완벽 지원
- ✅ 국내 10,000명 사용자 확보

### 중기 (1년)
- 🔲 다국어 지원 (영어, 일본어)
- 🔲 플러그인 시스템 도입
- 🔲 해외 결제 시스템 연동

### 장기 (2-3년)
- 🔲 웹 버전 출시
- 🔲 기업용 플랜 (Enterprise)
- 🔲 API 서비스 제공
- 🔲 글로벌 100,000명 사용자

---

> **⚠️ 중요 공지**
> - 이 프로젝트는 개발 중입니다.
> - 모든 기획 및 설계 문서는 변경될 수 있습니다.
> - 보안 관련 사항은 [01_보안_가이드라인.md](./01_보안_가이드라인.md)를 반드시 확인하세요.

**최종 업데이트**: 2025-10-23
