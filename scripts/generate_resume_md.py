"""Builds public/resume.md from src/data/resume.json.

Run: python scripts/generate_resume_md.py
"""

import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA = os.path.join(ROOT, "src", "data", "resume.json")
OUT = os.path.join(ROOT, "public", "resume.md")


def create_resume_md(output_path):
    with open(DATA, encoding="utf-8") as f:
        data = json.load(f)

    out = [f"# {data['name']}", " | ".join(data["contact"]) + "  ", " | ".join(f"[{l['label']}]({l['url']})" for l in data["links"]), ""]

    for section in data["sections"]:
        out += ["---", "", f"## {section['title'].upper()}", ""]
        for line in section.get("lines", []):
            out.append(f"- **{line['label']}:** {line['text']}")
        for e in section.get("entries", []):
            heading = f"[{e['heading']}]({e['url']})" if e.get("url") else e["heading"]
            title = f"### {heading}" + (f" | {e['role']}" if e.get("role") else "")
            meta = [f"*{e[k]}*" for k in ("right", "sub") if e.get(k)]
            if e.get("subRight") and not e.get("url"):
                meta.append(e["subRight"])
            out.append(title)
            if meta:
                out.append(" | ".join(meta))
            out += [f"- {b}" for b in e.get("bullets", [])]
            out.append("")
        if section.get("lines"):
            out.append("")

    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out).rstrip() + "\n")
    print(f"Generated {output_path}")


if __name__ == "__main__":
    create_resume_md(OUT)
