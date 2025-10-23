#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
보안 검증 스크립트

이 스크립트는 커밋 전에 보안 위험이 있는 파일이나 코드를 검사합니다.
참조: 01_보안_가이드라인.md
"""

import os
import re
import glob
import sys
from pathlib import Path


class SecurityValidator:
    """코드 보안 검증"""

    # 비밀키 패턴
    SECRET_PATTERNS = [
        (r'aws_access_key_id\s*=\s*["\'][A-Z0-9]{20}["\']', 'AWS Access Key'),
        (r'aws_secret_access_key\s*=\s*["\'][A-Za-z0-9/+=]{40}["\']', 'AWS Secret Key'),
        (r'sk_[a-zA-Z0-9]{32,}', 'Toss Payments Secret Key'),
        (r'ghp_[a-zA-Z0-9]{36}', 'GitHub Token'),
        (r'password\s*=\s*["\'][^"\']{8,}["\']', 'Password'),
        (r'secret\s*=\s*["\'][^"\']{16,}["\']', 'Secret'),
        (r'api_key\s*=\s*["\'][^"\']{16,}["\']', 'API Key'),
        (r'token\s*=\s*["\'][^"\']{32,}["\']', 'Token'),
    ]

    # 제외할 파일 패턴
    EXCLUDE_PATTERNS = [
        '.git',
        '__pycache__',
        '.env',
        'venv',
        'env',
        'node_modules',
        '.pytest_cache',
        'dist',
        'build',
        '*.pyc',
        '*.pyo',
        '*.pyd',
        '.env.example',  # 예외: 템플릿 파일은 검사 안 함
    ]

    def __init__(self):
        self.found_issues = []
        self.scanned_files = 0

    def scan_for_secrets(self, file_path):
        """파일에서 비밀키 패턴 검색"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            issues = []
            for pattern, secret_type in self.SECRET_PATTERNS:
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    # .env.example은 템플릿이므로 제외
                    if '.env.example' in str(file_path):
                        continue

                    for match in matches:
                        # 실제 값인지 확인 (템플릿 문자열 제외)
                        if not self._is_placeholder(match):
                            issues.append({
                                'file': file_path,
                                'type': secret_type,
                                'match': match[:50] + '...' if len(match) > 50 else match
                            })

            return issues

        except Exception as e:
            print(f"⚠️  파일 읽기 오류: {file_path} - {e}")
            return []

    @staticmethod
    def _is_placeholder(text):
        """템플릿 문자열인지 확인"""
        placeholders = [
            'your_', 'example', 'placeholder', 'xxx', 'yyy',
            'test_', 'dummy', 'sample', 'here', 'todo'
        ]
        text_lower = text.lower()
        return any(ph in text_lower for ph in placeholders)

    def check_all_files(self):
        """모든 Python 파일 보안 검사"""
        print("🔍 보안 검사 시작...\n")

        # Python 파일 검색
        python_files = []
        for pattern in ['**/*.py', '**/*.pyw']:
            python_files.extend(Path('.').glob(pattern))

        for file_path in python_files:
            # 제외 패턴 확인
            if any(exclude in str(file_path) for exclude in self.EXCLUDE_PATTERNS):
                continue

            self.scanned_files += 1
            issues = self.scan_for_secrets(file_path)

            if issues:
                self.found_issues.extend(issues)

        return len(self.found_issues) == 0

    def check_gitignore(self):
        """필수 .gitignore 항목 확인"""
        print("📋 .gitignore 검사 중...\n")

        required_items = [
            ".env*",
            "!.env.example",
            "*.key",
            "*.pem",
            "secrets.py",
            "user_data/",
            "logs/"
        ]

        if not os.path.exists(".gitignore"):
            print("❌ .gitignore 파일이 없습니다!")
            return False

        with open(".gitignore", "r", encoding='utf-8') as f:
            gitignore_content = f.read()

        missing_items = []
        for item in required_items:
            if item not in gitignore_content:
                missing_items.append(item)

        if missing_items:
            print("❌ .gitignore에 다음 항목들이 누락되었습니다:")
            for item in missing_items:
                print(f"   - {item}")
            return False
        else:
            print("✅ .gitignore 검사 통과\n")
            return True

    def check_env_files(self):
        """실제 .env 파일이 커밋되려는지 확인"""
        print("🔒 환경 변수 파일 검사 중...\n")

        env_files = list(Path('.').glob('**/.env'))
        env_files.extend(Path('.').glob('**/.env.*'))

        # .env.example은 제외
        env_files = [f for f in env_files if '.env.example' not in str(f)]

        if env_files:
            print("❌ 다음 환경 변수 파일들이 발견되었습니다:")
            for f in env_files:
                print(f"   - {f}")
            print("\n⚠️  이 파일들은 절대 Git에 커밋하면 안 됩니다!")
            return False
        else:
            print("✅ 환경 변수 파일 검사 통과\n")
            return True

    def print_report(self):
        """검사 결과 리포트 출력"""
        print("=" * 60)
        print("📊 보안 검사 결과")
        print("=" * 60)
        print(f"검사한 파일: {self.scanned_files}개")
        print(f"발견된 보안 이슈: {len(self.found_issues)}개\n")

        if self.found_issues:
            print("⚠️  발견된 보안 위험:")
            print("-" * 60)

            for issue in self.found_issues:
                print(f"\n📁 파일: {issue['file']}")
                print(f"🔑 유형: {issue['type']}")
                print(f"💾 내용: {issue['match']}")

            print("\n" + "=" * 60)
            print("❌ 보안 검사 실패!")
            print("=" * 60)
            print("\n🔧 해결 방법:")
            print("1. 하드코딩된 비밀키를 제거하세요")
            print("2. 환경 변수(.env)를 사용하세요")
            print("3. 참조: 01_보안_가이드라인.md")
            print()

            return False
        else:
            print("✅ 보안 이슈가 발견되지 않았습니다!")
            print("=" * 60)
            print()
            return True


def main():
    """메인 함수"""
    validator = SecurityValidator()

    # 1. .gitignore 검사
    gitignore_ok = validator.check_gitignore()

    # 2. .env 파일 검사
    env_ok = validator.check_env_files()

    # 3. 전체 파일 스캔
    files_ok = validator.check_all_files()

    # 4. 결과 리포트
    validator.print_report()

    # 모든 검사 통과 여부
    all_passed = gitignore_ok and env_ok and files_ok

    if all_passed:
        print("🎉 모든 보안 검사를 통과했습니다!")
        print("✅ 안전하게 커밋할 수 있습니다.\n")
        return 0
    else:
        print("🚨 보안 검사 실패!")
        print("❌ 위의 문제를 해결한 후 다시 시도하세요.\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
