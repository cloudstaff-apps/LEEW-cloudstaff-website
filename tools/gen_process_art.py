#!/usr/bin/env python3
"""Draws the "a process sounds simple" diagram for the AI Coworkers page.

One request at the top fans out neatly into six steps, and the steps then tangle
into the systems and people behind them. Prints an inline <svg>. The layout is
seeded, so re-running gives the same picture. The three tiers are separate groups (pa-t1, pa-t2, pa-t3) so the page can dim the
tiers an option cannot reach. Paste the output into the "reach-figure" in
src/partials/ai-coworkers.html.
"""
import random

W, H = 1100, 610
STEPS = ["Overtime reports", "Missing timesheets", "Extra billables", "Telco costs", "Holiday credits", "Approvals"]
PARTS = ["Workforce system", "Team leads", "Staff", "Procurement", "Suppliers", "Purchase orders", "Telco invoices",
         "Leave records", "Payroll", "Managers", "Finance system", "Client contracts", "Spreadsheets", "Email threads"]
FILLS = ["#fde2e4", "#e2f0cb", "#fff1c1", "#dfe7fd", "#f1e4f3"]


def main():
    rnd = random.Random(7)
    o = []
    a = o.append
    a('<svg class="process-art" viewBox="0 0 %d %d" role="img" aria-labelledby="process-art-title" xmlns="http://www.w3.org/2000/svg">' % (W, H))
    a('<title id="process-art-title">One simple request, "Show me last month\'s invoices", fans out into six steps, '
      'which then tangle into the many systems and people behind them.</title>')
    top = (550, 62)
    sx = [105 + i * 178 for i in range(6)]
    sy = 190
    px = [85 + i * 155 for i in range(7)]
    rows = [452, 548]
    nodes = [(px[i % 7], rows[i // 7]) for i in range(14)]

    notes = [(26, 30, 118, "It sounds simple"), (26, 160, 150, "Then come the steps"), (26, 268, 218, "The devil is in the detail")]

    def note(k):
        x, y, wdt, txt = notes[k]
        a('<g class="pa-notes"><rect x="%d" y="%d" width="%d" height="24" rx="12"/>' % (x - 10, y - 16, wdt + 14))
        a('<text x="%d" y="%d">%s</text></g>' % (x, y, txt))

    # tier 3: the tangle of orthogonal runs from each step into the moving parts
    a('<g class="pa-tier pa-t3">')
    a('<g class="pa-tangle" fill="none">')
    for i, x in enumerate(sx):
        targets = rnd.sample(range(14), 4)
        for k, t in enumerate(targets):
            nx, ny = nodes[t]
            x0 = x - 45 + k * 30
            y1 = rnd.randrange(262, 330, 9)
            xm = rnd.randrange(40, W - 40, 13)
            y2 = rnd.randrange(340, 412, 9)
            x3 = nx - 36 + rnd.randrange(0, 72, 12)
            a('<path d="M%d %d V%d H%d V%d H%d V%d"/>' % (x0, sy + 50, y1, xm, y2, x3, ny - 17))
    for _ in range(7):
        p, q = rnd.sample(range(14), 2)
        (ax, ay), (bx, by) = nodes[p], nodes[q]
        ym = rnd.randrange(486, 518, 6)
        a('<path d="M%d %d V%d H%d V%d"/>' % (ax + rnd.randrange(-30, 30, 10), ay + 17, ym, bx + rnd.randrange(-30, 30, 10), by - 17 if by > ay else by + 17))
    a('</g>')
    a('<g class="pa-parts">')
    for i, ((x, y), label) in enumerate(zip(nodes, PARTS)):
        a('<rect x="%d" y="%d" width="132" height="34" rx="8" fill="%s"/>' % (x - 66, y - 17, FILLS[i % len(FILLS)]))
        a('<text x="%d" y="%d" text-anchor="middle">%s</text>' % (x, y + 5, label))
    a('</g>')
    note(2)
    a('</g>')

    # tier 2: the neat fan from the request to the six steps
    a('<g class="pa-tier pa-t2">')
    a('<g class="pa-fan" fill="none">')
    for x in sx:
        a('<path d="M%d %d L%d %d"/>' % (top[0], top[1] + 27, x, sy))
    a('</g>')
    a('<g class="pa-steps">')
    for x, label in zip(sx, STEPS):
        a('<rect x="%d" y="%d" width="158" height="50" rx="10"/>' % (x - 79, sy))
        a('<text x="%d" y="%d" text-anchor="middle">%s</text>' % (x, sy + 31, label))
    a('</g>')
    note(1)
    a('</g>')

    # tier 1: the request itself
    a('<g class="pa-tier pa-t1">')
    a('<g class="pa-request"><rect x="%d" y="%d" width="400" height="54" rx="27"/>' % (top[0] - 200, top[1] - 27))
    a('<text x="%d" y="%d" text-anchor="middle">&#8220;Show me last month&#8217;s invoices&#8221;</text></g>' % (top[0], top[1] + 6))
    note(0)
    a('</g>')
    a('</svg>')
    print("\n".join("          " + line for line in o))


if __name__ == "__main__":
    main()
