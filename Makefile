.PHONY: help build up down logs shell test clean migrate

help:
	@echo "📚 Accounting System - Docker Commands"
	@echo ""
	@echo "🚀 Development:"
	@echo "  make build          - بناء صورة Docker / Build Docker image"
	@echo "  make up             - تشغيل التطبيق / Start application"
	@echo "  make down           - إيقاف التطبيق / Stop application"
	@echo "  make logs           - عرض السجلات / Show logs"
	@echo "  make shell          - فتح shell في التطبيق / Open app shell"
	@echo ""
	@echo "📊 Database:"
	@echo "  make migrate        - تشغيل الترحيل / Run migrations"
	@echo "  make db-shell       - فتح shell قاعدة البيانات / Open DB shell"
	@echo "  make seed           - ملء قاعدة البيانات بالبيانات الأولية / Seed database"
	@echo ""
	@echo "🧪 Testing:"
	@echo "  make test           - تشغيل الاختبارات / Run tests"
	@echo "  make coverage       - تقرير التغطية / Coverage report"
	@echo ""
	@echo "🔧 Maintenance:"
	@echo "  make clean          - تنظيف الملفات المؤقتة / Clean up"
	@echo "  make prod-up        - تشغيل الإنتاج مع Aiven / Start production"
	@echo "  make prod-down      - إيقاف الإنتاج / Stop production"
	@echo ""

# Development
build:
	docker-compose build

up:
	docker-compose up -d
	@echo "✅ التطبيق قيد التشغيل على http://localhost:5000"

down:
	docker-compose down

logs:
	docker-compose logs -f app

shell:
	docker-compose exec app /bin/bash

# Database
migrate:
	docker-compose exec app flask db upgrade

db-shell:
	docker-compose exec postgres psql -U postgres -d accounting_db

seed:
	docker-compose exec app python -c "from app import db; db.create_all(); print('✅ Database seeded')"

# Testing
test:
	docker-compose exec app pytest tests/ -v

coverage:
	docker-compose exec app pytest tests/ --cov=app --cov-report=html

# Production
prod-up:
	docker-compose -f docker-compose.prod.yml up -d

prod-down:
	docker-compose -f docker-compose.prod.yml down

prod-logs:
	docker-compose -f docker-compose.prod.yml logs -f app

# Maintenance
clean:
	docker-compose down -v
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	@echo "✅ تم التنظيف / Cleaned up"

# Utilities
restart:
	docker-compose restart

ps:
	docker-compose ps

pull:
	docker-compose pull

push:
	docker push your-registry/accounting-system:latest

# Development with live reload
dev:
	docker-compose up app

# Build for Vercel
build-vercel:
	pip install -r backend/requirements.txt
	cd backend && flask db upgrade
