import subprocess

def bypass_frp(device_id):
    """تجاوز FRP على الجهاز باستخدام ADB."""
    command = ['adb', '-s', device_id, 'shell', 'am', 'broadcast', '-a', 'com.google.android.intent.action.MASTER_CLEAR']
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        return "FRP bypassed successfully"
    else:
        return f"Failed to bypass FRP: {result.stderr}"
