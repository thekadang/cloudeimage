#!/bin/bash
############################################################
# macOS 코드 서명 및 공증 스크립트
#
# 사용법: ./sign_macos.sh [app 번들 경로]
# 예제: ./sign_macos.sh dist/ImageConverter.app
#
# 참조 문서: docs/배포_전략.md
############################################################

set -e  # 에러 발생 시 스크립트 중단

echo "============================================================"
echo "macOS Code Signing and Notarization Script"
echo "============================================================"
echo

# 파일 경로 확인
if [ -z "$1" ]; then
    echo "Error: No file specified"
    echo "Usage: ./sign_macos.sh [app bundle path]"
    exit 1
fi

TARGET_APP="$1"

if [ ! -d "$TARGET_APP" ]; then
    echo "Error: App bundle not found: $TARGET_APP"
    exit 1
fi

echo "Target app: $TARGET_APP"
echo

# TODO: Apple Developer 계정 정보 설정
# APPLE_ID="your-apple-id@example.com"
# TEAM_ID="YOUR_TEAM_ID"
# APP_PASSWORD="your-app-specific-password"

# TODO: 코드 서명 인증서 정보
# SIGNING_IDENTITY="Developer ID Application: Your Name (TEAM_ID)"

# TODO: 공증용 Bundle ID
# BUNDLE_ID="com.yourcompany.imageconverter"

echo "[TODO] Code signing and notarization not yet configured"
echo
echo "Required steps:"
echo "1. Enroll in Apple Developer Program"
echo "2. Create Developer ID Application certificate"
echo "3. Generate app-specific password for notarization"
echo "4. Configure APPLE_ID, TEAM_ID, and APP_PASSWORD"
echo
echo "Signing command:"
echo "  codesign --deep --force --verify --verbose --sign \"IDENTITY\" \"$TARGET_APP\""
echo
echo "Notarization steps:"
echo "  1. Create zip: ditto -c -k --keepParent \"$TARGET_APP\" app.zip"
echo "  2. Upload: xcrun altool --notarize-app --file app.zip ..."
echo "  3. Check status: xcrun altool --notarization-info REQUEST_UUID ..."
echo "  4. Staple: xcrun stapler staple \"$TARGET_APP\""
echo

# TODO: 실제 서명 단계
# echo "Step 1: Code signing..."
# codesign --deep --force --verify --verbose --sign "$SIGNING_IDENTITY" "$TARGET_APP"
#
# if [ $? -ne 0 ]; then
#     echo "Error: Code signing failed"
#     exit 1
# fi
#
# echo "Code signing successful!"
# echo
#
# # TODO: 공증 단계
# echo "Step 2: Creating zip for notarization..."
# ditto -c -k --keepParent "$TARGET_APP" "app.zip"
#
# echo "Step 3: Uploading for notarization..."
# xcrun altool --notarize-app \
#     --primary-bundle-id "$BUNDLE_ID" \
#     --username "$APPLE_ID" \
#     --password "$APP_PASSWORD" \
#     --asc-provider "$TEAM_ID" \
#     --file "app.zip"
#
# echo
# echo "Notarization submitted!"
# echo "Check status with:"
# echo "  xcrun altool --notarization-info REQUEST_UUID --username \"$APPLE_ID\" --password \"$APP_PASSWORD\""
# echo
# echo "Once approved, staple the ticket:"
# echo "  xcrun stapler staple \"$TARGET_APP\""

echo "============================================================"
echo "Code signing script completed (configuration pending)"
echo "============================================================"
exit 0
