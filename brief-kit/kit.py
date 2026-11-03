"""Brief design kit v2 (2026-10-20). Light, bubbly, email-safe.

Every color is inline and explicit (background AND text) on every element, tables carry
bgcolor attributes, no <style> block, no CSS classes. Same HTML goes in the email and on
the Claude page.
"""
import html

FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"
MONO = "'SF Mono',Menlo,Consolas,'Courier New',monospace"
PAGE_BG = "#eef1f6"
INK = "#0f172a"
BODY = "#334155"
MUTED = "#64748b"
CARD_BORDER = "#dfe4ec"
SOFT = "#f6f8fb"

# brief: (emoji, hero background, hero kicker color, hero dek color)
HERO = {
    "Morning Brief":         ("☀️", "#b4530f", "#ffe3c7", "#fff1e3"),
    "Mid-day Brief":         ("🕐", "#0f766e", "#c8f1ea", "#e6f8f5"),
    "Evening Brief":         ("🌙", "#3b3a98", "#d9d8ff", "#ecebff"),
    "Weekly Master Brief":   ("📅", "#1e3a8a", "#cdddff", "#e6eeff"),
    "Sooners Gameday Brief": ("🏈", "#841617", "#fdf9d8", "#fbeeee"),
    "Weekly Workflow Audit": ("🔧", "#334155", "#d7e0ea", "#eef2f6"),
}

PILL = {  # name: (background, text)
    "OU": ("#fde8e8", "#a61b1b"), "EY": ("#fff4cc", "#7a5a00"), "CPA": ("#f3e8ff", "#6b21a8"),
    "Personal": ("#e0ecff", "#1d4ed8"),
    "due": ("#fff1e0", "#b45309"), "overdue": ("#b42318", "#ffffff"), "new": ("#e0f2fe", "#0369a1"),
    "done": ("#dcfce7", "#15803d"), "warn": ("#fef3c7", "#92400e"), "status": ("#eef2f7", "#334155"),
}


def e(s):
    return html.escape(s, quote=True)


def pill(label, kind):
    bg, fg = PILL.get(kind, PILL["status"])
    return (f'<span style="display:inline-block;padding:3px 9px;margin:0 4px 4px 0;border-radius:999px;'
            f'background-color:{bg};color:{fg};font:700 11px/1.4 {FONT};letter-spacing:.05em;'
            f'text-transform:uppercase;">{e(label)}</span>')


def spacer(h=14):
    return f'<tr><td height="{h}" style="height:{h}px;line-height:{h}px;font-size:0;">&nbsp;</td></tr>'


def hero(brief, kicker, headline, dek):
    emoji, bg, kc, dc = HERO[brief]
    return (f'<tr><td bgcolor="{bg}" style="background-color:{bg};border-radius:24px;padding:24px 22px;">'
            f'<p style="margin:0 0 10px;font:700 12px/1.4 {FONT};letter-spacing:.07em;text-transform:uppercase;color:{kc};">{emoji} {e(kicker)}</p>'
            f'<h1 style="margin:0;font:800 22px/1.25 {FONT};color:#ffffff;">{e(headline)}</h1>'
            f'<p style="margin:12px 0 0;font:400 15px/1.55 {FONT};color:{dc};">{e(dek)}</p>'
            f'</td></tr>')


def needs(items):
    lis = "".join(f'<li style="margin:0 0 9px;font:400 15px/1.5 {FONT};color:#3b2a10;">{i}</li>' for i in items)
    return (f'<tr><td bgcolor="#fff7e6" style="background-color:#fff7e6;border:1px solid #f3d38c;border-radius:20px;padding:18px 20px;">'
            f'<p style="margin:0 0 10px;font:800 16px/1.3 {FONT};color:#8a4b00;">⚡ Needs you</p>'
            f'<ul style="margin:0;padding-left:20px;">{lis}</ul></td></tr>')


def card(title, inner, num=None, accent="#0b6e69"):
    n = f'<span style="color:{accent};">{num}.</span> ' if num else ""
    return (f'<tr><td bgcolor="#ffffff" style="background-color:#ffffff;border:1px solid {CARD_BORDER};border-radius:20px;padding:20px;">'
            f'<h2 style="margin:0 0 12px;font:800 17px/1.3 {FONT};color:{INK};">{n}{e(title)}</h2>{inner}</td></tr>')


