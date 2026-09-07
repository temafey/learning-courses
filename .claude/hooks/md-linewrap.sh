#!/usr/bin/env bash
# PostToolUse hook: warn when an edited Markdown file has lines over 80 columns.
# Advisory only -- never blocks. Skips fenced code blocks and table rows, which
# this repository's conventions allow to exceed 80.

f=$(jq -r '.tool_input.file_path // .tool_response.filePath // empty')
[ -n "$f" ] || exit 0
case "$f" in
  *.md|*.markdown) ;;
  *) exit 0 ;;
esac
[ -f "$f" ] || exit 0

awk '
  /^```/ { fence = !fence; next }
  fence { next }
  /^[ \t]*\|/ { next }
  /^[ \t]*(https?|ftp):\/\// { next }
  length($0) > 80 { n++; if (n <= 5) list = list (list ? ", " : "") FNR }
  END { if (n > 0) printf "%d %s\n", n, list }
' "$f" | {
  read -r n lines
  [ -n "$n" ] || exit 0
  jq -cn --arg f "$f" --arg n "$n" --arg l "$lines" \
    '{systemMessage: ("\($f): \($n) line(s) over 80 columns (line \($l)) - repo convention is an 80-column hard wrap"),
      hookSpecificOutput: {hookEventName: "PostToolUse",
        additionalContext: ("\($f) has \($n) prose line(s) longer than 80 columns at line(s) \($l). This repository hard-wraps prose at 80 columns; re-wrap them.")}}'
}
