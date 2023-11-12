# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

import sys
if sys.platform.startswith('win'):
#  site_packages='C:/Python39/Lib/site-packages'
  site_packages='c:/hostedtoolcache/windows/python/3.9.13/x64/lib/site-packages'

if sys.platform.startswith('linux'):
#  site_packages='./env/lib/python3.9/site-packages'
  site_packages='/opt/hostedtoolcache/Python/3.9.13/x64/lib/python3.9/site-packages'

if sys.platform.startswith('darwin'):
  site_packages='/Users/runner/hostedtoolcache/Python/3.9.13/x64/lib/python3.9/site-packages'

a = Analysis(
    ['neurofeedback_coherence_meditation_report_pyinstaller.py'],
    pathex=[],
    binaries=[],
    datas=[(site_packages+'/gradio', 'gradio'), (site_packages+'/gradio_client', 'gradio_client')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='neurofeedback_coherence_meditation_report_pyinstaller',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='neurofeedback_coherence_meditation_report_pyinstaller',
)
