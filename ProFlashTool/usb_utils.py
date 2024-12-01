import subprocess

def enable_usb_debugging(device_id):
    """تمكين تصحيح USB على الجهاز عبر ADB."""
    command = ['adb', '-s', device_id, 'shell', 'settings', 'put', 'global', 'adb_enabled', '1']
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        return "USB debugging enabled"
    else:
        return f"Failed to enable USB debugging: {result.stderr}"
