"""Builds public/Mark_Reizel_Vincent_Palma_Resume.docx from src/data/resume.json.

Same Harvard layout as the PDF: Times New Roman 10 pt, A4, dates on a right tab stop.
Run: python scripts/generate_resume_docx.py
"""

import json
import os
import re

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.opc.constants import RELATIONSHIP_TYPE
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn
from docx.shared import Inches, Mm, Pt

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA = os.path.join(ROOT, "src", "data", "resume.json")
OUT = os.path.join(ROOT, "public", "Mark_Reizel_Vincent_Palma_Resume.docx")

FONT = "Times New Roman"
MARGIN = Inches(0.5)
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
# Children of w:pPr that the schema places after w:pBdr
PPR_AFTER_PBDR = (
    "w:shd", "w:tabs", "w:suppressAutoHyphens", "w:kinsoku", "w:wordWrap", "w:overflowPunct",
    "w:topLinePunct", "w:autoSpaceDE", "w:autoSpaceDN", "w:bidi", "w:adjustRightInd", "w:snapToGrid",
    "w:spacing", "w:ind", "w:contextualSpacing", "w:mirrorIndents", "w:suppressOverlap", "w:jc",
    "w:textDirection", "w:textAlignment", "w:textboxTightWrap", "w:outlineLvl", "w:divId",
    "w:cnfStyle", "w:rPr", "w:sectPr", "w:pPrChange",
)


def add_hyperlink(paragraph, text, url, bold=False, italic=False, underline=True):
    r_id = paragraph.part.relate_to(url, RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    props = OxmlElement("w:rPr")
    for tag, on in (("w:b", bold), ("w:i", italic)):
        if on:
            props.append(OxmlElement(tag))
    if underline:
        u = OxmlElement("w:u")
        u.set(qn("w:val"), "single")
        props.append(u)
    run.append(props)
    t = OxmlElement("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    run.append(t)
    link.append(run)
    paragraph._p.append(link)


def add_rich(paragraph, text):
    """Plain text with [label](url) links."""
    pos = 0
    for m in LINK.finditer(text):
        paragraph.add_run(text[pos:m.start()])
        add_hyperlink(paragraph, m.group(1), m.group(2))
        pos = m.end()
    paragraph.add_run(text[pos:])


def create_resume_docx(output_path):
    with open(DATA, encoding="utf-8") as f:
        data = json.load(f)

    doc = Document()
    for section in doc.sections:
        section.page_width, section.page_height = Mm(210), Mm(297)  # A4
        section.top_margin = section.bottom_margin = Inches(0.45)
        section.left_margin = section.right_margin = MARGIN
    usable = doc.sections[0].page_width - 2 * MARGIN

    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(10)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.line_spacing = 1.0

    def para(align=None, before=0, after=0):
        p = doc.add_paragraph()
        if align is not None:
            p.alignment = align
        p.paragraph_format.space_before = Pt(before)
        p.paragraph_format.space_after = Pt(after)
        return p

    def two_sided(left_runs, right_text, italic=False, before=0):
        """Left content, then a right-aligned tab with right_text."""
        p = para(before=before)
        p.paragraph_format.tab_stops.add_tab_stop(usable, WD_TAB_ALIGNMENT.RIGHT)
        left_runs(p)
        if right_text:
            r = p.add_run("\t" + right_text)
            r.italic = italic
        return p

    def rule_below(p):
        # w:pBdr must come before w:shd, w:tabs, w:spacing, w:jc etc. in w:pPr (schema order)
        p._p.get_or_add_pPr().insert_element_before(parse_xml(
            r'<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
            r'<w:bottom w:val="single" w:sz="6" w:space="1" w:color="000000"/></w:pBdr>'
        ), *PPR_AFTER_PBDR)

    # Header
    p = para(WD_ALIGN_PARAGRAPH.CENTER, after=2)
    p.add_run(data["name"]).font.size = Pt(15)
    para(WD_ALIGN_PARAGRAPH.CENTER).add_run(" | ".join(data["contact"]))
    p = para(WD_ALIGN_PARAGRAPH.CENTER)
    for i, l in enumerate(data["links"]):
        if i:
            p.add_run(" | ")
        add_hyperlink(p, l["label"], l["url"], underline=False)

    for section in data["sections"]:
        p = para(before=6, after=3)
        r = p.add_run(section["title"].upper())
        r.bold = True
        r.font.size = Pt(10.5)
        rule_below(p)

        for line in section.get("lines", []):
            p = para()
            p.add_run(f"{line['label']}: ").bold = True
            p.add_run(line["text"])

        for i, e in enumerate(section.get("entries", [])):
            def heading(p, e=e):
                if e.get("url"):
                    add_hyperlink(p, e["heading"], e["url"], bold=True, underline=False)
                else:
                    p.add_run(e["heading"]).bold = True
                if e.get("role"):
                    p.add_run(f" | {e['role']}")

            two_sided(heading, e.get("right", ""), before=3 if i else 0)

            if e.get("sub"):
                def sub(p, e=e):
                    p.add_run(e["sub"]).italic = True

                p = two_sided(sub, "" if e.get("url") else e.get("subRight", ""), italic=True)
                if e.get("url") and e.get("subRight"):
                    p.add_run("\t")
                    add_hyperlink(p, e["subRight"], e["url"], italic=True)

            for b in e.get("bullets", []):
                p = para()
                p.paragraph_format.left_indent = Pt(14)
                p.paragraph_format.first_line_indent = Pt(-11)
                p.paragraph_format.tab_stops.add_tab_stop(Pt(14))
                p.add_run("●\t").font.size = Pt(7)
                add_rich(p, b)

    doc.save(output_path)
    print(f"Generated {output_path}")


if __name__ == "__main__":
    create_resume_docx(OUT)
