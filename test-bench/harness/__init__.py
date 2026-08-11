"""Settlements atom-pricing harness.

A general-purpose measurement tool, not another bespoke script per question.

The rebuild's five pipeline requirements, and where each lives:
  1. general-purpose atom pricing, not one script per question   -> effects.py, measure.py
  2. version-tag every result against the cost table it ran on   -> provenance.py
  3. cross-subsystem consistency checks as a standing test       -> consistency.py
  4. parameter sweeps, so curves emerge from data                -> sweep.py
  5. persist raw output alongside summaries, always              -> provenance.Envelope.write

The unit of account throughout is RAW WIN-POINTS PER MODEL. Nothing here converts
to Credits. The Credits-per-win-point constant is a scale choice the rebuild is
re-making, and a harness that stores Credits has already made it.
"""
