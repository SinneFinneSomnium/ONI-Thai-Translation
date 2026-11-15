# ONI Thai Translation · มอดภาษาไทยสำหรับ Oxygen Not Included

มอดแปลภาษาไทยสำหรับ **Oxygen Not Included** (เกมหลัก + DLC ทั้งหมดที่อยู่ในไฟล์ข้อความของเกม)
แปลใหม่ทั้งหมดจากไฟล์ `strings_template.pot` ของเกมเวอร์ชันปัจจุบัน ใช้ภาษาที่มีชีวิตชีวา มีมุกในคำบรรยาย แต่ข้อความกลไกเกมยังอ่านเข้าใจง่าย

> ⚠️ **สถานะ: กำลังแปล (ยังไม่ครบ)** — ข้อความที่ยังไม่แปลจะแสดงเป็นภาษาอังกฤษตามปกติ
> ดูความคืบหน้าล่าสุดได้จากหัวข้อ [ความคืบหน้า](#ความคืบหน้า)

## ติดตั้ง

1. ดาวน์โหลดโฟลเดอร์ [`mod/ThaiTranslation`](mod/ThaiTranslation)
2. วางไว้ที่ `Documents\Klei\OxygenNotIncluded\mods\Local\ThaiTranslation`
3. เปิดเกม → **Mods** → เปิดใช้ *ภาษาไทย | Thai Translation*
4. ไปที่ **Translations / แปลภาษา** ในเมนูหลัก แล้วเลือกมอดนี้ จากนั้นรีสตาร์ตเกม

## ฟอนต์ภาษาไทย

ไฟล์ `strings.po` ระบุ `Font: NotoSansThai-Regular` ในส่วนหัว ตามวิธีที่ Klei อธิบายไว้ใน
[Creating/Using Translation Files](https://forums.kleientertainment.com/topic/74765-creatingusing-translation-files/)
และชื่อฟอนต์นี้มีอยู่ในโค้ดของเกมเวอร์ชันปัจจุบัน

ข้อจำกัดที่รู้อยู่ (ต้องทดสอบในเกม):
- สระบน/วรรณยุกต์อาจซ้อนกันไม่สวยในบางคำ เพราะระบบตัวอักษรของเกม (TextMeshPro) ไม่ได้จัดตำแหน่งอักษรไทยแบบเต็มรูปแบบ
- ภาษาไทยไม่มีช่องว่างระหว่างคำ สคริปต์สร้างไฟล์จึงแทรกอักขระ zero-width space (U+200B) ระหว่างคำ ด้วย [PyThaiNLP](https://github.com/PyThaiNLP/pythainlp) เพื่อช่วยให้ตัดบรรทัดได้

## โครงสร้าง repo

| path | คืออะไร |
|---|---|
| `mod/ThaiTranslation/` | ตัวมอดพร้อมใช้ (`strings.po`, `mod.yaml`, `mod_info.yaml`) |
| `tr/*.tsv` | คำแปลต้นฉบับ: `ลำดับ<TAB>คำแปล` (ใช้ `\n` แทนขึ้นบรรทัดใหม่) |
| `src/uniq.json` | รายการข้อความอังกฤษที่ไม่ซ้ำกัน เรียงตามลำดับความสำคัญ (ลำดับไม่เปลี่ยน ข้อความใหม่ต่อท้าย) |
| `glossary.md` | อภิธานศัพท์ ให้ศัพท์ตรงกันทั้งเกม |
| `tools/` | สคริปต์ดึงข้อความ ตรวจแท็ก และสร้างไฟล์ `.po` |

## สร้าง strings.po ใหม่ / อัปเดตตามเกม

```bash
pip install polib pythainlp
# คัดลอก strings_template.pot จาก
#   <ที่ติดตั้งเกม>/OxygenNotIncluded_Data/StreamingAssets/strings/
# มาไว้ที่ src/strings_template.pot (ไฟล์นี้เป็นของ Klei จึงไม่ได้ใส่ไว้ใน repo)
python3 tools/extract.py src/strings_template.pot src/uniq.json   # เพิ่มข้อความใหม่ต่อท้าย
python3 tools/check.py    # ตรวจว่าแท็ก <...> และ {0} ตรงกับต้นฉบับ
python3 tools/build.py    # สร้าง mod/ThaiTranslation/strings.po
```

## ความคืบหน้า

ดูจากผลของ `python3 tools/check.py` (บรรทัด `translated X/Y`)

## เครดิตและสิทธิ์

- เกมและข้อความต้นฉบับภาษาอังกฤษ © Klei Entertainment
- คำแปลในมอดนี้แปลขึ้นใหม่ ไม่ได้นำมาจากมอดแปลไทยตัวอื่น
- ข้อมูลรูปแบบ `mod_info.yaml`: [Klei forum – Setting up mod_info.yaml](https://forums.kleientertainment.com/forums/topic/158363-setting-up-mod_infoyaml-and-archived_versions/)
