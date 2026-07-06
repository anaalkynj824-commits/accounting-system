#!/usr/bin/env python3
"""
Accounting System - Database Initialization & Application Runner
نظام محاسبة وإدارة مالية ذكي - واجهة البيانات
"""

import os
import sys
import sqlite3
import argparse
from pathlib import Path
from datetime import datetime

# Color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_header():
    """Print application header"""
    print(f"""
{Colors.BOLD}{Colors.BLUE}
╔═══════════════════════════════════════════════════════════════╗
║   نظام محاسبة وإدارة مالية ذكي                               ║
║   Smart Financial Accounting & Management System               ║
╚═══════════════════════════════════════════════════════════════╝
{Colors.RESET}
    """)

def check_database_exists(db_path):
    """Check if database already exists"""
    return os.path.exists(db_path)

def create_database(db_path, schema_path, sample_data_path=None):
    """Create SQLite database with schema and optional sample data"""
    try:
        print(f"{Colors.BLUE}📊 Creating SQLite Database...{Colors.RESET}")
        
        # Connect to database (creates it if doesn't exist)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Enable foreign keys
        cursor.execute('PRAGMA foreign_keys = ON')
        
        print(f"{Colors.YELLOW}📋 Applying schema...{Colors.RESET}")
        
        # Read and execute schema
        if not os.path.exists(schema_path):
            print(f"{Colors.RED}❌ Schema file not found: {schema_path}{Colors.RESET}")
            return False
        
        with open(schema_path, 'r', encoding='utf-8') as f:
            schema_sql = f.read()
            cursor.executescript(schema_sql)
        
        print(f"{Colors.GREEN}✅ Schema applied successfully!{Colors.RESET}")
        
        # Load sample data if provided and file exists
        if sample_data_path and os.path.exists(sample_data_path):
            print(f"{Colors.YELLOW}📝 Loading sample data...{Colors.RESET}")
            with open(sample_data_path, 'r', encoding='utf-8') as f:
                sample_sql = f.read()
                cursor.executescript(sample_sql)
            print(f"{Colors.GREEN}✅ Sample data loaded successfully!{Colors.RESET}")
        
        conn.commit()
        conn.close()
        
        return True
        
    except sqlite3.Error as e:
        print(f"{Colors.RED}❌ Database Error: {str(e)}{Colors.RESET}")
        return False
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {str(e)}{Colors.RESET}")
        return False

def verify_database(db_path):
    """Verify database integrity and show statistics"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get table count
        cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'")
        table_count = cursor.fetchone()[0]
        
        # Get row counts for main tables
        tables = ['users', 'customers', 'suppliers', 'products', 'invoices', 'expenses', 'revenues', 'accounts']
        
        print(f"{Colors.BLUE}\n📊 Database Statistics:{Colors.RESET}")
        print(f"{Colors.YELLOW}{'Table':<20} {'Rows':<10}{Colors.RESET}")
        print(f"{Colors.YELLOW}{'-'*30}{Colors.RESET}")
        
        total_rows = 0
        for table in tables:
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                count = cursor.fetchone()[0]
                total_rows += count
                status = f"{Colors.GREEN}✅{Colors.RESET}" if count > 0 else f"{Colors.YELLOW}⚠️{Colors.RESET}"
                print(f"{table:<20} {count:<10} {status}")
            except:
                pass
        
        print(f"{Colors.YELLOW}{'-'*30}{Colors.RESET}")
        print(f"{Colors.BOLD}Total Tables: {table_count}{Colors.RESET}")
        print(f"{Colors.BOLD}Total Records: {total_rows}{Colors.RESET}")
        
        # Check admin user
        cursor.execute("SELECT username FROM users WHERE username='admin'")
        admin = cursor.fetchone()
        
        if admin:
            print(f"{Colors.GREEN}\n✅ Admin User Found!{Colors.RESET}")
            print(f"   Username: {Colors.BOLD}admin{Colors.RESET}")
            print(f"   Password: {Colors.BOLD}admin123{Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}\n⚠️  No admin user found{Colors.RESET}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"{Colors.RED}❌ Error verifying database: {str(e)}{Colors.RESET}")
        return False

def init_database(db_path, schema_path, sample_data_path, force=False):
    """Initialize database with optional force flag"""
    print_header()
    
    if check_database_exists(db_path) and not force:
        print(f"{Colors.YELLOW}⚠️  Database already exists: {db_path}{Colors.RESET}")
        response = input(f"{Colors.BOLD}Do you want to recreate it? (yes/no): {Colors.RESET}")
        if response.lower() not in ['yes', 'y']:
            print(f"{Colors.YELLOW}Skipping database creation...{Colors.RESET}")
            return verify_database(db_path)
        else:
            try:
                os.remove(db_path)
                print(f"{Colors.YELLOW}Old database removed.{Colors.RESET}")
            except:
                pass
    
    if create_database(db_path, schema_path, sample_data_path):
        print(f"{Colors.GREEN}\n✅ Database initialized successfully!{Colors.RESET}")
        verify_database(db_path)
        return True
    else:
        return False

def run_application():
    """Run Flask development server"""
    print_header()
    print(f"{Colors.BLUE}🚀 Starting Application...{Colors.RESET}")
    
    try:
        # Check if we're in the right directory
        if not os.path.exists('backend'):
            print(f"{Colors.RED}❌ Error: 'backend' directory not found!{Colors.RESET}")
            print(f"{Colors.YELLOW}Please run this script from the project root directory.{Colors.RESET}")
            return False
        
        os.chdir('backend')
        
        # Set environment variables
        os.environ['FLASK_APP'] = 'run.py'
        os.environ['FLASK_ENV'] = 'development'
        os.environ['FLASK_DEBUG'] = '1'
        
        print(f"{Colors.GREEN}✅ Environment configured{Colors.RESET}")
        print(f"{Colors.BLUE}\n📍 Starting Flask Development Server...{Colors.RESET}")
        print(f"{Colors.YELLOW}http://localhost:5000{Colors.RESET}")
        print(f"{Colors.YELLOW}http://127.0.0.1:5000{Colors.RESET}")
        print(f"{Colors.BOLD}\nPress CTRL+C to stop the server{Colors.RESET}\n")
        
        # Try to import Flask and run
        try:
            from flask import Flask
            os.system('python run.py')
        except ImportError:
            print(f"{Colors.RED}❌ Flask not installed!{Colors.RESET}")
            print(f"{Colors.YELLOW}Please install dependencies: pip install -r requirements.txt{Colors.RESET}")
            return False
            
    except Exception as e:
        print(f"{Colors.RED}❌ Error starting application: {str(e)}{Colors.RESET}")
        return False
    
    return True

def show_help():
    """Show help message"""
    help_text = f"""
{Colors.BOLD}{Colors.BLUE}نظام محاسبة وإدارة مالية ذكي - مساعدة{Colors.RESET}
{Colors.BOLD}Smart Accounting System - Help{Colors.RESET}

