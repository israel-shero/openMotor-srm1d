import unittest
import motorlib.propellant
from uilib.defaults import DEFAULT_PROPELLANTS, SRM1D_REPOSITORY_PROPELLANTS
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QSizePolicy
from uilib.preferencesManager import Preferences
from uilib.widgets.propellantMenu import PropellantMenu
from uilib.widgets.propertyEditor import PropertyEditor


class _UnitPreferences:
    def getUnit(self, unit):
        return unit


class TestPropellantEditorLayout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])
        cls.app.icon = QIcon()

    def test_tabular_propellant_editor_keeps_controls_visible(self):
        propellant = motorlib.propellant.Propellant({
            'name': 'Layout Test',
            'density': 1700,
            'tabs': [{
                'minPressure': 0,
                'maxPressure': 7000000,
                'a': 1e-5,
                'n': 0.3,
                'k': 1.2,
                't': 2800,
                'm': 23.67,
            }],
        })

        prop = propellant.props['tabs']
        parent = QWidget()
        editor = PropertyEditor(parent, prop, _UnitPreferences())

        self.assertGreaterEqual(editor.editor.minimumWidth(), 520)
        self.assertGreaterEqual(editor.editor.minimumHeight(), 300)
        self.assertEqual(
            editor.editor.sizePolicy().horizontalPolicy(),
            QSizePolicy.Policy.Expanding,
        )

    def test_dialog_adapts_at_compact_and_standard_sizes(self):
        class Manager:
            propellants = [motorlib.propellant.Propellant({
                'name': 'Layout Test',
                'density': 1700,
                'tabs': [{
                    'minPressure': 0,
                    'maxPressure': 7000000,
                    'a': 1e-5,
                    'n': 0.3,
                    'k': 1.2,
                    't': 2800,
                    'm': 23.67,
                }],
            })]

            def getNames(self):
                return [prop.getProperty('name') for prop in self.propellants]

            def savePropellants(self):
                pass

        menu = PropellantMenu(Manager())
        menu.ui.propEditor.setPreferences(Preferences())
        menu.ui.listWidgetPropellants.setCurrentRow(0)
        menu.editProp()

        menu.resize(850, 700)
        menu.show()
        self.app.processEvents()
        self.assertEqual(menu.size().width(), 850)
        self.assertFalse(menu.ui.listWidgetPropellants.isVisible())
        self.assertFalse(menu.ui.propEditor.propellantPreview.isVisible())
        self.assertGreater(menu.ui.propEditor.width(), 700)
        self.assertIsNotNone(menu.ui.propEditor.scrollArea.widget())

        menu.resize(700, 600)
        self.app.processEvents()
        self.assertEqual(menu.size().width(), 700)
        self.assertGreater(
            menu.ui.propEditor.scrollArea.verticalScrollBar().maximum(),
            0,
        )
        self.assertEqual(
            menu.ui.propEditor.scrollArea.horizontalScrollBar().maximum(),
            0,
        )

        menu.resize(600, 500)
        self.app.processEvents()
        self.assertEqual(menu.size().width(), 600)
        self.assertFalse(menu.ui.listWidgetPropellants.isVisible())
        self.assertTrue(menu.ui.propEditor.applyButton.isVisible())
        self.assertTrue(menu.ui.propEditor.cancelButton.isVisible())
        self.assertEqual(
            menu.ui.propEditor.scrollArea.horizontalScrollBar().maximum(),
            0,
        )

        menu.resize(1100, 800)
        self.app.processEvents()
        self.assertTrue(menu.ui.listWidgetPropellants.isVisible())
        self.assertTrue(menu.ui.propEditor.propellantPreview.isVisible())

        menu.editingPropellant = False
        menu.close()


class TestRepositoryPropellantLibrary(unittest.TestCase):
    def test_repository_propellants_are_available_as_defaults(self):
        names = {prop['name'] for prop in DEFAULT_PROPELLANTS}
        for prop in SRM1D_REPOSITORY_PROPELLANTS:
            self.assertIn(prop['name'], names)
            self.assertGreater(prop['density'], 0)
            self.assertTrue(prop['tabs'])
            for tab in prop['tabs']:
                self.assertGreaterEqual(tab['maxPressure'], tab['minPressure'])
                self.assertGreater(tab['a'], 0)
                self.assertGreater(tab['k'], 1)
                self.assertGreater(tab['t'], 0)
                self.assertGreater(tab['m'], 0)

    def test_repository_library_has_expected_characterized_entries(self):
        names = {prop['name'] for prop in SRM1D_REPOSITORY_PROPELLANTS}
        self.assertIn('Hasegawa A Prop', names)
        self.assertIn('Chase - Energy', names)
        self.assertIn('Risky Batman V3 Jan2024 (LHS-calibrated)', names)

