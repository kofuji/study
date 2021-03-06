#!/usr/bin/env python
import os
import sys
sys.setrecursionlimit(10000) #追記
#maximum recursion depth exceeded while calling a Python object回避用

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manager_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
