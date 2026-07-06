# 🐳 Docker Setup Guide - نظام المحاسبة

دليل شامل لنشر نظام المحاسبة باستخدام Docker مع دعم Vercel و Aiven.io

---

## 📋 المتطلبات / Requirements

- **Docker** 20.10+
- **Docker Compose** 2.0+
- **Aiven PostgreSQL** (اختياري للإنتاج)
- **Git** (لاستنساخ المشروع)

---

## 🚀 البدء السريع / Quick Start

### 1️⃣ التطوير المحلي / Local Development

```bash
# 1. استنساخ المستودع
git clone https://github.com/anaalkynj824-commits/accounting-system.git
cd accounting-system

# 2. إعداد متغيرات البيئة
cp .env.example .env

# 3. بناء وتشغيل التطبيق
make build
make up

# 4. تشغيل الترحيلات
make migrate

# تم! التطبيق متاح على http://localhost:5000 ✅
```

---

## 🔧 إعداد Aiven PostgreSQL

### أ. إنشاء Aiven Account

1. اذهب إلى https://aiven.io
2. أنشئ حساباً مجانياً
3. انقر على "Create Service"
4. اختر **PostgreSQL**
5. اختر المنطقة والحجم (Free tier متاح)

### ب. الحصول على بيانات الاتصال

في لوحة Aiven:
1. افتح خدمتك PostgreSQL
2. اذهب إلى "Connection Info"
3. انسخ بيانات الاتصال:
   - **Host**: `your-instance.c.aivencloud.com`
   - **Port**: `5432`
   - **User**: `avnadmin`
   - **Password**: كلمة المرور التي وضعتها
   - **Database**: `defaultdb`

### ج. تحديث ملف .env

```env
# استخدم بيانات Aiven
AIVEN_HOST=your-instance.c.aivencloud.com
AIVEN_PORT=5432
AIVEN_USER=avnadmin
AIVEN_PASSWORD=your-password
AIVEN_DB=defaultdb

# أو استخدم DATABASE_URL مباشرة:
DATABASE_URL=postgresql://avnadmin:password@your-instance.c.aivencloud.com:5432/defaultdb?sslmode=require
```

---

## 📊 البيئات المختلفة / Environments

### ⚙️ التطوير (Development)

```bash
# استخدام قاعدة بيانات محلية PostgreSQL
docker-compose up

# الأوامر المفيدة:
make logs       # عرض ��لسجلات
make shell      # فتح terminal في التطبيق
make db-shell   # الاتصال بقاعدة البيانات
```

### 🏭 الإنتاج مع Aiven (Production)

```bash
# استخدام Aiven PostgreSQL
make prod-up

# أو يدوياً:
docker-compose -f docker-compose.prod.yml up -d

# مراقبة السجلات:
make prod-logs
```

---

## 🌐 النشر على Vercel

### 1️⃣ إعداد Vercel

```bash
# تثبيت Vercel CLI
npm i -g vercel

# تسجيل الدخول
vercel login

# النشر
vercel --prod
```

### 2️⃣ إعداد متغيرات البيئة على Vercel

في لوحة Vercel:
1. اذهب إلى Project Settings
2. اختر "Environment Variables"
3. أضف:
   ```
   DATABASE_URL=postgresql://avnadmin:password@your-instance.c.aivencloud.com:5432/defaultdb?sslmode=require
   SECRET_KEY=your-secret-key
   JWT_SECRET_KEY=your-jwt-secret
   AIVEN_HOST=your-instance.c.aivencloud.com
   AIVEN_USER=avnadmin
   AIVEN_PASSWORD=your-password
   AIVEN_DB=defaultdb
   ```

### 3️⃣ تشغيل الترحيلات

```bash
# قبل الوصول للتطبيق، شغل الترحيلات:
vercel env pull     # سحب المتغيرات
cd backend
flask db upgrade    # تشغيل الت��حيلات
```

---

## 🏗️ البناء والنشر

### بناء صورة Docker

