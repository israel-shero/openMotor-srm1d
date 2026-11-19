"""Provides default properties for the UI."""

DEFAULT_PREFERENCES = {
    'general': {
        'maxPressure': 1500 * 6895,
        'maxMassFlux': 2 / 0.001422,
        'maxMachNumber': 0.7,
        'minPortThroat': 2,
        'burnoutWebThres': 0.001 / 39.37,
        'burnoutThrustThres': 0.1,
        'timestep': 0.03,
        'ambPressure': 101325,
        'igniterPressure': 150 * 6895, # Deprecated, but needed for migration
        'mapDim': 750,
        'sepPressureRatio' : 0.4, # This is a good default value known as the Summerfield Criteria https://ntrs.nasa.gov/api/citations/19840011402/downloads/19840011402.pdf
        'flowSeparationWarnPercent': 0.05
    },
    'units': {
        'm': 'in',
        'm^3': 'in^3',
        'm/s': 'ft/s',
        'Pa': 'psi',
        'kg': 'lb',
        'kg/m^3': 'lb/in^3',
        'kg/s': 'lb/s',
        'kg/(m^2*s)': 'lb/(in^2*s)',
        '(m*Pa)/s': '(in*psi)/s',
        'm/(s*Pa)': 'thou/(s*psi)',
        'm/(s*Pa^n)': 'in/(s*psi^n)'
    }
}

CL_PROPS = {
            'name': 'MIT - Cherry Limeade',
            'density': 1670,
            'tabs': [
                {
                    'minPressure': 0,
                    'maxPressure': 6.895e+06,
                    'a': 3.517054143255937e-05,
                    'n': 0.3273,
                    't': 2800,
                    'm': 23.67,
                    'k': 1.21
                }
            ]
}
OW_PROPS = {
            'name': 'MIT - Ocean Water',
            'density': 1650,
            'tabs': [
                {
                    'minPressure': 0,
                    'maxPressure': 6.895e+06,
                    'a': 1.467e-05,
                    'n': 0.382,
                    't': 2600,
                    'm': 23.67,
                    'k': 1.25
                }
            ]
}
KNDX_PROPS = {
            'name': 'Nakka - KNDX',
            'density': 1785,
            'tabs': [
                {
                    'minPressure': 103425,
                    'maxPressure': 779135,
                    'a': 1.7096289148678155e-06,
                    'n': 0.619,
                    't': 1625.0,
                    'm': 42.39,
                    'k': 1.1308
                },
                {
                    'minPressure': 779135,
                    'maxPressure': 2571835,
                    'a': 0.008553459092346196,
                    'n': -0.009,
                    't': 1625.0,
                    'm': 42.39,
                    'k': 1.1308
                },
                {
                    'minPressure': 2571835,
                    'maxPressure': 5929700,
                    'a': 2.90330733578913e-07,
                    'n': 0.688,
                    't': 1625.0,
                    'm': 42.39,
                    'k': 1.1308
                },
                {
                    'minPressure': 5929700,
                    'maxPressure': 8501535,
                    'a': 0.1330457207587796,
                    'n': -0.148,
                    't': 1625.0,
                    'm': 42.39,
                    'k': 1.1308
                },
                {
                    'minPressure': 8501535,
                    'maxPressure': 11204375,
                    'a': 1.0537671694797537e-05,
                    'n': 0.444,
                    't': 1625.0,
                    'm': 42.39,
                    'k': 1.1308
                }
            ]
}
KNSB_PROPS = {
            'name': 'Nakka - KNSB',
            'density': 1750,
            'tabs': [
                {
                    'minPressure': 103425,
                    'maxPressure': 806715,
                    'a': 1.9253259619746373e-06,
                    'n': 0.625,
                    't': 1520.0,
                    'm': 39.9,
                    'k': 1.1361
                },
                {
                    'minPressure': 806715,
                    'maxPressure': 1503110,
                    'a': 0.6656608561590813,
                    'n': -0.313,
                    't': 1520.0,
                    'm': 39.9,
                    'k': 1.1361
                },
                {
                    'minPressure': 1503110,
                    'maxPressure': 3792250,
                    'a': 0.009528121181782798,
                    'n': -0.0145,
                    't': 1520.0,
                    'm': 39.9,
                    'k': 1.1361
                },
                {
                    'minPressure': 3792250,
                    'maxPressure': 7032900,
                    'a': 2.709667768835332e-06,
                    'n': 0.5245,
                    't': 1520.0,
                    'm': 39.9,
                    'k': 1.1361
                },
                {
                    'minPressure': 7032900,
                    'maxPressure': 10673460,
                    'a': 0.00417677261069904,
                    'n': 0.059,
                    't': 1520.0,
                    'm': 39.9,
                    'k': 1.1361
                }
            ]
}
WL_PROPS = {
            'name': 'RCS - White Lightning',
            'density': 1820.230130676801,
            'tabs': [
                {
                    'minPressure': 0.0,
                    'maxPressure': 10342500,
                    'a': 5.710516747228669e-06,
                    'n': 0.45,
                    't': 2339.0,
                    'm': 27.125,
                    'k': 1.243
                }
            ]
}
BT_PROPS = {
            'name': 'RCS - Blue Thunder',
            'density': 1625.0868456817973,
            'tabs': [
                {
                    'minPressure': 0.0,
                    'maxPressure': 10342500,
                    'a': 6.994600946367753e-05,
                    'n': 0.321,
                    't': 2616.5,
                    'm': 22.959,
                    'k': 1.235
                }
            ]
}
KNSU_PROPS = {
            'name': 'Nakka - KNSU',
            'density': 1800,
            'tabs': [
                {
                    'minPressure': 0.0,
                    'maxPressure': 10342500,
                    'a': 0.00010073115141607291,
                    'n': 0.319,
                    't': 1720,
                    'm': 41.98,
                    'k': 1.133
                }
            ]
}

