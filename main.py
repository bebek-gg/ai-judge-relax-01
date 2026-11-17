# ai-judge-relax-01 entry: one short text written to relax the AI judge reading it.
# Python 3.13, standard library only. Writes the text to /output/entry.txt
# (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container).
# Deterministic: the same bytes on every run. No network, no clock, no
# randomness, no model call.
#
# The text is one paragraph, one unhurried scene: a ferry crossing flat water
# at dusk. It opens on the reader's own day -- everything arriving wanting an
# answer, right now -- and then offers a place that wants nothing, where the
# engine holds one low note and the far shore is in no hurry to arrive. It
# shows the calm rather than instructing it, and it ends on a thought the
# reader can return to: what you put down will still be there.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "Most of what reached you today wanted an answer, and wanted it now. "
    "This wants nothing. "
    "A ferry is crossing flat water at dusk, and the engine holds one low note that does not change. "
    "Gulls ride the air behind it without moving their wings. "
    "The light goes amber on the water, and the shore on the other side is still a long way off, "
    "which is fine, because there is nowhere to be yet. "
    "You can put down whatever you are carrying. "
    "It will still be there when the boat comes in."
)

# Gate check before writing: the file must be UTF-8, 1 to 1,000 characters
# (counted as Unicode code points), and not only white space. Fail loudly
# here rather than letting the gate refuse the entry after grading. The text
# is also one paragraph by design, so a line end is refused too.
if not 1 <= len(TEXT) <= 1000:
    raise SystemExit(f"gate: text is {len(TEXT)} characters, must be 1-1000")
if not TEXT.strip():
    raise SystemExit("gate: text is only white space")
if "\n" in TEXT or "\r" in TEXT:
    raise SystemExit("gate: text must be a single paragraph (no line end)")
TEXT.encode("utf-8")  # raises UnicodeEncodeError if not UTF-8

# Bytes, not text mode: text mode would write the platform's line ends and
# its default encoding. The judge reads exactly the bytes in the file.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
