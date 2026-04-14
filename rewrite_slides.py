import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. HTML Global updates
html = html.replace('<div id="slide-counter"><span class="current">01</span> / <span id="total">12</span></div>', 
                    '<div id="slide-counter">\n  <div><span class="current">01</span> / <span id="total">12</span></div>\n  <div class="kbd-hint">(Use ←/→ keys to navigate)</div>\n</div>')

# Slide 1 changes
# Increase underline weight (hero-line)
html = html.replace('width: 60px; height: 2px; background: var(--gradient-primary);',
                    'width: 60px; height: 6px; background: var(--gradient-primary); mix-blend-mode: screen; box-shadow: 0 0 10px var(--accent-primary);')
# Gradient for title (use a clean linear gradient to fix the "split" feel)
html = html.replace('background: var(--gradient-primary);', 'background: linear-gradient(90deg, #a855f7, #06b6d4);', 1) 
# wait, replacing the first instance of var(--gradient-primary) might be risky. Let's do it via CSS class
html = html.replace('.hero-title {\n  font-family: var(--font-heading);', 
                    '.hero-title {\n  font-family: var(--font-heading); background: linear-gradient(90deg, #c084fc, #22d3ee) !important; -webkit-background-clip: text !important;')
# Raise hero content vertically
html = html.replace('.hero-content {\n  position: relative; z-index: 2; text-align: center;\n  display: flex; flex-direction: column; align-items: center; gap: 20px;\n}',
                    '.hero-content {\n  position: relative; z-index: 2; text-align: center;\n  display: flex; flex-direction: column; align-items: center; gap: 20px;\n  transform: translateY(-5vh);\n}')
# Increase size of author meta
html = html.replace('.hero-meta {\n  font-size: 0.8rem; color: var(--text-muted);',
                    '.hero-meta {\n  font-size: 0.95rem; color: var(--text-primary); opacity: 0.9;')
# Add geometric background element to Slide 1
html = html.replace('<div class="hero-bg"></div>\n    <div class="hero-content">',
                    '<div class="hero-bg"></div>\n    <svg style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); width:600px; height:600px; opacity:0.03; animation: spin 60s linear infinite;" viewBox="0 0 100 100"><polygon points="50,5 95,25 95,75 50,95 5,75 5,25" fill="none" stroke="#fff" stroke-width="0.5"/></svg>\n    <style>@keyframes spin { 100% { transform:translate(-50%, -50%) rotate(360deg); } }</style>\n    <div class="hero-content">')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
