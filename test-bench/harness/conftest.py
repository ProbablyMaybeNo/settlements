"""Make the harness importable no matter where pytest is invoked from.

THE FAILURE THIS FIXES, AND WHY IT WAS WORSE THAN A PAPERCUT
------------------------------------------------------------
`test_provenance.py` does a bare `import provenance`. That resolves only when the
harness directory is on `sys.path` - which it is when pytest runs FROM this
directory, and is not when it runs from the repo root.

The reason is that `harness/` contains `__init__.py`, so pytest treats it as a
package and prepends its PARENT (`test-bench/`) to `sys.path` rather than the
directory itself. Run from the root, the import fails at COLLECTION time, and a
collection error does not skip one test - it INTERRUPTS THE WHOLE RUN. So the
command reported an error and executed none of the 16 tests.

That is the dangerous shape: a suite that appears to be protecting you while
running nothing. Broken from 2026-08-11 (56e854b, the commit that introduced the
provenance harness) to 2026-08-13.

Fixing it HERE rather than in each test file is deliberate: conftest.py is
collected before any test module, so this covers every existing test and every
test added later. Patching the one file that happened to break would have left
the next one free to reintroduce it.
"""

from __future__ import annotations

import sys
from pathlib import Path

HARNESS = Path(__file__).resolve().parent
if str(HARNESS) not in sys.path:
    sys.path.insert(0, str(HARNESS))
