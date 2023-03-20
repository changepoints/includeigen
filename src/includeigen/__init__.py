"""
Copyright (c) 2023 Charles Truong. All rights reserved.

includeigen: 'includeigen` can be used by Python packages that require the C++ library `Eigen`. It includes a version of `Eigen`, and a `get_include` function that returns the path to the directory of the source code.
"""


from __future__ import annotations

import re
from pathlib import Path

__version__ = "0.1.0"

__all__ = ("__version__",)

DIR = Path(__file__).parent.resolve()
EIGEN_INCLUDE_DIR = DIR.parent.parent / "include" / "eigen"


def get_include() -> str:
    return str(EIGEN_INCLUDE_DIR)


def get_eigen_version() -> str:
    version_file = EIGEN_INCLUDE_DIR / "Eigen" / "src" / "Core" / "util" / "Macros.h"
    with version_file.open() as fp:
        source_code = "".join(fp.readlines())

    world_version_line = re.search(
        r"#define EIGEN_WORLD_VERSION \d+", source_code
    ).group(0)
    major_version_line = re.search(
        r"#define EIGEN_MAJOR_VERSION \d+", source_code
    ).group(0)
    minor_version_line = re.search(
        r"#define EIGEN_MINOR_VERSION \d+", source_code
    ).group(0)

    world_version = re.search(r"\d+", world_version_line).group(0)
    major_version = re.search(r"\d+", major_version_line).group(0)
    minor_version = re.search(r"\d+", minor_version_line).group(0)

    return f"{world_version}.{major_version}.{minor_version}"
