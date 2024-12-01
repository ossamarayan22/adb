import unittest
from adb_utils import execute_adb_command, get_device_info

class TestADBUtils(unittest.TestCase):
    def test_execute_adb_command_success(self):
        # اختبار تنفيذ أمر ADB بنجاح
        result = execute_adb_command(['devices'])
        self.assertIn('List of devices attached', result)  # التأكد من وجود قائمة الأجهزة

    def test_execute_adb_command_failure(self):
        # اختبار تنفيذ أمر ADB مع خطأ
        result = execute_adb_command(['nonexistent_command'])
        self.assertTrue(result.startswith("Error:"))

    def test_get_device_info(self):
        # اختبار استرجاع معلومات الجهاز عبر ADB
        result = get_device_info()
        self.assertTrue(isinstance(result, str))  # التأكد من أن النتيجة هي سلسلة نصية

if __name__ == "__main__":
    unittest.main()
