-- Insert Default Admin User
-- Username: admin
-- Password: admin123 (hashed with bcrypt)

INSERT OR REPLACE INTO users (id, username, email, password_hash, first_name, last_name, is_active, role_id)
VALUES (
    1,
    'admin',
    'admin@accounting-system.local',
    -- This is the bcrypt hash of 'admin123'
    -- Hash generated with: bcrypt.hashpw(b'admin123', bcrypt.gensalt()).decode()
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5YmMxSUmGEJqq',
    'مدير',
    'النظام',
    1,
    1
);

-- Insert Sample Customers
INSERT OR REPLACE INTO customers (id, name, email, phone, city, country, balance, is_active)
VALUES
(1, 'محمود محمد', 'mahmoud@example.com', '0501234567', 'الرياض', 'السعودية', 15000.00, 1),
(2, 'فاطمة علي', 'fatima@example.com', '0502234567', 'جدة', 'السعودية', 8500.00, 1),
(3, 'أحمد خليل', 'ahmed@example.com', '0503234567', 'الدمام', 'السعودية', 22000.00, 1),
(4, 'سارة عبدالله', 'sarah@example.com', '0504234567', 'مكة', 'السعودية', 5500.00, 1),
(5, 'علي العمري', 'ali@example.com', '0505234567', 'مدينة النور', 'السعودية', 12000.00, 1);

-- Insert Sample Suppliers
INSERT OR REPLACE INTO suppliers (id, name, email, phone, city, country, balance, is_active)
VALUES
(1, 'شركة الواحة', 'oasis@suppliers.com', '0541234567', 'الرياض', 'السعودية', 25000.00, 1),
(2, 'مورد التمور', 'dates@suppliers.com', '0542234567', 'المدينة', 'السعودية', 15000.00, 1),
(3, 'توزيع البيارات', 'spices@suppliers.com', '0543234567', 'جدة', 'السعودية', 18000.00, 1);

-- Insert Sample Products
INSERT OR REPLACE INTO products (id, name, description, category_id, sku, unit_price, quantity_in_stock, is_active)
VALUES
(1, 'الأرز البياض', 'أرز بياض عالي الجودة', 1, 'RICE-001', 50.00, 150, 1),
(2, 'الزيت الطازج', 'زيت طازج بكر 100%', 1, 'OIL-001', 120.00, 75, 1),
(3, 'التمر المجدول', 'تمر مجدول من المدينة', 2, 'DATE-001', 80.00, 200, 1),
(4, 'اللبن البرمرة', 'لبن برمرة فريش', 1, 'MILK-001', 35.00, 300, 1),
(5, 'الخبز الخباز البرعي', 'خبز طازج يومي', 2, 'BREAD-001', 2.50, 1000, 1);

-- Insert Sample Invoices
INSERT OR REPLACE INTO invoices (id, invoice_number, invoice_type, customer_id, issue_date, due_date, total_amount, tax_amount, discount_amount, status, created_by)
VALUES
(1, 'INV-2024-001', 'SALES', 1, '2024-01-15', '2024-02-15', 15000.00, 1500.00, 0, 'PAID', 1),
(2, 'INV-2024-002', 'SALES', 2, '2024-01-14', '2024-02-14', 8500.00, 850.00, 500, 'PENDING', 1),
(3, 'INV-2024-003', 'SALES', 3, '2024-01-13', '2024-02-13', 22000.00, 2200.00, 0, 'PAID', 1),
(4, 'INV-2024-004', 'PURCHASE', NULL, '2024-01-12', '2024-02-12', 25000.00, 2500.00, 1000, 'PAID', 1),
(5, 'INV-2024-005', 'SALES', 4, '2024-01-11', '2024-02-11', 5500.00, 550.00, 0, 'PARTIALLY_PAID', 1);

-- Insert Sample Expense Categories
INSERT OR REPLACE INTO expense_categories (id, name, description)
VALUES
(1, 'رواتب موظفين', 'رواتب الموظفين'),
(2, 'إيجارات', 'تكاليف مباني المكاتب'),
(3, 'مرافق وخدمات', 'شهريات الكهرباء والماء'),
(4, 'مشتريات', 'مبالغ للمشتريات والعمليات'),
(5, 'امور أخرى', 'نفقات متفرقة');

-- Insert Sample Expenses
INSERT OR REPLACE INTO expenses (id, category_id, description, amount, expense_date, payment_method_id, created_by)
VALUES
(1, 1, 'رواتب يناير 2024', 50000.00, '2024-01-31', 3, 1),
(2, 2, 'إيجار المرؤب - يناير', 15000.00, '2024-01-01', 3, 1),
(3, 3, 'فاتورة الكهرباء', 3500.00, '2024-01-25', 3, 1),
(4, 3, 'فاتورة الماه', 2000.00, '2024-01-25', 3, 1),
(5, 5, 'نفقات متفرقة', 5000.00, '2024-01-30', 1, 1);

-- Insert Sample Revenues
INSERT OR REPLACE INTO revenues (id, description, amount, revenue_date, source, created_by)
VALUES
(1, 'بيع منتجات', 25000.00, '2024-01-15', 'بيع مباشر', 1),
(2, 'بيع منتجات', 18000.00, '2024-01-20', 'بيع مباشر', 1),
(3, 'رسوم وخدمات', 5000.00, '2024-01-25', 'رسوم مباثرة', 1);

-- Insert Sample Accounts (Chart of Accounts)
INSERT OR REPLACE INTO accounts (id, account_number, name, type, balance, is_active)
VALUES
(1, '1000', 'النقد بالبنك', 'ASSET', 100000.00, 1),
(2, '1100', 'الذمم المدينة', 'ASSET', 45500.00, 1),
(3, '2000', 'الذمم الدائنة', 'LIABILITY', -25000.00, 1),
(4, '3000', 'رأس المال', 'EQUITY', 120500.00, 1),
(5, '4000', 'إيرادات بيع', 'REVENUE', 48000.00, 1),
(6, '5000', 'مصروفات رواتب', 'EXPENSE', -50000.00, 1),
(7, '5100', 'مصروفات إيجارات', 'EXPENSE', -15000.00, 1);

-- Create an Index for Performance
CREATE INDEX IF NOT EXISTS idx_customer_name ON customers(name);
CREATE INDEX IF NOT EXISTS idx_supplier_name ON suppliers(name);
CREATE INDEX IF NOT EXISTS idx_invoice_status ON invoices(status);
CREATE INDEX IF NOT EXISTS idx_expense_category_date ON expenses(category_id, expense_date);