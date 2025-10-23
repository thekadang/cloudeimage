#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Git Hooks 자동 설정 스크립트

이 스크립트는 커밋 전에 자동으로 보안 검사를 실행하도록 Git Hooks를 설정합니다.
"""

import os
import sys
import stat
from pathlib import Path


class GitHooksInstaller:
    """Git Hooks 설치 관리자"""

    def __init__(self):
        self.git_hooks_dir = Path('.git/hooks')
        self.pre_commit_hook = self.git_hooks_dir / 'pre-commit'

    def check_git_repository(self):
        """Git 저장소인지 확인"""
        if not Path('.git').exists():
            print("❌ Git 저장소가 아닙니다!")
            print("   먼저 'git init'을 실행하세요.\n")
            return False
        return True

    def create_pre_commit_hook(self):
        """pre-commit hook 생성"""
        hook_content = """#!/bin/sh
# Pre-commit hook: 보안 검사 자동 실행

echo "🔍 커밋 전 보안 검사 실행 중..."
echo ""

# Python 스크립트 실행
python security_check.py

# 검사 결과 확인
if [ $? -ne 0 ]; then
    echo ""
    echo "❌ 보안 검사 실패! 커밋이 중단되었습니다."
    echo "   위의 문제를 해결한 후 다시 커밋하세요."
    echo ""
    exit 1
fi

echo ""
echo "✅ 보안 검사 통과! 커밋을 진행합니다."
echo ""

exit 0
"""

        # Windows용 배치 파일도 생성
        hook_content_bat = """@echo off
REM Pre-commit hook: 보안 검사 자동 실행

echo 🔍 커밋 전 보안 검사 실행 중...
echo.

REM Python 스크립트 실행
python security_check.py

REM 검사 결과 확인
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ 보안 검사 실패! 커밋이 중단되었습니다.
    echo    위의 문제를 해결한 후 다시 커밋하세요.
    echo.
    exit /b 1
)

echo.
echo ✅ 보안 검사 통과! 커밋을 진행합니다.
echo.

exit /b 0
"""

        # 훅 파일 작성
        with open(self.pre_commit_hook, 'w', encoding='utf-8', newline='\n') as f:
            f.write(hook_content)

        # Windows용 배치 파일
        pre_commit_bat = self.git_hooks_dir / 'pre-commit.bat'
        with open(pre_commit_bat, 'w', encoding='utf-8') as f:
            f.write(hook_content_bat)

        # 실행 권한 설정 (Unix/Linux/macOS)
        if os.name != 'nt':  # Windows가 아니면
            st = os.stat(self.pre_commit_hook)
            os.chmod(self.pre_commit_hook, st.st_mode | stat.S_IEXEC)

        print("✅ pre-commit hook이 설치되었습니다!")
        print(f"   위치: {self.pre_commit_hook}\n")

    def install(self):
        """Git Hooks 설치"""
        print("🔧 Git Hooks 설치 중...\n")

        # Git 저장소 확인
        if not self.check_git_repository():
            return False

        # hooks 디렉토리 확인
        if not self.git_hooks_dir.exists():
            print("❌ .git/hooks 디렉토리가 없습니다!")
            return False

        # 기존 hook 백업
        if self.pre_commit_hook.exists():
            backup_path = self.pre_commit_hook.with_suffix('.backup')
            print(f"⚠️  기존 pre-commit hook을 백업합니다: {backup_path}")
            self.pre_commit_hook.rename(backup_path)

        # pre-commit hook 생성
        self.create_pre_commit_hook()

        print("=" * 60)
        print("🎉 Git Hooks 설치 완료!")
        print("=" * 60)
        print("\n📝 이제부터 git commit 시 자동으로 보안 검사가 실행됩니다.")
        print("\n사용법:")
        print("  git add .")
        print("  git commit -m \"커밋 메시지\"  # 자동으로 보안 검사 실행됨")
        print()

        return True

    def remove(self):
        """Git Hooks 제거"""
        print("🗑️  Git Hooks 제거 중...\n")

        if self.pre_commit_hook.exists():
            self.pre_commit_hook.unlink()
            print("✅ pre-commit hook이 제거되었습니다!\n")

            # 백업 파일 복원
            backup_path = self.pre_commit_hook.with_suffix('.backup')
            if backup_path.exists():
                print(f"♻️  백업 파일을 복원합니다: {backup_path}")
                backup_path.rename(self.pre_commit_hook)
        else:
            print("ℹ️  설치된 pre-commit hook이 없습니다.\n")

        return True

    def status(self):
        """Git Hooks 상태 확인"""
        print("📊 Git Hooks 상태 확인...\n")

        if not self.check_git_repository():
            return False

        if self.pre_commit_hook.exists():
            print("✅ pre-commit hook이 설치되어 있습니다.")
            print(f"   위치: {self.pre_commit_hook}")

            # 파일 내용 확인
            with open(self.pre_commit_hook, 'r', encoding='utf-8') as f:
                content = f.read()

            if 'security_check.py' in content:
                print("   상태: 정상 (보안 검사 활성화)\n")
            else:
                print("   상태: 비정상 (보안 검사 비활성화)\n")
        else:
            print("❌ pre-commit hook이 설치되어 있지 않습니다.")
            print("   'python setup_git_hooks.py install'을 실행하세요.\n")

        return True


def print_usage():
    """사용법 출력"""
    print("\n" + "=" * 60)
    print("Git Hooks 자동 설정 스크립트")
    print("=" * 60)
    print("\n사용법:")
    print("  python setup_git_hooks.py install  # Git Hooks 설치")
    print("  python setup_git_hooks.py remove   # Git Hooks 제거")
    print("  python setup_git_hooks.py status   # 상태 확인")
    print()


def main():
    """메인 함수"""
    installer = GitHooksInstaller()

    if len(sys.argv) < 2:
        print_usage()
        return 0

    command = sys.argv[1].lower()

    if command == 'install':
        success = installer.install()
        return 0 if success else 1

    elif command == 'remove':
        success = installer.remove()
        return 0 if success else 1

    elif command == 'status':
        success = installer.status()
        return 0 if success else 1

    else:
        print(f"❌ 알 수 없는 명령어: {command}")
        print_usage()
        return 1


if __name__ == "__main__":
    sys.exit(main())
