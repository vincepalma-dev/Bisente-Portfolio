"""Builds public/Mark_Reizel_Vincent_Palma_Resume.pdf from src/data/resume.json.

Harvard-style layout: Times New Roman, centered header, ALL-CAPS section headings
with a rule, "Heading | Role" with dates on the right, italic sub-line, bullets.
Run: python scripts/generate_resume_pdf.py
"""

import json
import os
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA = os.path.join(ROOT, "src", "data", "resume.json")
OUT = os.path.join(ROOT, "public", "Mark_Reizel_Vincent_Palma_Resume.pdf")


def register_fonts():
    """Embed Times New Roman when available (Windows); fall back to the built-in Times."""
    fonts_dir = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")
    files = {"TNR": "times.ttf", "TNR-Bold": "timesbd.ttf", "TNR-Italic": "timesi.ttf", "TNR-BoldItalic": "timesbi.ttf"}
    if all(os.path.exists(os.path.join(fonts_dir, f)) for f in files.values()):
        for name, f in files.items():
            pdfmetrics.registerFont(TTFont(name, os.path.join(fonts_dir, f)))
        pdfmetrics.registerFontFamily("TNR", normal="TNR", bold="TNR-Bold", italic="TNR-Italic", boldItalic="TNR-BoldItalic")
        return "TNR", "TNR-Bold", "TNR-Italic", "\u25cf"
    return "Times-Roman", "Times-Bold", "Times-Italic", "\u2022"


def create_resume(output_path):
    with open(DATA, encoding="utf-8") as f:
        data = json.load(f)

    regular, bold, italic, bullet = register_fonts()
    size = 10

    def style(name, **kw):
        base = dict(fontName=regular, fontSize=size, leading=size * 1.18, textColor=colors.black)
        base.update(kw)
        return ParagraphStyle(name, **base)

    s_name = style("Name", fontName=regular, fontSize=15, leading=18, alignment=TA_CENTER, spaceAfter=2)
    s_center = style("Center", alignment=TA_CENTER)
    s_section = style("Section", fontName=bold, fontSize=10.5, leading=12, spaceBefore=6, spaceAfter=1)
    s_left = style("Left")
    s_right = style("Right", alignment=TA_RIGHT)
    s_line = style("Line", leftIndent=0)
    s_bullet = style("Bullet", leftIndent=14, bulletIndent=3, bulletFontName=regular, bulletFontSize=7, spaceBefore=1)

    usable = A4[0] - 2 * 0.5 * inch - 12  # minus the frame's 6pt padding on each side
    right_w = 1.55 * inch

    def link(label, url, underline=True):
        text = f"<u>{escape(label)}</u>" if underline else escape(label)
        return f'<a href="{escape(url)}" color="black">{text}</a>'

    def rich(text):
        # Bullets may hold [label](url) links; escape plain text and link parts once each
        out, pos = [], 0
        for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", text):
            out += [escape(text[pos:m.start()]), link(m.group(1), m.group(2))]
            pos = m.end()
        out.append(escape(text[pos:]))
        return "".join(out)

    def row(left, right, left_style=s_left, right_style=s_right):
        t = Table([[Paragraph(left, left_style), Paragraph(right, right_style)]], colWidths=[usable - right_w, right_w])
        t.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]))
        return t

    story = [
        Paragraph(escape(data["name"]), s_name),
        Paragraph(" | ".join(escape(c) for c in data["contact"]), s_center),
        Paragraph(" | ".join(link(l["label"], l["url"], underline=False) for l in data["links"]), s_center),
    ]

    for section in data["sections"]:
        story.append(Paragraph(escape(section["title"].upper()), s_section))
        story.append(HRFlowable(width="100%", thickness=0.6, color=colors.black, spaceBefore=0, spaceAfter=3))

        for line in section.get("lines", []):
            story.append(Paragraph(f"<b>{escape(line['label'])}:</b> {escape(line['text'])}", s_line))

        for i, e in enumerate(section.get("entries", [])):
            heading = link(e["heading"], e["url"], underline=False) if e.get("url") else escape(e["heading"])
            left = f"<b>{heading}</b>" + (f" | {escape(e['role'])}" if e.get("role") else "")
            block = [row(left, escape(e.get("right", "")))]
            if e.get("sub"):
                sub_right = escape(e.get("subRight", ""))
                if e.get("url") and sub_right:
                    sub_right = link(e["subRight"], e["url"])
                block.append(row(f"<i>{escape(e['sub'])}</i>", f"<i>{sub_right}</i>"))
            for b in e.get("bullets", []):
                block.append(Paragraph(rich(b), s_bullet, bulletText=bullet))
            if i:
                story.append(Spacer(1, 3))
            story.append(KeepTogether(block))

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=0.5 * inch,
        rightMargin=0.5 * inch,
        topMargin=0.45 * inch,
        bottomMargin=0.45 * inch,
        title=f"{data['name'].title()} - Resume",
        author="Mark Reizel Vincent C. Palma",
        subject="Full-Stack Software Engineer Resume",
    )
    doc.build(story)
    print(f"Generated {output_path}")


if __name__ == "__main__":
    create_resume(OUT)
