# -*- mode: python -*-

# Run with:
#   OPENMOTOR_SRM1D_PATH=../../srm_1d \
#   pyinstaller --windowed --clean --noconfirm pyinstaller/macOneFile.spec
#
# This spec bundles the srm_1d plugin, so the resulting app can run both
# openMotor's quasi-steady solver and srm_1d's transient solver.

from PyInstaller.utils.hooks import collect_submodules
from uilib.fileIO import appVersionStr
from pathlib import Path

ROOT = Path(SPECPATH).resolve().parent
SRM_ROOT = (ROOT.parent / 'srm_1d').resolve()

block_cipher = None

a = Analysis([str(ROOT / 'scripts/run_openmotor_srm1d.py')],
             pathex=[str(ROOT), str(SRM_ROOT)],
             binaries=[],
             datas=[
                 (str(ROOT / 'resources/oMFile256.icns'), '.'),
                 (str(SRM_ROOT / 'srm_1d/pyrogens'), 'srm_1d/pyrogens'),
             ],
             hiddenimports=(
                 ['pywt._extensions._cwt',
                  'srm_1d.srm1d_plugin',
                  'srm_1d.openmotor_adapter',
                  'srm_1d.station_viz']
                 + collect_submodules('srm_1d')
             ),
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False,
             target_arch=None)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='openMotor',
          debug=False,
          bootloader_ignore_signals=False,
          argv_emulation=True,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False)
coll = COLLECT(exe,
              a.binaries,
              a.zipfiles,
              a.datas,
              strip=False,
              upx=True,
              name='openMotor')
app = BUNDLE(coll,
             name='openMotor.app',
             icon='../resources/oMIconCycles.icns',
             version=appVersionStr,
             info_plist={
              'NSHighResolutionCapable': True,
              'CFBundleDocumentTypes': [
               {
                'CFBundleTypeName': 'openMotor Motor File',
                'CFBundleTypeExtensions': ['ric'],
                'CFBundleTypeRole': 'Editor',
                'CFBundleTypeIconFile': 'oMFile256',
                'LSHandlerRank': 'Owner',
               }
              ],
             },
             bundle_identifier=None)
