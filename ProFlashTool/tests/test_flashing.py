import unittest
from flashing_utils import flash_firmware

class TestFlashingUtils(unittest.TestCase):
    def test_flash_firmware_success(self):
        # اختبار نجاح التفليش
        result = flash_firmware('/path/to/firmware.img', 'device_id')
        self.assertEqual(result, "Flashing successful")

    def test_flash_firmware_failure(self):
        # اختبار فشل التفليش
        result = flash_firmware('/path/to/invalid_firmware.img', 'device_id')
        self.assertTrue(result.startswith("Flashing failed"))

if __name__ == "__main__":
    unittest.main()