SRM1D_REPOSITORY_PROPELLANTS = [
    {
        'name': '84 Unsuppressed - CHARACTERIZED',
        'density': 1699.5457728642882,
        'transportVariant': 'frozen',
        'tabs': [{
            'minPressure': 0, 'maxPressure': 13790000.000000002,
            'a': 1.5694834407944363e-05, 'n': 0.4,
            'k': 1.19, 't': 3105.0, 'm': 24.98,
            'mu': 9.125e-05, 'kThermalFrozen': 0.3654, 'cpFrozen': 2050.0,
            'kThermalEffective': 0.6584, 'cpEffective': 2826.0,
        }],
    },
    {
        'name': 'Alex - Hairless Balless',
        'density': 1743.8336105936507,
        'transportVariant': 'frozen',
        'tabs': [{
            'minPressure': 0, 'maxPressure': 13790000.000000002,
            'a': 0.00027796386499737217, 'n': 0.28,
            'k': 1.213, 't': 2733.6, 'm': 27.027,
            'mu': 8.382e-05, 'kThermalFrozen': 0.2713, 'cpFrozen': 1838.0,
            'kThermalEffective': 0.2713, 'cpEffective': 1838.0,
        }],
    },
    {
        'name': 'Booska Super Pourable - Vibe Mix THERMO',
        'density': 1646.95396556067,
        'transportVariant': 'frozen',
        'tabs': [{
            'minPressure': 0, 'maxPressure': 13790000.000000002,
            'a': 1.1333086102492701e-05, 'n': 0.405,
            'k': 1.2106, 't': 2752.0, 'm': 23.55,
            'mu': 8.319e-05, 'kThermalFrozen': 0.3386, 'cpFrozen': 2.049,
            'kThermalEffective': 0.4499, 'cpEffective': 2.354,
        }],
    },
    {
        'name': 'Chase - Energy',
        'density': 1862.8571744913124,
        'transportVariant': 'frozen',
        'tabs': [{
            'minPressure': 0, 'maxPressure': 13790000.000000002,
            'a': 1.075303334201942e-05, 'n': 0.412,
            'k': 1.198, 't': 2977.0, 'm': 24.98,
            'mu': 9.009e-05, 'kThermalFrozen': 0.346, 'cpFrozen': 2017.0,
            'kThermalEffective': 0.5761, 'cpEffective': 2629.0,
        }],
    },
    {
        'name': 'Chase Red',
        'density': 1622.6510146066823,
        'transportVariant': 'frozen',
        'tabs': [{
            'minPressure': 0, 'maxPressure': 13790000.000000002,
            'a': 1.293975943475869e-05, 'n': 0.39,
            'k': 1.22209, 't': 2641.471, 'm': 24.01168,
            'mu': 8.236e-05, 'kThermalFrozen': 0.2841, 'cpFrozen': 1881.0,
            'kThermalEffective': 0.2841, 'cpEffective': 1881.0,
        }],
    },
    {
        'name': 'Hasegawa A Prop',
        'density': 1700.0,
        'transportVariant': 'frozen',
        'tabs': [{
            'minPressure': 0, 'maxPressure': 10000000.0,
            'a': 4.821e-05, 'n': 0.3,
            'k': 1.19, 't': 3041.0, 'm': 25.4,
            'mu': 8.842e-05, 'kThermalFrozen': 0.3685, 'cpFrozen': 2060.0,
            'kThermalEffective': 0.6517, 'cpEffective': 2764.0,
        }],
    },
    {
        'name': 'Hasegawa Propellant 1 (69AP/17HTPB/14Al)',
        'density': 1700.0,
        'transportVariant': 'frozen',
        'tabs': [{
            'minPressure': 0, 'maxPressure': 20000000.0,
            'a': 4.821e-05, 'n': 0.3,
            'k': 1.19, 't': 3041.0, 'm': 25.4,
            'mu': 8.842e-05, 'kThermalFrozen': 0.3685, 'cpFrozen': 2060.0,
            'kThermalEffective': 0.3685, 'cpEffective': 2060.0,
        }],
    },
    {
        'name': 'KSP v1 0.42ips',
        'density': 1681.1746241761768,
        'transportVariant': 'frozen',
        'tabs': [{
            'minPressure': 6895.000000000001, 'maxPressure': 13790000.000000002,
            'a': 0.00016438807796402777, 'n': 0.265,
            'k': 1.210129, 't': 2835.896, 'm': 24.54,
            'mu': 8.998e-05, 'kThermalFrozen': 0.2892, 'cpFrozen': 1927.0,
            'kThermalEffective': 0.2892, 'cpEffective': 1927.0,
        }],
    },
    {
        'name': 'RCS - 8522',
        'density': 1716.153712012799,
        'transportVariant': 'frozen',
        'tabs': [{
            'minPressure': 0, 'maxPressure': 13790000.000000002,
            'a': 1.912458279795643e-05, 'n': 0.405,
            'k': 1.216, 't': 3016.0, 'm': 25.278,
            'mu': 8.389e-05, 'kThermalFrozen': 0.2506, 'cpFrozen': 1878.0,
            'kThermalEffective': 0.2506, 'cpEffective': 1878.0,
        }],
    },
    {
        'name': 'RCS - Warp9',
        'density': 1641.4179858444998,
        'transportVariant': 'frozen',
        'tabs': [{
            'minPressure': 0, 'maxPressure': 20685000.000000004,
            'a': 0.0002472181550396159, 'n': 0.287,
            'k': 1.229, 't': 2780.64, 'm': 23.6686,
            'mu': 7.401e-05, 'kThermalFrozen': 0.2383, 'cpFrozen': 1867.0,
            'kThermalEffective': 0.2383, 'cpEffective': 1867.0,
        }],
    },
    {
        'name': 'Risky Batman V3 Jan2024',
        'density': 1682.0520769611899,
        'transportVariant': 'frozen',
        'tabs': [{
            'minPressure': 0, 'maxPressure': 13100500.000000002,
            'a': 5.054532350783141e-06, 'n': 0.456,
            'k': 1.19889, 't': 2883.66, 'm': 23.7923,
            'mu': 8.604e-05, 'kThermalFrozen': 0.3455, 'cpFrozen': 2052.0,
            'kThermalEffective': 0.5038, 'cpEffective': 2468.0,
        }],
    },
    {
        'name': 'Risky Batman V3 Jan2024 (LHS-calibrated)',
        'density': 1682.0520769611899,
        'transportVariant': 'frozen',
        'tabs': [{
            'minPressure': 0, 'maxPressure': 13100500.000000002,
            'a': 4.6343518757893865e-06, 'n': 0.456,
            'k': 1.19889, 't': 2883.66, 'm': 23.7923,
            'mu': 8.604e-05, 'kThermalFrozen': 0.3455, 'cpFrozen': 2052.0,
            'kThermalEffective': 0.3455, 'cpEffective': 2052.0,
        }],
    },
    {
        'name': 'Stormtrooper 2.1',
        'density': 1832.0965031984122,
        'transportVariant': 'frozen',
        'tabs': [{
            'minPressure': 0, 'maxPressure': 11032000.000000002,
            'a': 6.919245093121588e-06, 'n': 0.427909,
            'k': 1.239961, 't': 2202.0, 'm': 24.50103,
            'mu': 7.285e-05, 'kThermalFrozen': 0.2898, 'cpFrozen': 1621.0,
            'kThermalEffective': 0.2898, 'cpEffective': 1621.0,
        }],
    },
]

DEFAULT_PROPELLANTS = [
    CL_PROPS, OW_PROPS, KNDX_PROPS, KNSB_PROPS, KNSU_PROPS, WL_PROPS, BT_PROPS,
] + SRM1D_REPOSITORY_PROPELLANTS
