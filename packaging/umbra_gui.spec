# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

from PyInstaller.utils.hooks import collect_all, collect_data_files


ROOT = Path(SPEC).resolve().parent.parent
ctk_datas, ctk_binaries, ctk_hiddenimports = collect_all("customtkinter")
app_datas = collect_data_files("external_app_raider")
datas = [
    *ctk_datas,
    *app_datas,
    (str(ROOT / "config" / "config.jsonc.example"), "config"),
]

analysis = Analysis(
    [str(ROOT / "packaging" / "umbra_gui.py")],
    pathex=[str(ROOT / "src")],
    binaries=ctk_binaries,
    datas=datas,
    hiddenimports=[*ctk_hiddenimports, "PIL._tkinter_finder"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["discord"],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(analysis.pure)

exe = EXE(
    pyz,
    analysis.scripts,
    analysis.binaries,
    analysis.datas,
    [],
    name="Umbra",
    icon=str(ROOT / "src" / "external_app_raider" / "gui" / "assets" / "umbra-development.png"),
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
