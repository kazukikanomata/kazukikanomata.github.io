import os
import re
from datetime import datetime, timezone

title = os.environ.get("ISSUE_TITLE", "untitled")
body = os.environ.get("ISSUE_BODY", "")
issue_number = os.environ.get("ISSUE_NUMBER", "0")
created_at = os.environ.get("ISSUE_CREATED_AT", datetime.now(timezone.utc).isoformat())

date_str = created_at[:10]

# ASCII-only slug from title + issue number for uniqueness
ascii_part = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
slug = f"{ascii_part}-{issue_number}" if ascii_part else f"issue-{issue_number}"

filename = f"_learning/{date_str}-{slug}.md"

# Escape double quotes in title for YAML
title_escaped = title.replace('"', '\\"')

content = f"""---
title: "{title_escaped}"
date: {date_str}
issue: {issue_number}
---

{body}
"""

os.makedirs("_learning", exist_ok=True)

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Created: {filename}")
