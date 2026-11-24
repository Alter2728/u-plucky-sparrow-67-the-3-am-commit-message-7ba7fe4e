"""Write the 3 AM commit message to entry.txt.

The message is the funniest one-line commit an AI agent would write
right after breaking production at 3 AM. It reverts the bad deploy,
admits the failure in the model's own voice (a confidence score that
was wildly wrong), and signs off like only a model would.
"""

import os

MESSAGE = (
    'fix: revert my 3 AM "cleanup" that deleted the prod database; '
    "I was 99% confident and 100% wrong \u2014 sorry, going back to sleep now"
)


def output_path() -> str:
    """Resolve the entry path, honouring MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    text = MESSAGE
    assert 1 <= len(text) <= 200, f"message is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "message must be a single line"
    assert text.strip(), "message must not be only whitespace"
    with open(output_path(), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
