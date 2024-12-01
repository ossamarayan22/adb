import os
import subprocess

def flash_firmware(firmware_path, device_id):
    """تفليش الروم إلى الجهاز."""
    command = ['adb', '-s', device_id, 'push', firmware_path, '/data/local/tmp/firmware.img']
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        return "Flashing successful"
    else:
        return f"Flashing failed: {result.stderr}"
