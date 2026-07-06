# دليل التثبيت / Installation Guide

## المتطلبات / Requirements

### البرامج المطلوبة
- Python 3.8 أو أحدث
- PostgreSQL 12+ أو MySQL 5.7+
- Node.js 14+ (اختياري)
- Git

### البيئة
- نظام تشغيل: Windows, macOS, أو Linux
- المتصفح: Chrome, Firefox, Safari, أو Edge (آخر إصدار)

## خطوات التثبيت

### 1. استنساخ المستودع
```bash
git clone https://github.com/anaalkynj824-commits/accounting-system.git
cd accounting-system
```

### 2. إنشاء البيئة الافتراضية

#### على Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### على macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. تثبيت المكتبات
```bash
cd backend
pip install -r requirements.txt
```

### 4. إعداد قاعدة البيانات

#### إنشاء قاعدة البيانات

**PostgreSQL:**
```sql
createdb accounting_system
```

**MySQL:**
```sql
mysql -u root -p
CREATE DATABASE accounting_system;
```

#### تنفيذ Schema
```bash
# PostgreSQL
psql -U postgres -d accounting_system -f ../database/schema.sql

# MySQL
mysql -u root -p accounting_system < ../database/schema.sql
```

### 5. تكوين متغيرات البيئة

أنشئ ملف `.env` في مجلد `backend`:
```env
FLASK_ENV=development
FLASK_DEBUG=True

DATABASE_URL=postgresql://user:password@localhost:5432/accounting_system
# أو للـ MySQL
# DATABASE_URL=mysql://user:password@localhost:3306/accounting_system

JWT_SECRET_KEY=your-secret-key-here-change-in-production

MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_DEFAULT_SENDER=noreply@accounting.local
```

### 6. تشغيل التطبيق

#### تشغيل خادم Flask
```bash
python run.py
```

سيكون التطبيق متاحاً على `http://localhost:5000`

#### تشغيل خادم التطوير (مع Hot Reload)
```bash
flask run --reload
```

## بيانات تجريبية / Sample Data

للبدء السريع، يمكنك تحميل بيانات تجريبية:

```bash
python -m flask db seed
```

## المستخدم الافتراضي / Default User

بعد التثبيت، يمكنك تسجيل الدخول بـ:

- **Username:** admin
- **Password:** admin123

⚠️ **تغيير كلمة السر** بعد تسجيل الدخول الأول!

## استكشاف الأخطاء

### خطأ: Database connection refused

**الحل:**
1. تأكد من تشغيل قاعدة البيانات
2. تحقق من بيانات الاتصال في `.env`
3. تأكد من إنشاء قاعدة البيانات

### خطأ: Module not found

**الحل:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### خطأ: JWT_SECRET_KEY not set

**الحل:**
أضف `JWT_SECRET_KEY` في ملف `.env`

## الخطوات التالية

بعد التثبيت الناجح:
1. اقرأ [دليل المستخدم](USER_GUIDE.md)
2. اطلع على [توثيق API](API.md)
3. استكشف [هيكل قاعدة البيانات](DATABASE.md)