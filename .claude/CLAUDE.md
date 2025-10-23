# 이미지변환기 프로젝트 - Claude Code 가이드

> **이 문서는 Claude Code가 프로젝트를 이해하고 작업을 수행하기 위한 메타 가이드입니다.**
> **세션 시작 시 반드시 이 문서를 먼저 읽으세요.**

---

## 📋 프로젝트 개요

### 기본 정보
- **프로젝트명**: 이미지변환기 (Image Converter)
- **목적**: WebP/AVIF 형식으로 이미지를 변환하는 데스크톱 애플리케이션
- **비즈니스 모델**: SaaS 구독 서비스 (Free/Basic/Pro)
- **기술 스택**:
  - 클라이언트: Python 3.8+, PyQt5, Pillow
  - 백엔드: AWS Serverless (Lambda, DynamoDB, API Gateway)
  - 결제: 토스페이먼츠

### 주요 기능
1. 이미지 형식 변환 (JPEG/PNG/BMP/TIFF/GIF → WebP/AVIF)
2. 드래그 앤 드롭 배치 처리
3. 하이브리드 인증 (온라인 + 오프라인 유예)
4. 구독 관리 및 자동 결제
5. 컴퓨터 전체 스캔 (Pro 플랜)

---

## 🚀 세션 시작 시 체크리스트

**매번 작업 시작 시 다음 순서를 따르세요:**

1. **task.md 확인**
   ```bash
   cat task.md
   ```
   - 현재 진행 상황 파악
   - 완료된 작업 [x], 진행 중 [~], 대기 [​ ] 확인
   - 다음 우선순위 작업 식별

2. **Git 상태 확인**
   ```bash
   git status
   git log --oneline -5
   ```
   - 커밋되지 않은 변경사항 확인
   - 최근 작업 이력 파악

3. **관련 문서 읽기**
   - 작업 유형에 따라 아래 "문서 참조 매트릭스" 참조
   - 해당 docs/ 파일 읽고 이해

4. **TodoWrite로 작업 계획**
   - 3단계 이상 작업은 TodoWrite 사용
   - 작업 시작 전 계획 수립

---

## 📚 문서 참조 매트릭스

**작업 유형에 따라 참조해야 할 문서:**

| 작업 유형 | 참조 문서 | 설명 |
|---------|---------|------|
| **UI 개발** | `docs/ui_설계.md` | PyQt5 위젯, 레이아웃, 색상, 폰트 |
| **이미지 변환 로직** | `docs/로컬_변환기능.md` | SafeConverter 클래스, 원자적 변환 |
| **인증/구독 시스템** | `docs/서버_인증시스템.md` | JWT, 하이브리드 인증, API 설계 |
| **배포/코드 서명** | `docs/배포_전략.md` | PyInstaller, 인증서, CI/CD |
| **비즈니스 로직** | `docs/프로젝트_개요.md` | 요금제, KPI, 수익 모델 |
| **보안 관련** | `01_보안_가이드라인.md` | .env, Git 보안, API 키 관리 |
| **전체 작업 목록** | `task.md` | 18개 작업, 마일스톤, 진행사항 |
| **프로젝트 구조** | `README.md` | 폴더 구조, 설치 방법, 개발 가이드 |

---

## 🗂️ 폴더별 책임

### src/core/ - 핵심 변환 엔진
- **참조 문서**: `docs/로컬_변환기능.md`
- **파일**:
  - `converter.py` - SafeConverter 클래스, 이미지 변환
  - `scanner.py` - 파일 스캔, 재귀 탐색
  - `logger.py` - Excel 로그 관리
- **규칙**: 원자적 변환 보장, 원본 백업 옵션

### src/auth/ - 인증 및 구독 관리
- **참조 문서**: `docs/서버_인증시스템.md`
- **파일**:
  - `subscription.py` - SubscriptionManager, 구독 상태 관리
  - `security.py` - JWT 검증, 하드웨어 ID
  - `api_client.py` - AWS API 통신
