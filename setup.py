#!/usr/bin/env python
"""
Setup script for Al-Abyaz Django Project
"""
import os
import sys
import subprocess


def run_command(command, description):
    """Run a shell command and print status"""
    print(f"\n{'='*60}")
    print(f"📌 {description}")
    print(f"{'='*60}")
    
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"❌ Error: {description} failed")
        sys.exit(1)
    print(f"✅ {description} completed successfully")


def main():
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║           🌟 Al-Abyaz - Luxury Perfume Store 🌟              ║
    ║                                                              ║
    ║              Django Project Setup Script                     ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    
    print(f"✅ Python version: {sys.version.split()[0]}")
    
    # Install requirements
    run_command("pip install -r requirements.txt", "Installing dependencies")
    
    # Run migrations
    run_command("python manage.py migrate", "Running database migrations")
    
    # Collect static files
    run_command("python manage.py collectstatic --noinput", "Collecting static files")
    
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║              ✅ Setup Completed Successfully!                 ║
    ║                                                              ║
    ║   Next steps:                                                ║
    ║   1. Create admin user: python manage.py createsuperuser     ║
    ║   2. Run server: python manage.py runserver                  ║
    ║   3. Visit: http://127.0.0.1:8000/                           ║
    ║   4. Admin: http://127.0.0.1:8000/admin/                     ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)


if __name__ == '__main__':
    main()
