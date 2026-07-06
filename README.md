# نظام محاسبة وإدارة مالية ذكي
# Smart Financial Accounting & Management System

## 📋 نظرة عامة / Overview

نظام ويب متكامل لإدارة الحسابات المالية للشركات والمحلات التجارية، يتيح تسجيل الإيرادات والمصروفات، وإدارة العملاء والموردين، وإصدار الفواتير، وتحليل البيانات المالية باستخدام الذكاء الاصطناعي.

A comprehensive web system for managing financial accounts for companies and commercial stores, enabling income and expense recording, customer and supplier management, invoice issuance, and financial data analysis using Artificial Intelligence.

---

## 🎯 المميزات الرئيسية / Core Features

### 1. 🔐 نظام المستخدمين / User Management
- مدير النظام (Admin)
- محاسب (Accountant)
- موظف (Employee)
- صلاحيات مختلفة لكل دور

### 2. 📊 لوحة التحكم / Dashboard
- إجمالي الإيرادات والمصروفات
- صافي الربح
- عدد العملاء والموردين
- أحدث الفواتير
- رسوم بيانية توضيحية

### 3. 👥 إدارة العملاء والموردين / Customer & Supplier Management
- إضافة وتعديل العملاء
- إضافة وتعديل الموردين
- متابعة المديونيات
- كشوفات الحساب

### 4. 📄 إدارة الفواتير / Invoice Management
- فواتير البيع
- فواتير الشراء
- مرتجعات البيع والشراء
- QR Code وBarcode للفواتير
- طباعة وتصدير PDF

### 5. 💰 إدارة الإيرادات والمصروفات / Revenue & Expense Management
- تسجيل الإيرادات
- تسجيل المصروفات
- تصنيف المصروفات
- متابعة الأرباح والخسائر

### 6. 📈 التقارير المالية / Financial Reports
- الميزانية العمومية (Balance Sheet)
- قائمة الأرباح والخسائر (P&L)
- التدفقات النقدية (Cash Flow)
- كشف حساب العملاء والموردين
- تقارير شهرية وسنوية

### 7. 🤖 الذكاء الاصطناعي / AI Features
- توقع الأرباح القادمة
- تحليل المصروفات غير الطبيعية
- اكتشاف العمليات المشبوهة
- اقتراح طرق لتقليل المصروفات
- تحليل الأداء المالي
- مساعد ذكي للإجابة على الأسئلة المالية

### 8. 🔔 الإشعارات / Notifications
- موعد استحقاق الفواتير
- انخفاض الرصيد
- تأخر العملاء في السداد
- تنبيهات تجاوز الميزانية

### 9. 📦 ميزات إضافية / Additional Features
- دعم الضرائب (VAT)
- دعم العملات المختلفة
- البحث المتقدم
- تصدير Excel و PDF
- سجل العمليات (Logs)
- Backup تلقائي واستعادة البيانات

---

## 🛠️ التقنيات المستخدمة / Tech Stack

### Frontend
- **HTML5** - الهيكل والمحتوى
- **CSS3** - التصميم والاستجابة
- **JavaScript (Vanilla)** - التفاعلية والديناميكية
- **Chart.js** - الرسوم البيانية
- **DataTables** - جداول البيانات

### Backend
- **Python** - لغة البرمجة الرئيسية
- **Flask** - إطار عمل الويب
- **SQLAlchemy** - ORM لقاعدة البيانات
- **JWT** - المصادقة والتفويض

### Database
- **PostgreSQL** - قاعدة البيانات الرئيسية
- أو **MySQL** - بديل

### AI & ML
- **Scikit-learn** - للتنبؤات والتحليلات
- **Pandas** - معالجة البيانات
- **NumPy** - العمليات الحسابية

### Additional Libraries
- **ReportLab** - إنشاء PDF
- **openpyxl** - تصدير Excel
- **python-qrcode** - توليد QR Codes
- **Flask-Mail** - الإشعارات البريدية

---

## 📁 هيكل المشروع / Project Structure