class TestPropellantMethods(unittest.TestCase):
    def test_proper_propellant_ranges(self):
        props = {
            'name': 'TestProp',
            'density': 1650,
            'tabs': [
                {
                    'minPressure': 0,
                    'maxPressure': 6.895e+06,
                    'a': 1.467e-05,
                    'n': 0.382,
                    't': 3500,
                    'm': 23.67,
                    'k': 1.25
                }
            ]
        }
        testProp = motorlib.propellant.Propellant(props)
        self.assertEqual(len(testProp.getErrors()), 0)

    def test_backwards_pressure_ranges(self):
        props = {
            'name': 'TestProp',
            'density': 1650,
            'tabs': [
                {
                    'minPressure': 6.895e+06,
                    'maxPressure': 0,
                    'a': 1.467e-05,
                    'n': 0.382,
                    't': 3500,
                    'm': 23.67,
                    'k': 1.25
                }, {
                    'minPressure': 6.895e+06,
                    'maxPressure': 1.379e+07,
                    'a': 1.467e-05,
                    'n': 0.382,
                    't': 3500,
                    'm': 23.67,
                    'k': 1.25
                }
            ]
        }
        testProp = motorlib.propellant.Propellant(props)
        self.assertIn('Tab #1 has reversed pressure limits.', [err.description for err in testProp.getErrors()])

    def test_overlapping_pressure_ranges(self):
        props = {
            'name': 'TestProp',
            'density': 1650,
            'tabs': [
                {      
                    'minPressure': 0,
                    'maxPressure': 6.895e+06,
                    'a': 1.467e-05,
                    'n': 0.382,
                    't': 3500,
                    'm': 23.67,
                    'k': 1.25
                }, {
                    'minPressure': 6e+06,
                    'maxPressure': 1.379e+07,
                    'a': 1.467e-05,
                    'n': 0.382,
                    't': 3500,
                    'm': 23.67,
                    'k': 1.25
                }
            ]
        }
        testProp = motorlib.propellant.Propellant(props)
        self.assertIn('Tabs #1 and #2 have overlapping ranges.', [err.description for err in testProp.getErrors()])

    def test_get_combustion_properties_in_range(self):
        props = {
            'name': 'TestProp',
            'density': 1650,
            'tabs': [
                {
                    'minPressure': 0,
                    'maxPressure': 6.895e+06,
                    'a': 1.467e-05,
                    'n': 0.382,
                    't': 3500,
                    'm': 23.67,
                    'k': 1.25
                }, {
                    'minPressure': 6.895e+06,
                    'maxPressure': 1.379e+07,
                    'a': 1e-05,
                    'n': 0.3,
                    't': 3500,
                    'm': 23.67,
                    'k': 1.25
                }
            ]
        }
        testProp = motorlib.propellant.Propellant(props)
        self.assertEqual(testProp.getCombustionProperties(8e5), (1.467e-05, 0.382, 1.25, 3500, 23.67))
        self.assertEqual(testProp.getCombustionProperties(8e6), (1e-05, 0.3, 1.25, 3500, 23.67))

    def test_get_combustion_properties_out_of_range(self):
        props = {
            'name': 'TestProp',
            'density': 1650,
            'tabs': [
                {
                    'minPressure': 0,
                    'maxPressure': 6.895e+06,
                    'a': 1.467e-05,
                    'n': 0.382,
                    't': 3500,
                    'm': 23.67,
                    'k': 1.25
                }, {
                    'minPressure': 7e+06,
                    'maxPressure': 1.379e+07,
                    'a': 1e-05,
                    'n': 0.3,
                    't': 3500,
                    'm': 23.67,
                    'k': 1.25
                }
            ]
        }
        testProp = motorlib.propellant.Propellant(props)
        self.assertEqual(testProp.getCombustionProperties(6.9e5), (1.467e-05, 0.382, 1.25, 3500, 23.67))
        self.assertEqual(testProp.getCombustionProperties(8e10), (1e-05, 0.3, 1.25, 3500, 23.67))

if __name__ == '__main__':
    unittest.main()
