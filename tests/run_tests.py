import subprocess
import sys
import os

print("=== апуск тестов ===")

# 1. роверяем импорт
sys.path.insert(0, 'src')
try:
    import masks
    import widget
    import processing
    print("✅ се модули импортируются")
except ImportError as e:
    print(f"❌ шибка импорта: {e}")
    sys.exit(1)

# 2. апускаем тесты через pytest
result = subprocess.run([sys.executable, "-m", "pytest", "tests/", "-v"], 
                       capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)
    
print(f"од возврата: {result.returncode}")
