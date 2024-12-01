import subprocess

def execute_adb_command(command):
    """تنفيذ أمر ADB وإرجاع الناتج."""
    try:
        result = subprocess.run(['adb'] + command, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            raise Exception(result.stderr.strip())
    except Exception as e:
        return f"Error: {e}"

def get_device_info():
    """الحصول على معلومات الجهاز المتصل عبر ADB."""
    return execute_adb_command(['shell', 'getprop'])
