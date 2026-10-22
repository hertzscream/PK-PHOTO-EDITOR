# PK PHOTO EDITOR

Official website and Android APK releases for PK PHOTO EDITOR.

- Website: https://hertzscream.github.io/PK-PHOTO-EDITOR/
- Download: https://github.com/hertzscream/PK-PHOTO-EDITOR/releases/latest
- Android 14 or later (API 34+)
- Current version: 0.5.0 (versionCode 9), testing build signed with the existing debug certificate.

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
## QR ดาวน์โหลด

หน้าเว็บมี QR Code ที่ลิงก์ไปยัง APK ใน latest release โดยตรง พร้อมปุ่มบันทึก QR ภาพ QR ถูกเก็บใน docs/assets/download-qr.png ไม่ใช้บริการ QR ภายนอก เมื่อเปลี่ยน URL ให้สร้างใหม่ด้วย scripts/generate-download-qr.py (qrcode[pil] 8.2 และ zxing-cpp 2.3.0) สคริปต์ตรวจอ่านกลับและขนาดแสดงผลทั้งสองแบบก่อนบันทึก


## 0.4.0
โปรเจกต์แยกชุดรูป ความเข้มโทน 0–200% ใช้เฉพาะภาพ/ที่เลือก/ทั้งโปรเจกต์ จัดลำดับ โทนโปรด แก้ ซ่อน ถังขยะกู้คืน พร้อมโลโก้และฟอนต์เว็บใหม่

พัฒนาโดย prasert sungthonglang รุ่นทดสอบ ยังไม่มีสำรองโปรเจกต์ ห้ามถอนแอปหรือล้างข้อมูลหากต้องการเก็บงาน


0.4.1 เพิ่มชื่อวันที่–เวลาอัตโนมัติและพื้นหลัง/การ์ดโปร่งใสมีมิติ


0.4.2 แสดงภาพย่อในการ์ดโปรเจกต์ และตัวอย่างโทนจริงบนรูปที่เปิดอยู่หรือภาพสาธิตเมื่อยังไม่เปิดรูป


0.5.0 เพิ่มถังขยะสำหรับโปรเจกต์ รูป และโทน พร้อมกู้คืน/ยืนยันลบถาวร และโทนมาตรฐาน12แบบ (10ใหม่+DSLR Café/Sea) หน้าจัดการใช้ภาพสาธิต AI เดียวกันทุกโทน