def stat(text):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{SOFT}" '
            f'style="background-color:{SOFT};border-radius:14px;margin:0 0 12px;"><tr><td style="padding:11px 14px;'
            f'font:700 15px/1.45 {FONT};color:{INK};">{text}</td></tr></table>')


def item(pills, title, meta=None, note=None, button=None, accent="#0b6e69", last=False):
    out = (f'<p style="margin:0 0 2px;line-height:1;">{"".join(pills)}</p>' if pills else '')
    out += f'<p style="margin:0 0 4px;font:700 15px/1.45 {FONT};color:{INK};">{e(title)}</p>'
    if meta:
        out += f'<p style="margin:0 0 4px;font:500 12.5px/1.5 {MONO};color:{MUTED};">{e(meta)}</p>'
    if note:
        out += f'<p style="margin:0 0 4px;font:400 14px/1.55 {FONT};color:{BODY};">{note}</p>'
    if button:
        label, href = button
        out += (f'<p style="margin:8px 0 0;"><a href="{e(href)}" style="display:inline-block;padding:9px 16px;'
                f'border-radius:999px;background-color:{accent};color:#ffffff;text-decoration:none;'
                f'font:700 14px/1 {FONT};">{e(label)}</a></p>')
    sep = "" if last else f'<p style="margin:12px 0;border-top:1px solid #edf0f5;font-size:0;line-height:0;">&nbsp;</p>'
    return out + sep


def para(text):
    return f'<p style="margin:0 0 10px;font:400 15px/1.55 {FONT};color:{BODY};">{text}</p>'


def nxt(n, title, why, accent):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{SOFT}" '
            f'style="background-color:{SOFT};border-radius:16px;margin:0 0 10px;"><tr><td style="padding:14px 16px;">'
            f'<p style="margin:0 0 4px;font:700 15px/1.45 {FONT};color:{INK};">'
            f'<span style="display:inline-block;width:24px;height:24px;border-radius:999px;background-color:{accent};'
            f'color:#ffffff;text-align:center;font:700 13px/24px {FONT};margin-right:8px;">{n}</span>{e(title)}</p>'
            f'<p style="margin:0;font:400 14px/1.55 {FONT};color:{BODY};">{why}</p></td></tr></table>')


def footer(lines):
    body = "<br>".join(e(l) for l in lines)
    return f'<tr><td style="padding:6px 10px 0;font:400 12.5px/1.7 {FONT};color:{MUTED};text-align:center;">{body}</td></tr>'


def wrap(rows):
    inner = spacer().join(rows)
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{PAGE_BG}" '
            f'style="background-color:{PAGE_BG};"><tr><td align="center" style="padding:20px 12px 36px;">'
            f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:680px;">'
            f'{inner}</table></td></tr></table>')


def email_html(body):
    return ('<!doctype html><html><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light">'
            f'</head><body style="margin:0;padding:0;background-color:{PAGE_BG};">{body}</body></html>')


def page_html(title, body):
    return (f'<title>{e(title)}</title>\n'
            f'<style>html,body{{background-color:{PAGE_BG};margin:0;}}</style>\n{body}\n')


def bullets(items):
    lis = "".join(f'<li style="margin:0 0 7px;font:400 15px/1.5 {FONT};color:{BODY};">{i}</li>' for i in items)
    return f'<ul style="margin:0 0 10px;padding-left:20px;">{lis}</ul>'


def link(label, href):
    return f'<a href="{e(href)}" style="color:#1d4ed8;text-decoration:underline;">{e(label)}</a>'


def build(brief, rows, page_url, outdir="/tmp/brief"):
    """rows[0] must be hero(...). Writes email.html and page.html; returns their paths."""
    import os
    os.makedirs(outdir, exist_ok=True)
    accent = HERO[brief][1]
    btn = (f'<tr><td align="center"><a href="{e(page_url)}" style="display:inline-block;padding:12px 22px;'
           f'border-radius:999px;background-color:{accent};color:#ffffff;text-decoration:none;'
           f'font:700 15px/1 {FONT};">📄 Open the full brief</a></td></tr>')
    email = email_html(wrap([rows[0], btn] + rows[1:]))
    page = page_html(brief, wrap(rows))
    pe, pp = os.path.join(outdir, "email.html"), os.path.join(outdir, "page.html")
    open(pe, "w").write(email)
    open(pp, "w").write(page)
    return pe, pp
