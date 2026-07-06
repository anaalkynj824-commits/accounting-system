# Quick Start Guide / دليل البدء السريع

## 🚀 بدء سريع / Quick Start

### **الخطوة 1: إنشاء قاعدة البيانات / Create Database**
```bash
python run.py init
```

### **الخطوة 2: تشغيل التطبيق / Run Application**
```bash
python run.py run
```

### **الخطوة 3: افتح المتصفح / Open Browser**
```
http://localhost:5000
```

### **بيانات الدخول / Login Credentials**
```
Username: admin
Password: admin123
```

---

## 📋 أوامر متاحة / Available Commands

### **1. إنشاء قاعدة البيانات مع البيانات التجريبية**
```bash
python run.py init
```
- ✅ ينشئ الجداول (Creates tables)
- ✅ يدرج بيانات تجريبية (Loads sample data)
- ✅ يتحقق من المستخدم admin (Verifies admin user)

### **2. إنشاء قاعدة البيانات فقط (بدون بيانات)**
```bash
python run.py init-only
```
- ✅ ينشئ الجداول فقط
- ❌ لا يدرج بيانات تجريبية

### **3. إعادة إنشاء قاعدة البيانات (قوة)**
```bash
python run.py init --force
```
- ⚠️ يحذف قاعدة البيانات القديمة
- ✅ ينشئ قاعدة جديدة

### **4. التحقق من قاعدة البيانات**
```bash
python run.py verify
```
- ✅ يعرض إحصائيات قاعدة البيانات
- ✅ يتحقق من وجود مستخدم admin
- ✅ يعرض عدد الصفوف في كل جدول

### **5. تشغيل التطبيق**
```bash
python run.py run
```
- 🚀 يشغل خادم Flask
- 📍 الرابط: http://localhost:5000

### **6. عرض المساعدة**
```bash
python run.py help
```

---

## ⚡ أمثلة عملية / Practical Examples

### **مثال 1: البدء الأول**
```bash
# الخطوة 1: إنشاء قاعدة البيانات
python run.py init

# الخطوة 2: التحقق من البيانات
python run.py verify

# الخطوة 3: تشغيل التطبيق
python run.py run
```

### **مثال 2: إعادة تعيين كاملة**
```bash
# حذف وإعادة إنشاء قاعدة البيانات
python run.py init --force

# ثم تشغيل التطبيق
python run.py run
```

### **مثال 3: أمر واحد**
```bash
# إنشاء + التحقق + التشغيل
python run.py init && python run.py verify && python run.py run
```

---

## 🎯 معلومات مهمة / Important Information

### **مسارات الملفات الافتراضية**
```
📂 Project Root
 ├── run.py                           # ملف البدء الرئيسي
 ├── accounting_system.db             # قاعدة البيانات
 ├── database/
 │   ├── sqlite_schema.sql           # هيكل الجداول
 │   └── sample_data.sql             # البيانات التجريبية
 ├── backend/
 │   ├── run.py                      # خادم Flask
 │   ├── requirements.txt             # المكتبات المطلوبة
 │   └── app/
 │       ├── __init__.py
 │       ├── config.py
 │       ├── models/
 │       ├── routes/
 │       └── services/
 └── frontend/
    ├── index.html
    ├── assets/
    │   ├── css/
    │   └── js/
```

### **متطلبات النظام**
- Python 3.8+
- SQLite3 (مدمج في Python)
- Flask (سيتم تثبيته من requirements.txt)

### **المتغيرات البيئية**
```bash
FLASK_ENV=development
FLASK_DEBUG=1
FLASK_APP=run.py
DATABASE_URL=sqlite:///accounting_system.db
```

---

## 🔧 استكشاف الأخطاء / Troubleshooting

### **مشكلة: "ModuleNotFoundError: No module named 'flask'"**
```bash
# الحل: تثبيت المكتبات
cd backend
pip install -r requirements.txt
cd ..
```

### **مشكلة: "Database is locked"**
```bash
# الحل: حذف قاعدة البيانات وإعادة إنشاؤها
python run.py init --force
```

### **مشكلة: "Port 5000 already in use"**
```bash
# الحل: تغيير المنفذ في backend/run.py
app.run(port=5001)  # استخدم منفذ آخر
```

### **مشكلة: "Cannot find database file"**
```bash
# تأكد أنك في المجلد الرئيسي
ls run.py          # يجب أن تراه
python run.py init # ثم حاول مرة أخرى
```

---

## 📊 بيانات النظام / System Data

### **إحصائيات قاعدة البيانات**
```
Total Tables:     17
Total Indexes:    10
Default Users:    1 (admin)
Sample Customers: 5
Sample Suppliers: 3
Sample Products:  5
Sample Invoices:  5
Sample Expenses:  5
Sample Revenues:  3
```

### **بيانات المسؤول**
```
👤 Username:  admin
🔐 Password:  admin123
📧 Email:     admin@accounting-system.local
🎯 Role:      Administrator
```

---

## 🔐 ملاحظات أمنية / Security Notes

⚠️ **قبل الإطلاق في الإنتاج:**

1. **غير كلمة المرور الافتراضية**
   ```bash
   # في لوحة التحكم -> إعدادات -> تغيير كلمة المرور
   ```

2. **استخدم قاعدة بيانات آمنة**
   ```python
   # استخدم PostgreSQL بدلاً من SQLite
   DATABASE_URL = 'postgresql://user:pass@localhost/db'
   ```

3. **عطّل Flask Debug Mode**
   ```bash
   export FLASK_DEBUG=0
   ```

4. **استخدم HTTPS**
   ```python
   # في الإنتاج، استخدم SSL/TLS
   ```

---

## 📞 الدعم / Support

للمزيد من المعلومات:
- 📖 اطلع على [README.md](../README.md)
- 📚 اطلع على [DATABASE.md](DATABASE_SETUP.md)
- 🐛 أبلغ عن المشاكل في GitHub Issues

---

**آخر تحديث / Last Updated:** 2024-01-07
**الإصدار / Version:** 1.0.0