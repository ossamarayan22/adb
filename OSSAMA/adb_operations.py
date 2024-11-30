import subprocess

def run_adb_command(command):
    """Run an ADB command and return the output."""
    try:
        result = subprocess.run(['adb'] + command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.stderr:
            raise Exception(result.stderr)
        return result.stdout
    except Exception as e:
        return f"Error: {str(e)}"

def get_devices():
    """Get the list of connected devices."""
    output = run_adb_command("devices")
    devices = [line.split()[0] for line in output.splitlines() if line.endswith("device")]
    return devices

def get_accounts():
    """Extract Google account emails from the device."""
    output = run_adb_command("shell dumpsys account")
    accounts = [line.strip() for line in output.split("\n") if "name=" in line]
    return accounts

def get_phone_number():
    """Extract phone number from the device."""
    output = run_adb_command("shell service call iphonesubinfo 1")
    return output
