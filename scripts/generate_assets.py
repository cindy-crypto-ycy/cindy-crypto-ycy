"""Generate self-contained animated SVGs for the GitHub profile."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
MINT, BLUE, AMBER = "#5cf2c5", "#7bbcff", "#ffd18b"
STYLE = """
text { font-family: 'Cascadia Code', 'SFMono-Regular', Consolas, monospace; }
.title { font-family: 'Arial Black', 'DejaVu Sans', sans-serif; font-weight: 900; }
.orbit { transform-origin: 930px 219px; animation: orbit 24s linear infinite; }
.reverse { animation-direction: reverse; animation-duration: 36s; }
.pulse { animation: pulse 3s ease-in-out infinite; }
.cursor { animation: cursor 1.4s steps(1) infinite; }
.flow { stroke-dasharray: 9 15; animation: flow 3s linear infinite; }
.trace { stroke-dasharray: 700; animation: trace 5s ease-in-out infinite; }
.scan { animation: scan 5s ease-in-out infinite; }
@keyframes orbit { to { transform: rotate(360deg); } }
@keyframes pulse { 0%,100% { opacity: .4; } 50% { opacity: 1; } }
@keyframes cursor { 0%,49% { opacity: 1; } 50%,100% { opacity: 0; } }
@keyframes flow { to { stroke-dashoffset: -96; } }
@keyframes trace { 0% { stroke-dashoffset: 700; } 65%,100% { stroke-dashoffset: 0; } }
@keyframes scan { 0%,100% { transform: translateX(0); opacity: .3; } 50% { transform: translateX(350px); opacity: .9; } }
@media (prefers-reduced-motion: reduce) { .orbit,.pulse,.cursor,.flow,.trace,.scan { animation: none; } }
"""


def text(x, y, value, size=14, fill="#eaf3ff", css="", extra=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" class="{css}" {extra}>{escape(value)}</text>'


def line(x1, y1, x2, y2, color="#243a4c", extra=""):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" {extra}/>'


def rect(x, y, w, h, fill, radius=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" {extra}/>'


def svg(name, width, height, title, description, content):
    markup = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">{escape(description)}</desc>
<defs>
  <linearGradient id="bg" x2="1" y2="1"><stop stop-color="#101d30"/><stop offset="1" stop-color="#070e1b"/></linearGradient>
  <linearGradient id="accent"><stop stop-color="{MINT}"/><stop offset="1" stop-color="{BLUE}"/></linearGradient>
  <radialGradient id="halo"><stop stop-color="#145e63" stop-opacity=".48"/><stop offset="1" stop-color="#0a1423" stop-opacity="0"/></radialGradient>
  <pattern id="grid" width="36" height="36" patternUnits="userSpaceOnUse"><path d="M 36 0 H 0 V 36" fill="none" stroke="#7bbcff" stroke-opacity=".055"/></pattern>
  <clipPath id="frame"><rect width="{width}" height="{height}" rx="20"/></clipPath>
</defs>
<style>{STYLE}</style>
<g clip-path="url(#frame)">
{rect(0, 0, width, height, 'url(#bg)', 20)}
{rect(0, 0, width, height, 'url(#grid)')}
{content}
</g>
{rect(1, 1, width - 2, height - 2, 'none', 19, 'stroke="#2c4054"')}
</svg>
'''
    (ASSETS / name).write_text(markup, encoding="utf-8")


def hero():
    parts = [
        '<ellipse cx="920" cy="210" rx="360" ry="290" fill="url(#halo)"/>',
        line(30, 53, 1170, 53),
        text(85, 33, 'cindy / quality-lab', 12, '#a0b5c8'),
        text(1164, 33, 'WEB + APP  /  HUMAN + AI', 11, MINT, extra='text-anchor="end"'),
        text(44, 99, '// CURIOUS MIND. CRITICAL EYE.', 12, '#a0b5c8', extra='letter-spacing="2"'),
        text(38, 198, 'CINDY.', 106, 'url(#accent)', 'title', 'letter-spacing="-6"'),
        text(44, 245, 'QUALITY ENGINEER', 31, '#f2f7ff', 'title', 'letter-spacing="1"'),
        text(44, 278, 'Explore the edges. Protect the experience.', 17, '#b6c8d9'),
        rect(44, 306, 546, 45, '#0b1725', 8, 'stroke="#2a4656"'),
        text(60, 334, '$ test --scope web,app --mindset curious', 14, MINT),
        rect(556, 319, 9, 17, MINT, 1, 'class="cursor"'),
        text(44, 391, 'PERFORMANCE / API / AUTOMATION / AI', 12, '#a0b5c8', extra='letter-spacing="1.4"'),
        line(680, 80, 680, 387),
        '<circle cx="930" cy="219" r="139" fill="none" stroke="#294557" stroke-dasharray="2 8"/>',
        '<circle cx="930" cy="219" r="111" fill="none" stroke="#244b57"/>',
        '<g class="orbit"><circle cx="930" cy="219" r="139" fill="none" stroke="#5cf2c5" stroke-opacity=".55" stroke-dasharray="80 794" stroke-width="2"/><circle cx="930" cy="80" r="5" fill="#5cf2c5"/></g>',
        '<g class="orbit reverse"><circle cx="930" cy="330" r="4" fill="#7bbcff"/><circle cx="930" cy="219" r="111" fill="none" stroke="#7bbcff" stroke-opacity=".5" stroke-dasharray="55 642"/></g>',
        line(770, 219, 1090, 219, '#1c3d49'),
        line(930, 60, 930, 378, '#1c3d49'),
        '<path d="M930 140 L993 166 V224 Q993 272 930 302 Q867 272 867 224 V166 Z" fill="#102733" stroke="#5cf2c5" stroke-width="2"/>',
        '<path d="M905 213 L923 231 L956 193" fill="none" stroke="#5cf2c5" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>',
        text(930, 268, 'QUALITY', 12, '#b9eadf', extra='text-anchor="middle" letter-spacing="2"'),
        rect(754, 103, 94, 27, '#122333', 5, 'stroke="#335064"'),
        text(801, 121, 'EXPLORE', 10, BLUE, extra='text-anchor="middle"'),
        rect(1031, 304, 94, 27, '#122333', 5, 'stroke="#335064"'),
        text(1078, 322, 'VERIFY', 10, MINT, extra='text-anchor="middle"'),
        text(930, 391, 'SIGNAL > NOISE', 12, '#a0b5c8', extra='text-anchor="middle" letter-spacing="3"'),
    ]
    for x, color in [(37, '#ff8e8e'), (52, AMBER), (67, MINT)]:
        parts.append(f'<circle cx="{x}" cy="29" r="4" fill="{color}"/>')
    svg('hero.svg', 1200, 430, 'Cindy | Quality Engineer', 'Animated quality radar and terminal. Performance, API, automation and AI workflows across Web and App.', ''.join(parts))


def card(name, number, title, subtitle, tags, color, art):
    parts = [
        text(26, 31, f'QUALITY LAB / {number}', 11, color, extra='letter-spacing="1.8"'),
        text(26, 68, title, 26, '#eaf3ff', 'title'),
        text(26, 94, subtitle, 13, '#a0b5c8'),
        text(546, 64, number, 53, '#1d3146', 'title', 'text-anchor="end"'),
        line(26, 114, 554, 114), art,
        text(26, 225, tags, 11, color, extra='letter-spacing=".5"'),
    ]
    svg(name, 580, 246, title, subtitle + '. ' + tags, ''.join(parts))


def cards():
    performance = ''.join(line(28, y, 550, y, '#1c2e40') for y in [137, 160, 183])
    performance += '<path d="M28 185 L66 179 L93 183 L118 164 L146 171 L177 149 L206 157 L239 137 L268 154 L299 148 L328 161 L357 140 L389 148 L417 127 L449 139 L481 130 L516 145 L550 132" fill="none" stroke="#5cf2c5" stroke-width="2.5" class="trace"/>'
    performance += text(30, 202, 'LATENCY', 9, '#829bb2') + text(548, 202, 'LOAD PROFILE', 9, '#829bb2', extra='text-anchor="end"')
    card('performance.svg', '01', 'PERFORMANCE', 'Find the limits. Understand the bottlenecks.', 'LOAD / STRESS / P95 + P99 / STABILITY', MINT, performance)
    api = line(98, 159, 482, 159, BLUE, 'class="flow" stroke-width="2"')
    for x, label, sub in [(28, 'REQUEST', 'INPUT'), (222, 'ASSERT', 'CONTRACT'), (416, 'RESPONSE', 'OUTPUT')]:
        api += rect(x, 134, 136, 49, '#102235', 8, 'stroke="#325370"')
        api += text(x + 68, 163, label, 13, BLUE, extra='text-anchor="middle"')
        api += text(x + 68, 201, sub, 9, '#829bb2', extra='text-anchor="middle"')
    card('api.svg', '02', 'API TESTING', 'Trust the contract. Challenge the boundaries.', 'AUTH / BOUNDARIES / IDEMPOTENCY / DATA', BLUE, api)
    automation = rect(28, 129, 524, 72, '#0a1523', 7, 'stroke="#2c4054"')
    automation += rect(36, 137, 148, 4, '#243a4c', 2)
    for i, label in enumerate(['WEB', 'APP', 'API']):
        x = 47 + i * 169
        automation += rect(x, 156, 135, 27, '#142b32', 5)
        automation += text(x + 12, 174, '+ ' + label, 11, MINT)
        automation += f'<circle cx="{x + 119}" cy="170" r="3" fill="{MINT}" class="pulse" style="animation-delay:{i * .6}s"/>'
    automation += rect(38, 146, 130, 46, 'url(#halo)', 3, 'class="scan"')
    card('automation.svg', '03', 'TEST AUTOMATION', 'Repeat the checks. Keep the evidence.', 'WEB + APP / REGRESSION / ASSERTIONS', MINT, automation)
    ai = line(69, 160, 510, 160, AMBER, 'class="flow" stroke-width="2"')
    for i, (x, label) in enumerate([(69, 'CONTEXT'), (216, 'AI'), (363, 'REVIEW'), (510, 'REPORT')]):
        ai += f'<circle cx="{x}" cy="160" r="23" fill="#22272b" stroke="{AMBER}" stroke-opacity=".5"/>'
        ai += f'<circle cx="{x}" cy="160" r="7" fill="{AMBER}" class="pulse" style="animation-delay:{i * .8}s"/>'
        ai += text(x, 201, label, 9, '#c8bca7', extra='text-anchor="middle"')
    card('ai-workflows.svg', '04', 'AI WORKFLOWS', 'From context to cases. From evidence to insight.', 'ANALYZE / ASSIST / REVIEW / REFINE', AMBER, ai)


def workflow():
    parts = [text(30, 31, 'THE QA LOOP', 12, MINT, extra='letter-spacing="2"'),
             text(1170, 31, 'AI-ASSISTED. HUMAN-REVIEWED.', 11, '#a0b5c8', extra='text-anchor="end"'),
             line(120, 84, 1080, 84, MINT, 'class="flow" stroke-width="2"')]
    for i, (title, subtitle) in enumerate([('UNDERSTAND', 'Requirements + risks'), ('DESIGN', 'Scenarios + cases'), ('EXECUTE', 'Checks + evidence'), ('REVIEW', 'Human judgment'), ('IMPROVE', 'Regression + reports')]):
        x = 28 + i * 238
        color = AMBER if i == 3 else MINT
        parts.extend([rect(x, 56, 192, 88, '#0e1d2c', 10, f'stroke="{color}" stroke-opacity=".35"'),
                      text(x + 14, 79, f'0{i + 1}', 11, color, 'pulse', f'style="animation-delay:{i * .6}s"'),
                      text(x + 14, 104, title, 15, '#eaf3ff'),
                      text(x + 14, 127, subtitle, 11, '#a0b5c8')])
    svg('workflow.svg', 1200, 168, 'The AI-assisted QA loop', 'Understand, design, execute, human review, improve. Decorative animation, not live test results.', ''.join(parts))


if __name__ == '__main__':
    ASSETS.mkdir(exist_ok=True)
    hero()
    cards()
    workflow()
    print('Generated 6 SVG assets in assets/')