- **규칙**: 7일 온라인 체크, 30일 오프라인 유예

### src/ui/ - 사용자 인터페이스
- **참조 문서**: `docs/ui_설계.md`
- **파일**:
  - `main_window.py` - 메인 윈도우 (QMainWindow)
  - `settings.py` - 설정 다이얼로그
  - `dialogs.py` - 공통 다이얼로그
- **규칙**: PyQt5 스타일, 반응형 레이아웃

### src/utils/ - 유틸리티
- **참조 문서**: `README.md`
- **파일**:
  - `config.py` - 설정 관리 (JSON)
  - `helpers.py` - 헬퍼 함수
- **규칙**: 재사용 가능한 공통 기능

### tests/ - 테스트 코드
- **참조 문서**: `README.md`
- **규칙**: pytest 프레임워크, 커버리지 80% 이상

### scripts/ - 유틸리티 스크립트
- **참조 문서**: `docs/배포_전략.md`
- **파일**:
  - `sign_windows.bat` - Windows 코드 서명
  - `sign_macos.sh` - macOS 공증
- **규칙**: 배포 자동화

### resources/ - 리소스 파일
- **하위 폴더**: `icons/`, `images/`
- **규칙**: 라이선스 명시, 최적화된 에셋

---

## ⚙️ 개발 규칙 및 컨벤션

### 1. 언어 규칙
- ✅ **문서**: 한국어 (MD 파일, 주석, 커밋 메시지)
- ✅ **코드**: 영어 (변수명, 함수명, 클래스명)
- ❌ **혼용 금지**: 한국어 변수명 사용 금지

```python
# ✅ 올바른 예시
def convert_image(input_path, output_format):
    """이미지를 지정된 형식으로 변환합니다."""
    pass

# ❌ 잘못된 예시
def 이미지변환(입력경로, 출력형식):
    pass
```

### 2. 보안 규칙
- ❌ **절대 커밋 금지**: `.env`, `*.key`, `*.pem`, `secrets.py`
- ✅ **환경 변수 사용**: `os.getenv()` 또는 `python-dotenv`
- ✅ **커밋 전 검증**: `security_check.py` 자동 실행 (Git hooks)
- ✅ **GitHub Secrets**: 민감 정보는 GitHub Secrets에 저장

### 3. Git 워크플로우
- ✅ **브랜치 전략**: `main` (안정), `develop` (개발), `feature/*` (기능)
- ✅ **커밋 메시지**: 한국어, 명확한 설명
  ```
  feat: 이미지 변환 기능 구현

  - SafeConverter 클래스 추가
  - WebP/AVIF 형식 지원
  - 원자적 변환 보장
  ```
- ✅ **커밋 전**: `git status`, `git diff` 확인
- ✅ **자동 검증**: pre-commit hook으로 보안 검사

### 4. 코드 스타일
- **Python**: PEP 8 준수, Black 포맷터 사용
- **들여쓰기**: 4칸 스페이스
- **최대 줄 길이**: 88자 (Black 기본값)
- **타입 힌트**: 함수 시그니처에 타입 명시

```python
def convert_image(
    input_path: str,
    output_format: str,
    quality: int = 85
) -> bool:
    """이미지를 변환합니다."""
    pass
```

### 5. 문서 업데이트 규칙
**코드 변경 시 반드시 관련 MD 파일도 업데이트:**

| 변경 영역 | 업데이트할 문서 |
|---------|---------------|
| UI 컴포넌트 추가/수정 | `docs/ui_설계.md` |
| 변환 로직 변경 | `docs/로컬_변환기능.md` |
| 인증 시스템 변경 | `docs/서버_인증시스템.md` |
| 배포 프로세스 변경 | `docs/배포_전략.md` |
| 비즈니스 로직 변경 | `docs/프로젝트_개요.md` |
| 보안 정책 변경 | `01_보안_가이드라인.md` |
| 작업 완료 | `task.md` (체크박스 [x]) |

