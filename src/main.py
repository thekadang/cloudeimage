"""
이미지 변환기 - 메인 엔트리포인트

애플리케이션 시작점입니다.

참조 문서: README.md, docs/프로젝트_개요.md
"""

import sys
from pathlib import Path

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def main():
    """메인 함수"""
    print("=" * 60)
    print("이미지 변환기 (Image Converter)")
    print("WebP/AVIF 이미지 변환 데스크톱 애플리케이션")
    print("=" * 60)
    print()

    print("TODO: GUI 초기화 및 애플리케이션 실행")
    print()

    # TODO: PyQt5 애플리케이션 초기화
    # app = QApplication(sys.argv)

    # TODO: 메인 윈도우 생성 및 표시
    # window = MainWindow()
    # window.show()

    # TODO: 이벤트 루프 실행
    # sys.exit(app.exec_())

    print("애플리케이션 구조:")
    print("  src/core/     - 이미지 변환 엔진")
    print("  src/auth/     - 인증 및 구독 관리")
    print("  src/ui/       - 사용자 인터페이스")
    print("  src/utils/    - 유틸리티 함수")
    print()

    print("실행 방법:")
    print("  python src/main.py")
    print()

    print("다음 단계:")
    print("  Task 4: 가상환경 생성 및 의존성 설치 (requirements.txt)")
    print("  Task 5: 보안 모듈 구현")
    print("  Task 6: 이미지 변환 엔진 구현")
    print()


if __name__ == "__main__":
    main()
