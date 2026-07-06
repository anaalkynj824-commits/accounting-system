"""Routes package."""

from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/api/dashboard')
customers_bp = Blueprint('customers', __name__, url_prefix='/api/customers')
suppliers_bp = Blueprint('suppliers', __name__, url_prefix='/api/suppliers')
invoices_bp = Blueprint('invoices', __name__, url_prefix='/api/invoices')
reports_bp = Blueprint('reports', __name__, url_prefix='/api/reports')
ai_bp = Blueprint('ai', __name__, url_prefix='/api/ai')

# Import route handlers
from . import auth, dashboard, customers, suppliers, invoices, reports, ai

__all__ = [
    'auth_bp', 'dashboard_bp', 'customers_bp', 'suppliers_bp',
    'invoices_bp', 'reports_bp', 'ai_bp'
]