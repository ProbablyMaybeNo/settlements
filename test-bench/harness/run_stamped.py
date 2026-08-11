"""Run an existing harness, capture its stdout verbatim, and stamp it.

    py -3.13 run_stamped.py <script.py> [args...] [--as NAME] [--note "..."]

Persisting raw output was already this project's practice. It was not enough:
`results/packet_battle-n2000.txt` records an `extra activation` row of -2.63 that
neither the branch engine nor today's engine produces, because the .txt was
generated before the implementation beside it was fixed and both were committed
together. Nothing tied the numbers to the code that made them.

So this wrapper exists to make the binding automatic rather than remembered. It
writes two files side by side:

    results/<name>-<engine8>.txt    verbatim stdout, exactly as before
    results/<name>-<engine8>.json   the provenance envelope for that stdout

`provenance.staleness()` can then answer "which stored results were taken against
something that has since moved?" without anyone having to recall that it moved.

The stdout is stored verbatim and NOT parsed. Parsing a harness's prose output is
how a rounded summary quietly replaces the raw numbers it was rounded from.
"""

from __future__ import annotations

import contextlib
import io
import runpy
import sys
from pathlib import Path

import provenance as P

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2

    name = None
    note = ""
    args = []
    i = 0
    while i < len(argv):
        if argv[i] == "--as" and i + 1 < len(argv):
            name = argv[i + 1]
            i += 2
        elif argv[i] == "--note" and i + 1 < len(argv):
            note = argv[i + 1]
            i += 2
        else:
            args.append(argv[i])
            i += 1

    script = Path(args[0]).resolve()
    if not script.exists():
        print(f"no such harness: {script}")
        return 2
    script_args = args[1:]
    name = name or f"{script.stem}-n{script_args[0] if script_args else 'default'}"

    # Fingerprint BEFORE the run, not after. A long run with an edit landing
    # mid-flight would otherwise be stamped with the post-edit engine it never
    # used — the exact mislabelling this module exists to prevent, reintroduced
    # by the wrapper meant to stop it. Python caches the imported module, so the
    # run genuinely used the pre-edit source; the stamp must say so.
    pre = {
        "engine": P.engine_fingerprint(),
        "cost_table": P.cost_table_fingerprint(),
        "git": P.git_state(),
    }

    # The harnesses chdir into engine2d/ and read sys.argv themselves.
    cwd = Path.cwd()
    old_argv = sys.argv[:]
    sys.argv = [str(script)] + script_args

    buf = io.StringIO()

    class Tee:
        """Show progress live AND capture it. A 30-minute run with no output is
        indistinguishable from a hung one."""

        def write(self, s):
            buf.write(s)
            sys.__stdout__.write(s)
            return len(s)

        def flush(self):
            sys.__stdout__.flush()

    status = "ok"
    try:
        with contextlib.redirect_stdout(Tee()):
            runpy.run_path(str(script), run_name="__main__")
    except SystemExit as e:
        status = f"SystemExit({e.code})"
    except Exception as e:
        status = f"{type(e).__name__}: {e}"
        buf.write(f"\n\n!! HARNESS RAISED: {status}\n")
    finally:
        sys.argv = old_argv
        try:
            import os

            os.chdir(cwd)
        except Exception:
            pass

    text = buf.getvalue()
    post = P.engine_fingerprint()
    caveats = ["stdout captured verbatim and NOT parsed; the .txt beside this envelope is the record"]
    if post["combined"] != pre["engine"]["combined"]:
        caveats.append(
            f"engine source CHANGED during the run ({pre['engine']['combined']} -> "
            f"{post['combined']}); this envelope records the PRE-run fingerprint, "
            "which is what the run actually executed"
        )

    env = P.Envelope(
        name=name,
        question=note or f"stdout of {script.name} {' '.join(script_args)}",
        params={
            "harness": str(script.relative_to(P.REPO)) if str(script).startswith(str(P.REPO)) else str(script),
            "argv": script_args,
            "status": status,
        },
        caveats=caveats,
        engine=pre["engine"],
        cost_table=pre["cost_table"],
        git=pre["git"],
    )
    out = env.write(stdout_text=text)
    print(f"\n[stamped] {out.name}  engine={env.engine['combined']}  cost_table={env.cost_table['combined']}")
    if env.git["dirty_relevant"]:
        print("[stamped] WARNING: uncommitted changes in engine/points/balance at run time —")
        for p in env.git["dirty_relevant"]:
            print(f"[stamped]          {p}")
        print("[stamped] this result is not cleanly attributable to a commit")
    elif env.git["dirty"]:
        print("[stamped] (tree dirty elsewhere; nothing feeding the fingerprints was uncommitted)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
