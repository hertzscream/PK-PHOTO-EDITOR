# PK PHOTO EDITOR

Official website and Android APK releases for PK PHOTO EDITOR.

- Website: https://hertzscream.github.io/PK-PHOTO-EDITOR/
- Download: https://github.com/hertzscream/PK-PHOTO-EDITOR/releases/latest
- Android 14 or later (API 34+)
- Current version: 0.2.0 (versionCode 3), testing build signed with the existing debug certificate.

## ใช้งาน

ดาวน์โหลด `PK-PHOTO-EDITOR.apk` จาก Releases แล้วเปิดเพื่อติดตั้ง อนุญาตการติดตั้งจากเบราว์เซอร์เมื่อ Android ขอ หากติดตั้งรุ่น 0.1.x อยู่แล้ว สามารถติดตั้งทับเพื่อเก็บงานเดิมได้ ชื่อแพ็กเกจยังเป็น `com.kee.proshotlocal`

ในแอป: ตั้งค่า → ตรวจสอบอัปเดต → ตรวจสอบเวอร์ชัน → ดาวน์โหลด → อนุญาตแหล่งติดตั้ง → ติดตั้งผ่านหน้าระบบ Android ไม่มีการติดตั้งเงียบ

แอปตรวจ SHA-256, applicationId, versionCode และ signing certificate ก่อนเปิดตัวติดตั้ง การแต่งภาพทำงานบนเครื่อง ไม่มีการส่งรูปไป GitHub

## สิ่งที่มีใน repository นี้

หน้าเว็บ `/docs` และเอกสารเผยแพร่ ส่วน Android source ส่งมอบแยกให้เจ้าของโครงการ ไม่รวมรูปส่วนตัว SDK หรือ private signing key

## เผยแพร่รุ่นถัดไป

1. เพิ่ม versionCode ทุกครั้ง ใช้ signing key เดิม และทดสอบ APK ก่อนเผยแพร่
2. สร้าง GitHub Release ใหม่ tag `vX.Y.Z` แนบ APK ชื่อ `PK-PHOTO-EDITOR.apk`, `update.json` และ `SHA256SUMS.txt`
3. `update.json` ต้องระบุ SHA-256 ของ APK จริงและ URL แบบ tag ที่ไม่เปลี่ยน
4. Publish เป็น release ปกติ เพราะ feed `/releases/latest/download/update.json` ไม่เลือก draft หรือ prerelease
5. ตรวจ URL feed แล้วทดสอบปุ่มตรวจสอบอัปเดตบนเครื่อง Android

โปรดเก็บ signing key ไว้ในที่ปลอดภัยนอก repository การเปลี่ยน key จะอัปเดตทับรุ่นเดิมไม่ได้