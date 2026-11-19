import unittest
import motorlib.propellant
from PyQt6.QtWidgets import QApplication, QWidget, QSizePolicy
from uilib.widgets.propertyEditor import PropertyEditor


class _UnitPreferences:
    def getUnit(self, unit):
        return unit


class TestPropellantEditorLayout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

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
