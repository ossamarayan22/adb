import unittest
import tkinter as tk
from gui import AppGUI

class TestAppGUI(unittest.TestCase):
    def setUp(self):
        # إعداد التطبيق قبل كل اختبار
        self.app = AppGUI()

    def test_window_title(self):
        # التأكد من أن العنوان صحيح
        self.assertEqual(self.app.window.title(), "ProFlashTool")

    def test_flash_button(self):
        # التأكد من وجود زر "Flash Device"
        flash_button = self.app.flash_button
        self.assertIsNotNone(flash_button)

if __name__ == "__main__":
    unittest.main()
