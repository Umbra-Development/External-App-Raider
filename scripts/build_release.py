"""Build the GUI and bot executables for the current operating system."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SPECS = (
    ROOT / "packaging" / "umbra_gui.spec",
    ROOT / "packaging" / "umbra_bot.spec",
)
REQUIRED_INPUTS = (
    ROOT / "config" / "config.jsonc.example",
    ROOT / "src" / "umbra_gui" / "assets" / "umbra-development.png",
    ROOT / "src" / "umbra_gui" / "assets" / "umbra-theme.json",
)


def main() -> None:
    missing_inputs = [path for path in REQUIRED_INPUTS if not path.is_file()]
    if missing_inputs:
        missing = "\n".join(f"- {path}" for path in missing_inputs)
        raise FileNotFoundError(f"Missing release build inputs:\n{missing}")

    for spec in SPECS:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "PyInstaller",
                "--clean",
                "--noconfirm",
                str(spec),
            ],
            cwd=ROOT,
            check=True,
        )
    suffix = ".exe" if sys.platform == "win32" else ""
    for name in ("Umbra", "UmbraBot"):
        artifact = ROOT / "dist" / f"{name}{suffix}"
        if not artifact.is_file():
            raise FileNotFoundError(
                f"Expected build artifact was not created: {artifact}"
            )
        print(artifact)


if __name__ == "__main__":
    main()
