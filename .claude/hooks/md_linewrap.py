"""PostToolUse hook: warn when an edited Markdown file has over-long lines.

Advisory only — it never blocks an edit. But it must never fail *silently*
either: a check that quietly stops running is worse than no check, because the
absence of a warning reads as "clean" when it actually means "not looked at".
So every failure path prints a systemMessage saying the check did not run.

Written in Python rather than bash+jq+awk because that is one dependency
instead of three, and because JSON and UTF-8 paths (Cyrillic filenames on a
cp1251 console) are handled natively.
"""
import json
import re
import sys

LIMIT = 80

# Exempt the same constructs .markdownlint-cli2.jsonc exempts. One difference
# remains and it is deliberate: markdownlint's MD013 only reports a long line
# when there is whitespace past the limit, i.e. when the line could actually be
# broken. This hook reports any prose line over the limit, including one that
# runs long only because its last word straddles column 80 — that word can be
# moved down, and the convention says hard wrap. So the hook is the stricter of
# the two, and `npm run lint` staying green does not mean the hook will be
# quiet.
TABLE = re.compile(r"^\s*\|")
HEADING = re.compile(r"^#")
BARE_URL = re.compile(r"^\s*(https?|ftp)://")
DISABLE = re.compile(r"^\s*<!--\s*markdownlint-disable-next-line")


def emit(message, context=None):
    out = {"systemMessage": message}
    if context:
        out["hookSpecificOutput"] = {
            "hookEventName": "PostToolUse",
            "additionalContext": context,
        }
    json.dump(out, sys.stdout, ensure_ascii=False)
    sys.stdout.write("\n")


def over_long(text):
    """Return [(lineno, width)] for prose lines wider than LIMIT."""
    hits, fence, skip = [], False, False
    for n, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        if DISABLE.match(line):
            skip = True
            continue
        if skip:
            skip = False
            continue
        if TABLE.match(line) or HEADING.match(line) or BARE_URL.match(line):
            continue
        if len(line) > LIMIT:
            hits.append((n, len(line)))
    return hits


def main():
    raw = sys.stdin.read()
    if not raw.strip():
        return
    data = json.loads(raw)
    path = (data.get("tool_input", {}).get("file_path")
            or data.get("tool_response", {}).get("filePath") or "")
    if not path or not path.lower().endswith((".md", ".markdown")):
        return

    # Deliberately not guarded: PostToolUse fires only after a successful
    # write, so an unreadable path means something is wrong with the hook's
    # assumptions. That belongs in the loud handler, not swallowed here.
    with open(path, encoding="utf-8", errors="replace") as fh:
        text = fh.read()

    hits = over_long(text)
    if not hits:
        return

    shown = ", ".join(str(n) for n, _ in hits[:5])
    emit(
        f"{path}: {len(hits)} line(s) over {LIMIT} columns (line {shown})"
        f" - repo convention is an {LIMIT}-column hard wrap",
        f"{path} has {len(hits)} prose line(s) longer than {LIMIT} columns at"
        f" line(s) {shown}. This repository hard-wraps prose at {LIMIT}"
        f" columns; re-wrap them.",
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # never block an edit, but never hide either
        emit(f"md-linewrap hook did NOT run ({type(exc).__name__}: {exc})."
             f" The {LIMIT}-column check was skipped for this edit.")
    sys.exit(0)