```bash
# بناء الصورة
docker build -t accounting-system:latest .

# بناء مع tag مخصص
docker build -t your-registry/accounting-system:v1.0 .
```

### دفع إلى Docker Registry

```bash
# تسجيل الدخول
docker login

# دفع الصورة
docker push your-registry/accounting-system:latest
```

### النشر على خادم

```bash
# على خادم بـ Docker Compose
docker pull your-registry/accounting-system:latest
docker-compose up -d

# أو استخدام docker-compose.prod.yml
docker-compose -f docker-compose.prod.yml up -d
```

---

## 🛠️ أوامر مفيدة

### التطوير

```bash
make build              # بناء الصورة
make up                 # تشغيل التطبيق
make down               # إيقاف التطبيق
make logs               # عرض السجلات
make shell              # فتح shell
make clean              # تنظيف الملفات المؤقتة
make restart            # إعادة تشغيل
```

### قاعدة البيانات

```bash
make migrate            # تشغيل الترحيلات
make db-shell           # الاتصال بقاعدة البيا��ات
make seed               # ملء البيانات الأولية
```

### الاختبار

```bash
make test               # تشغيل الاختبارات
make coverage           # تقرير التغطية
```

### الإنتاج

```bash
make prod-up            # تشغيل الإنتاج
make prod-down          # إيقاف الإنتاج
make prod-logs          # سجلات الإنتاج
```

---

## 🔍 استكشاف الأخطاء

### المشكلة: "Cannot connect to database"

```bash
# تحقق من الاتصال
docker-compose exec app flask shell
>>> from app import db
>>> db.engine.execute("SELECT 1")
```

### المشكلة: Port already in use

```bash
# تغيير المنفذ في docker-compose.yml
ports:
  - "5001:5000"  # استخدام 5001 بدلاً من 5000
```

### المشكلة: Aiven SSL connection error

```bash
# تأكد من إضافة ?sslmode=require في DATABASE_URL
DATABASE_URL=postgresql://...?sslmode=require
```

### مسح كل شيء والبدء من جديد

```bash
make clean
make build
make up
make migrate
```

---

## 📈 مراقبة الأداء

### استخدام Docker Stats

```bash
docker stats
```

### عرض السجلات

```bash
docker-compose logs -f app
docker-compose logs -f postgres
```

### Backup قاعدة البيانات

```bash
# من قاعدة البيانات المحلية
docker-compose exec postgres pg_dump -U postgres accounting_db > backup.sql

# من Aiven
pg_dump "postgresql://user:pass@host:5432/db" > backup.sql
```

---

## 🔐 الأمان

### نقاط مهمة:

1. **لا تستخدم الكلمات السرية الافتراضية في الإنتاج**
   ```bash
   # في .env (الإنتاج):
   SECRET_KEY=generate-strong-random-key-here
   JWT_SECRET_KEY=another-strong-random-key
   POSTGRES_PASSWORD=very-strong-password
   REDIS_PASSWORD=very-strong-password
   ```

2. **استخدم SSL/TLS مع Aiven**
   ```
   DATABASE_URL=postgresql://...?sslmode=require
   ```

3. **قيود الوصول (Firewall)**
   - في Aiven: حدد IPs المسموح بها
   - في Nginx: استخدم rate limiting

4. **متغيرات البيئة الحساسة**
   ```bash
   # لا تضعها في git
   echo ".env" >> .gitignore
   ```

---

## 📚 مراجع إضافية

- [Docker Documentation](https://docs.docker.com)
- [Docker Compose Reference](https://docs.docker.com/compose/compose-file/)
- [Aiven PostgreSQL](https://docs.aiven.io/docs/products/postgresql)
- [Vercel Python Support](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python)
- [Flask Deployment](https://flask.palletsprojects.com/deployment/)

---

## 🤝 الدعم

للمساعدة والاستفسارات:
- 📧 فتح Issue على GitHub
- 💬 المناقشات في المستودع
- 📖 راجع التوثيق الكاملة

---

**Made with ❤️ for accounting-system**