---

## 📝 task.md 사용법

### 상태 표시
- `[ ]` TODO: 대기 중
- `[~]` IN_PROGRESS: 진행 중
- `[x]` DONE: 완료
- `[!]` BLOCKED: 차단됨 (의존성 미해결)

### 작업 완료 시
1. 해당 작업의 체크박스를 `[x]`로 변경
2. **완료일** 추가: `- 완료일: YYYY-MM-DD`
3. **결과물** 기록: 생성된 파일, 커밋 해시 등
4. Git 커밋 시 커밋 메시지에 "Task N 완료" 명시

### 진행률 업데이트
- Milestone별 진행률 계산: `완료된 작업 / 전체 작업`
- 상단 전체 진행률 업데이트

**예시:**
```markdown
### [x] Task 1: GitHub 저장소 생성 및 연동
- **우선순위**: P0
- **완료일**: 2025-10-23
- **결과물**: https://github.com/thekadang/cloudeimage.git
- **커밋 해시**: 68488f1
```

---

## 🔄 세션 재개 시 워크플로우

1. **이 문서 읽기** (`.claude/CLAUDE.md`)
2. **task.md 확인** → 마지막 완료 작업, 다음 작업
3. **Git 로그 확인** → 최근 변경사항
   ```bash
   git log --oneline --graph -10
   ```
4. **관련 docs/ 읽기** → 작업에 필요한 문서
5. **TodoWrite 작성** → 작업 계획
6. **작업 실행** → 개발, 테스트, 문서 업데이트
7. **task.md 업데이트** → 체크박스, 완료일
8. **Git 커밋** → 변경사항 저장

---

## 🛠️ 자주 사용하는 명령어

### 개발 환경 설정
```bash
# 가상환경 생성 및 활성화
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS

# 의존성 설치
pip install -r requirements.txt

# 보안 검사
python security_check.py

# Git hooks 설치
python setup_git_hooks.py install
```

### 테스트 실행
```bash
# 전체 테스트
pytest

# 커버리지
pytest --cov=src --cov-report=html
```

### 빌드
```bash
# PyInstaller로 실행 파일 생성
pyinstaller ImageConverter.spec
```

---

## 📞 긴급 상황 대응

### 보안 이슈 발견 시
1. **즉시 작업 중단**
2. `.env` 파일 삭제 확인
3. `security_check.py` 실행
4. GitHub에 푸시된 경우:
   - GitHub Secrets 즉시 재발급
   - 커밋 히스토리에서 제거 (BFG Repo-Cleaner 사용)
5. `01_보안_가이드라인.md` 참조

### 빌드 실패 시
1. `docs/배포_전략.md` 참조
2. 인증서 유효기간 확인
3. PyInstaller 로그 확인
4. 의존성 충돌 확인

### 테스트 실패 시
1. 실패한 테스트 로그 확인
2. 관련 문서 재확인
3. 코드 변경사항 검토
4. 필요 시 롤백

---

## 📌 중요 링크

- **GitHub 리포지토리**: https://github.com/thekadang/cloudeimage.git
- **원본 기획 문서**:
  - `이미지변환기_기획서.md`
  - `서버리스_구독서비스_연동방안.md`
  - `01_보안_가이드라인.md`
  - `추가사항.md`

---

## 💡 팁

### 효율적인 작업을 위해
- 큰 작업은 작은 단위로 분할 (TodoWrite 활용)
- 자주 커밋 (작은 커밋 > 큰 커밋)
- 테스트 먼저 작성 (TDD)
- 문서와 코드 동기화 유지

### 품질 유지를 위해
- 코드 리뷰 체크리스트:
  - [ ] 보안 이슈 없음
  - [ ] 테스트 통과
  - [ ] 문서 업데이트
  - [ ] 타입 힌트 추가
  - [ ] 주석 명확함

---

**최종 업데이트**: 2025-10-23
**버전**: 1.0.0
