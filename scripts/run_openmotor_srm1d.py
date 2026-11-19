"""Run openMotor with the sibling srm_1d checkout on sys.path."""

import os
import sys
from pathlib import Path


def _configure_srm1d():
    root = Path(__file__).resolve().parents[1]
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    candidates = [
        Path(os.environ.get("OPENMOTOR_SRM1D_PATH", "")).expanduser(),
        root.parent / "srm_1d",
        root / "srm_1d",
    ]
    for candidate in candidates:
        if candidate and (candidate / "srm_1d").is_dir():
            srm_root = str(candidate.resolve())
            if srm_root not in sys.path:
                sys.path.insert(0, srm_root)
            os.environ.setdefault("OPENMOTOR_SRM1D_PATH", srm_root)
            os.environ.setdefault("SRM1D_OPENMOTOR_PATH", str(root.resolve()))
            return


_configure_srm1d()

from app import App
from PyQt6.QtCore import Qt


app = App(sys.argv)
sys.exit(app.exec())