```
accounting-system/
├── frontend/                    # واجهة المستخدم
│   ├── assets/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── pages/
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── customers.html
│   │   ├── suppliers.html
│   │   ├── invoices.html
│   │   ├── reports.html
│   │   ├── ai.html
│   │   └── settings.html
│   └── index.html
├── backend/                     # الخادم والمنطق
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── customer.py
│   │   │   ├── supplier.py
│   │   │   ├── invoice.py
│   │   │   ├── expense.py
│   │   │   └── account.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── dashboard.py
│   │   │   ├── customers.py
│   │   │   ├── suppliers.py
│   │   │   ├── invoices.py
│   │   │   ├── reports.py
│   │   │   └── ai.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── ai_service.py
│   │   │   ├── report_service.py
│   │   │   ├── invoice_service.py
│   │   │   └── notification_service.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── decorators.py
│   │   │   ├── validators.py
│   │   │   └── helpers.py
│   │   └── templates/
│   ├── migrations/
│   ├── tests/
│   ├── requirements.txt
│   ├── run.py
│   └── config.example.env
├── database/                    # قاعدة البيانات
│   ├── schema.sql
│   ├── migrations/
│   └── seeds/
├── docs/                        # التوثيق
│   ├── API.md
│   ├── DATABASE.md
│   ├── INSTALLATION.md
│   └── USER_GUIDE.md
├── .gitignore
├── README.md
└── LICENSE
```

---

## 🗄️ جداول قاعدة البيانات / Database Tables

### جداول المستخدمين
- **users** - بيانات المستخدمين
- **roles** - الأدوار والصلاحيات
- **role_permissions** - ربط الأدوار بالصلاحيات

### جداول المبيعات والشراء
- **customers** - بيانات العملاء
- **suppliers** - بيانات الموردين
- **invoices** - الفواتير
- **invoice_items** - بنود الفواتير
- **purchases** - المشتريات
- **purchase_items** - بنود المشتريات

### جداول المنتجات
- **products** - المنتجات
- **categories** - تصنيفات المنتجات
- **product_prices** - أسعار المنتجات

### جداول الحسابات المالية
- **accounts** - دليل الحسابات
- **journal_entries** - قيود اليوميات
- **account_balances** - أرصدة الحسابات

### جداول الإيرادات والمصروفات
- **revenues** - الإيرادات
- **expenses** - المصروفات
- **expense_categories** - تصنيفات المصروفات

### جداول الدفع
- **payments** - السدادات
- **payment_methods** - طرق الدفع

### جداول الإشعارات والسجلات
- **notifications** - الإشعارات
- **audit_logs** - سجل العمليات

### جداول الذكاء الاصطناعي
- **ai_reports** - التقارير الذكية
- **ai_predictions** - التنبؤات
- **ai_recommendations** - التوصيات

---

## 🚀 البدء السريع / Quick Start

### المتطلبات / Requirements
- Python 3.8+
- PostgreSQL 12+
- Node.js (optional for frontend tools)

### التثبيت / Installation

1. **استنساخ المستودع / Clone the repository**
```bash
git clone https://github.com/anaalkynj824-commits/accounting-system.git
cd accounting-system
```

2. **إنشاء بيئة افتراضية / Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **تثبيت المكتبات / Install dependencies**
```bash
cd backend
pip install -r requirements.txt
```

4. **إنشاء قاعدة البيانات / Setup database**
```bash
# Create database
psql -U postgres -c "CREATE DATABASE accounting_system;"

# Run migrations
flask db upgrade
```

5. **تشغيل الخادم / Run the server**
```bash
python run.py
```

سيكون التطبيق متاحاً على `http://localhost:5000`

---

## 📖 التوثيق / Documentation

- [دليل التثبيت / Installation Guide](docs/INSTALLATION.md)
- [توثيق API / API Documentation](docs/API.md)
- [هيكل قاعدة البيانات / Database Schema](docs/DATABASE.md)
- [دليل المستخدم / User Guide](docs/USER_GUIDE.md)

---

## 🧪 الاختبار / Testing

```bash
cd backend
pytest tests/
```

---

## 📝 الترخيص / License

هذا المشروع مرخص تحت [MIT License](LICENSE)

---

## 👨‍💻 المساهمة / Contributing

نرحب بمساهماتك! يرجى:

1. Fork المستودع
2. إنشاء branch للميزة الجديدة (`git checkout -b feature/amazing-feature`)
3. Commit التغييرات (`git commit -m 'Add amazing feature'`)
4. Push إلى branch (`git push origin feature/amazing-feature`)
5. فتح Pull Request

---

## 📧 التواصل / Contact

للأسئلة والاستفسارات، يرجى فتح Issue في المستودع.

---

**Made with ❤️ by anaalkynj824-commits**