"""Build the combined Umbra executable for the current operating system."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "packaging" / "umbra_gui.spec"
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

    subprocess.run(
        [
            sys.executable,
            "-m",
            "PyInstaller",
            "--clean",
            "--noconfirm",
            str(SPEC),
        ],
        cwd=ROOT,
        check=True,
    )
    suffix = ".exe" if sys.platform == "win32" else ""
    artifact = ROOT / "dist" / f"Umbra{suffix}"
    if not artifact.is_file():
        raise FileNotFoundError(
            f"Expected build artifact was not created: {artifact}"
        )
    print(artifact)


if __name__ == "__main__":
    main()
