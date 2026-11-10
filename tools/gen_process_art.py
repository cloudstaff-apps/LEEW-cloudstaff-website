#!/usr/bin/env python3
"""Draws the "a process sounds simple" diagram for the AI Coworkers page.

One request at the top fans out into six steps, and the steps then cross over
into the systems and people behind them. Prints an inline <svg>. The three tiers
are separate groups (pa-t1, pa-t2, pa-t3) so the page can dim the tiers an option
cannot reach. Paste the output into the "reach-figure" in
src/partials/ai-coworkers.html (or run with --write to splice it in).

Style rules: brand blue, navy text, white and pale grey boxes only. No pastel
fills, no black lines. Keep it to eleven moving parts so it stays readable.
"""
import re
import sys

W, H = 1100, 540
STEPS = ["Overtime reports", "Missing timesheets", "Extra billables", "Telco costs", "Holiday credits", "Approvals"]
ROW1 = ["Workforce system", "Team leads", "Procurement", "Suppliers", "Telco invoices", "Finance system"]
ROW2 = ["Leave records", "Payroll", "Client contracts", "Spreadsheets", "Email threads"]
# step index -> parts it depends on, as (row, column)
LINKS = {
    0: [(1, 0), (1, 1), (2, 1)],
    1: [(1, 0), (2, 0), (2, 4)],
    2: [(2, 2), (2, 3), (1, 5)],
    3: [(1, 4), (1, 3), (1, 2)],
    4: [(2, 0), (2, 1), (1, 1)],
    5: [(1, 5), (2, 4), (2, 2)],
}


def render():
    o = []
    a = o.append
    a('<svg class="process-art" viewBox="0 0 %d %d" role="img" aria-labelledby="process-art-title" xmlns="http://www.w3.org/2000/svg">' % (W, H))
    a('<title id="process-art-title">One simple request, "Show me last month\'s invoices", fans out into six steps, '
      'which then cross over into the many systems and people behind them.</title>')
    top = (550, 58)
    sx = [105 + i * 178 for i in range(6)]
    sy, sh = 176, 48
    r1y, r2y, ph, pw = 392, 468, 36, 150
    r2x = [(sx[i] + sx[i + 1]) // 2 for i in range(5)]

    def note(y, txt):
        a('<g class="pa-notes"><rect x="0" y="%d" width="%d" height="20" rx="4"/>' % (y - 14, len(txt) * 7.6 + 10))
        a('<text x="2" y="%d">%s</text></g>' % (y, txt.upper()))

    a('<g class="pa-tier pa-t3">')
    a('<g class="pa-tangle" fill="none">')
    used = {}
    for i, x in enumerate(sx):
        for k, (row, col) in enumerate(LINKS[i]):
            x0 = x - 40 + k * 40
            key = (row, col)
            n = used.get(key, 0)
            used[key] = n + 1
            if row == 1:
                x1 = sx[col] - 30 + n * 30
                a('<path d="M%d %d C%d %d %d %d %d %d"/>' % (x0, sy + sh, x0, 318, x1, 300, x1, r1y))
            else:
                x1 = r2x[col] - 6 + n * 6
                a('<path d="M%d %d C%d %d %d %d %d %d V%d"/>' % (x0, sy + sh, x0, 312, x1, 292, x1, 376, r2y))
    a('</g>')
    a('<g class="pa-parts">')
    for x, label in zip(sx, ROW1):
        a('<rect x="%d" y="%d" width="%d" height="%d" rx="8"/>' % (x - pw // 2, r1y, pw, ph))
        a('<text x="%d" y="%d" text-anchor="middle">%s</text>' % (x, r1y + 23, label))
    for x, label in zip(r2x, ROW2):
        a('<rect x="%d" y="%d" width="%d" height="%d" rx="8"/>' % (x - pw // 2, r2y, pw, ph))
        a('<text x="%d" y="%d" text-anchor="middle">%s</text>' % (x, r2y + 23, label))
    a('</g>')
    note(270, "The devil is in the detail")
    a('</g>')

    a('<g class="pa-tier pa-t2">')
    a('<g class="pa-fan" fill="none">')
    for x in sx:
        a('<path d="M%d %d C%d %d %d %d %d %d"/>' % (top[0], top[1] + 26, top[0], 140, x, 120, x, sy))
    a('</g>')
    a('<g class="pa-steps">')
    for x, label in zip(sx, STEPS):
        a('<rect x="%d" y="%d" width="158" height="%d" rx="10"/>' % (x - 79, sy, sh))
        a('<text x="%d" y="%d" text-anchor="middle">%s</text>' % (x, sy + 30, label))
    a('</g>')
    note(150, "Then come the steps")
    a('</g>')

    a('<g class="pa-tier pa-t1">')
    a('<g class="pa-request"><rect x="%d" y="%d" width="400" height="52" rx="26"/>' % (top[0] - 200, top[1] - 26))
    a('<text x="%d" y="%d" text-anchor="middle">&#8220;Show me last month&#8217;s invoices&#8221;</text></g>' % (top[0], top[1] + 7))
    note(24, "It sounds simple")
    a('</g>')
    a('</svg>')
    return "\n".join("              " + line for line in o)


if __name__ == "__main__":
    svg = render()
    if "--write" in sys.argv:
        p = "src/partials/ai-coworkers.html"
        s = open(p, encoding="utf-8").read()
        s, n = re.subn(r'[ \t]*<svg class="process-art".*?</svg>', lambda m: svg, s, count=1, flags=re.S)
        assert n == 1
        open(p, "w", encoding="utf-8").write(s)
    else:
        print(svg)