{Colors.BOLD}الاستخدام / Usage:{Colors.RESET}
  python run.py [COMMAND] [OPTIONS]

{Colors.BOLD}الأوامر / Commands:{Colors.RESET}
  init      {Colors.YELLOW}Initialize database with schema and sample data{Colors.RESET}
  init-only {Colors.YELLOW}Initialize database without sample data{Colors.RESET}
  verify    {Colors.YELLOW}Verify database integrity{Colors.RESET}
  run       {Colors.YELLOW}Run Flask development server{Colors.RESET}
  help      {Colors.YELLOW}Show this help message{Colors.RESET}

{Colors.BOLD}الخيارات / Options:{Colors.RESET}
  --force   {Colors.YELLOW}Force database recreation (use with init){Colors.RESET}
  --db      {Colors.YELLOW}Custom database path (default: accounting_system.db){Colors.RESET}

{Colors.BOLD}أمثلة / Examples:{Colors.RESET}
  python run.py init              {Colors.YELLOW}# Initialize database with sample data{Colors.RESET}
  python run.py init --force      {Colors.YELLOW}# Force recreate database{Colors.RESET}
  python run.py verify            {Colors.YELLOW}# Check database{Colors.RESET}
  python run.py run               {Colors.YELLOW}# Start Flask server{Colors.RESET}
  python run.py init && python run.py run  {Colors.YELLOW}# Init + Run{Colors.RESET}

{Colors.BOLD}قيم الافتراضية / Default Values:{Colors.RESET}
  Database:     {Colors.YELLOW}accounting_system.db{Colors.RESET}
  Schema:       {Colors.YELLOW}database/sqlite_schema.sql{Colors.RESET}
  Sample Data:  {Colors.YELLOW}database/sample_data.sql{Colors.RESET}
  Port:         {Colors.YELLOW}5000{Colors.RESET}
  Host:         {Colors.YELLOW}localhost{Colors.RESET}

{Colors.BOLD}بيانات المسؤول الافتراضية / Default Admin:{Colors.RESET}
  Username:  {Colors.YELLOW}admin{Colors.RESET}
  Password:  {Colors.YELLOW}admin123{Colors.RESET}
  Email:     {Colors.YELLOW}admin@accounting-system.local{Colors.RESET}
"""
    print(help_text)

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Accounting System - Database & Server Manager',
        add_help=False
    )
    
    parser.add_argument('command', nargs='?', default='init',
                       help='Command to execute (init, verify, run, help)')
    parser.add_argument('--force', action='store_true',
                       help='Force database recreation')
    parser.add_argument('--db', default='accounting_system.db',
                       help='Database path')
    parser.add_argument('--schema', default='database/sqlite_schema.sql',
                       help='Schema file path')
    parser.add_argument('--sample', default='database/sample_data.sql',
                       help='Sample data file path')
    
    args = parser.parse_args()
    
    # Get absolute paths
    root_dir = Path(__file__).parent
    db_path = root_dir / args.db
    schema_path = root_dir / args.schema
    sample_path = root_dir / args.sample
    
    # Execute command
    if args.command == 'init':
        success = init_database(str(db_path), str(schema_path), str(sample_path), args.force)
        sys.exit(0 if success else 1)
    
    elif args.command == 'init-only':
        success = init_database(str(db_path), str(schema_path), None, args.force)
        sys.exit(0 if success else 1)
    
    elif args.command == 'verify':
        print_header()
        success = verify_database(str(db_path))
        sys.exit(0 if success else 1)
    
    elif args.command == 'run':
        success = run_application()
        sys.exit(0 if success else 1)
    
    elif args.command == 'help':
        show_help()
    
    else:
        print(f"{Colors.RED}❌ Unknown command: {args.command}{Colors.RESET}")
        print(f"{Colors.YELLOW}Use 'python run.py help' for available commands{Colors.RESET}")
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}\n⏹️  Application stopped.{Colors.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{Colors.RED}\n❌ Fatal Error: {str(e)}{Colors.RESET}")
        sys.exit(1)