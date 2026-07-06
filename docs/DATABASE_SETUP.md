# إعدادات قاعدة البيانات / Database Configuration Guide

## إنشاء قاعدة البيانات SQLite / Create SQLite Database

### الطريقة 1: استخدام سطر الأوامر
```bash
# إنشاء قاعدة البيانات وتطبيق الجداول
sqlite3 accounting_system.db < database/sqlite_schema.sql

# إدراج البيانات التجريبية
sqlite3 accounting_system.db < database/sample_data.sql
```

### الطريقة 2: استخدام Python
```python
import sqlite3

# إنشاء الاتصال وتطبيق الجداول
conn = sqlite3.connect('accounting_system.db')
cursor = conn.cursor()

with open('database/sqlite_schema.sql', 'r', encoding='utf-8') as f:
    cursor.executescript(f.read())

with open('database/sample_data.sql', 'r', encoding='utf-8') as f:
    cursor.executescript(f.read())

conn.commit()
conn.close()
print("✅ Database created successfully!")
```

### الطريقة 3: استخدام Flask Shell
```bash
cd backend
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()

# ثم تحميل البيانات
sqlite3 ../accounting_system.db < ../database/sample_data.sql
```

---

## بيانات المسؤول الافتراضية / Default Admin Credentials

```
Username: admin
Password: admin123
Email: admin@accounting-system.local
Role: Administrator
```

**⚠️ تهم أمني مهم:** غير كلمة السر بعد تسجيل الدخول الأول!

---

## البيانات التجريبية المُرفقة / Sample Data Included

### العملاء (5 عملاء)
- محمود محمد
- فاطمة علي
- أحمد خليل
- سارة عبدالله
- علي العمري

### الموردين (3 موردين)
- شركة الواحة
- مورد التمور
- توزيع البيارات

### المنتجات (5 منتجات)
- الأرز الأبيض
- الزيت الطازج
- التمر المجدول
- اللبن البرمرة
- الخبز

### الفواتير (5 فواتير)
- 3 فواتير مبيعات
- 2 فاتورة شراء

### المصروفات (5 مصروفات)
- رواتب الموظفين: 50,000 ر.س
- إيجارات: 15,000 ر.س
- مرافق: 5,500 ر.س
- متفرقات: 5,000 ر.س

### الإيرادات (3 إيرادات)
- إجمالي الإيرادات: 48,000 ر.س

---

## التحقق من البيانات / Verify Data

```bash
# عرض الجداول
sqlite3 accounting_system.db
sqlite> .tables

# عرض عدد الصفوف في كل جدول
sqlite> SELECT COUNT(*) FROM users;
sqlite> SELECT COUNT(*) FROM customers;
sqlite> SELECT COUNT(*) FROM invoices;

# عرض بيانات المسؤول
sqlite> SELECT * FROM users WHERE username='admin';

# خروج
sqlite> .quit
```

---

## ملاحظات مهمة / Important Notes

1. ✅ كل الجداول لها indexes للأداء العالي
2. ✅ يوجد triggers لتحديث التاريخ تلقائياً
3. ✅ جميع البيانات باللغة العربية والإنجليزية
4. ✅ كلمة المرور محفوظة بصيغة bcrypt آمنة
5. ✅ الفواتير والحسابات متوازنة

---

## ربط قاعدة البيانات بـ Flask / Connect Database to Flask

في ملف `backend/app/config.py`:

```python
import os

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///accounting_system.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

أو استخدم متغير البيئة:

```bash
export DATABASE_URL="sqlite:///accounting_system.db"
```