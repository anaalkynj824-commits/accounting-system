# البناء متعدد المراحل / Multi-stage Build
FROM python:3.9-slim as builder

WORKDIR /app

# تثبيت المكتبات المطلوبة
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# نسخ requirements
COPY backend/requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# المرحلة الإنتاجية / Production Stage
FROM python:3.9-slim

WORKDIR /app

# متغيرات البيئة
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=5000 \
    FLASK_APP=run.py \
    FLASK_ENV=production

# تثبيت الأدوات الأساسية
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    curl \
    && rm -rf /var/lib/apt/lists/*

# نسخ المكتبات من مرحلة البناء
COPY --from=builder /root/.local /root/.local

# تحديث PATH
ENV PATH=/root/.local/bin:$PATH

# نسخ المشروع
COPY backend/ /app/

# إنشاء مستخدم غير جذر / Non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT}/health || exit 1

# تشغيل التطبيق
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120", "--access-logfile", "-", "--error-logfile", "-", "run:app"]
