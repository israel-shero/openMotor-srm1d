import unittest

import motorlib.motor
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication, QDialogButtonBox, QFormLayout, QWidget,
)

import srm_1d.srm1d_plugin  # noqa: F401
from uilib.preferencesManager import Preferences
from uilib.widgets.motorEditor import MotorEditor
from uilib.widgets.preferencesMenu import PreferencesMenu


class TestConfigEditorLayout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])
        cls.app.icon = QIcon()
        cls.app.isDarkMode = lambda: False

    def test_motor_config_keeps_actions_visible_and_fields_wrapped(self):
        parent = QWidget()
        editor = MotorEditor(parent)
        editor.setPreferences(Preferences())
        editor.resize(240, 320)
        editor.loadMotorConfig(
            motorlib.motor.Motor(), 'srm_1d-transient', [])
        parent.show()
        editor.show()
        self.app.processEvents()

        self.assertEqual(
            editor.form.rowWrapPolicy(),
            QFormLayout.RowWrapPolicy.WrapLongRows,
        )
        self.assertGreater(
            editor.editorScroll.verticalScrollBar().maximum(), 0)
        self.assertEqual(
            editor.editorScroll.horizontalScrollBar().maximum(), 0)
        for row in range(editor.form.rowCount()):
            field = editor.form.itemAt(
                row, QFormLayout.ItemRole.FieldRole)
            if field is not None and field.widget() is not None:
                rect = field.widget().geometry()
                self.assertGreaterEqual(rect.left(), 0)
                self.assertLessEqual(
                    rect.right(), editor.editorContent.width())
        self.assertTrue(editor.applyButton.isVisible())
        self.assertTrue(editor.cancelButton.isVisible())
        self.assertLessEqual(
            editor.applyButton.geometry().bottom(), editor.height())
        self.assertLessEqual(
            editor.cancelButton.geometry().bottom(), editor.height())
        self.assertGreater(
            editor.applyButton.geometry().top(),
            editor.editorScroll.geometry().top(),
        )

        applied = []
        editor.motorConfigApplied.connect(
            lambda *args: applied.append(args))
        editor.applyButton.click()
        self.assertEqual(len(applied), 1)

        editor.close()
        parent.close()

    def test_preferences_accept_controls_stay_outside_scrolling_form(self):
        menu = PreferencesMenu()
        menu.load(Preferences())
        menu.resize(320, 350)
        menu.show()
        self.app.processEvents()

        self.assertTrue(menu.ui.buttonBox.isVisible())
        self.assertIsNotNone(menu.ui.settingsEditorGeneral.scrollArea)
        self.assertGreater(
            menu.ui.settingsEditorGeneral.scrollArea
            .verticalScrollBar().maximum(),
            0,
        )
        self.assertEqual(
            menu.ui.settingsEditorGeneral.scrollArea
            .horizontalScrollBar().maximum(),
            0,
        )
        self.assertLessEqual(
            menu.ui.buttonBox.geometry().bottom(), menu.height())

        accepted = []
        menu.preferencesApplied.connect(accepted.append)
        menu.ui.buttonBox.button(
            QDialogButtonBox.StandardButton.Ok).click()
        self.assertEqual(len(accepted), 1)
        self.assertFalse(menu.isVisible())

        menu.close()


if __name__ == '__main__':
    unittest.main()
