"""Flask application factory."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_name='development'):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Load configuration
    if config_name == 'development':
        from .config import DevelopmentConfig
        app.config.from_object(DevelopmentConfig)
    elif config_name == 'production':
        from .config import ProductionConfig
        app.config.from_object(ProductionConfig)
    else:
        from .config import TestingConfig
        app.config.from_object(TestingConfig)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)
    
    # Register blueprints
    with app.app_context():
        from .routes import auth_bp, dashboard_bp, customers_bp, suppliers_bp
        from .routes import invoices_bp, reports_bp, ai_bp
        
        app.register_blueprint(auth_bp)
        app.register_blueprint(dashboard_bp)
        app.register_blueprint(customers_bp)
        app.register_blueprint(suppliers_bp)
        app.register_blueprint(invoices_bp)
        app.register_blueprint(reports_bp)
        app.register_blueprint(ai_bp)
    
    return app