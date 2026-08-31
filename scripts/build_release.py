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


def main() -> None:
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
            raise FileNotFoundError(f"Expected build artifact was not created: {artifact}")
        print(artifact)


if __name__ == "__main__":
    main()
