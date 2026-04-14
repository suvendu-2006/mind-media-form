import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make all slide-titles heroes
text = text.replace('class="slide-title"', 'class="slide-title animate hero-reveal"')
text = text.replace('class="hero-title"', 'class="hero-title animate hero-reveal"')

# Make cards, content rows, bullet points standard reveals
text = text.replace('class="card"', 'class="card animate reveal"')
text = text.replace('<p class="hero-subtitle"', '<p class="hero-subtitle animate reveal"')
text = text.replace('<ul class="bullet-list stagger"', '<ul class="bullet-list stagger animate reveal"')
text = text.replace('class="bottom-banner"', 'class="bottom-banner animate reveal"')
text = text.replace('class="debate-row"', 'class="debate-row animate reveal"')
text = text.replace('class="takeaway-grid"', 'class="takeaway-grid animate reveal"')
text = text.replace('class="hookline"', 'class="hookline animate reveal"')
text = text.replace('class="zone-bar"', 'class="zone-bar animate reveal"')

# Custom sequences
# Slide 8 - Goldilocks stagger
text = text.replace('<div class="zone-bar animate reveal">', '<div class="zone-bar animate reveal zone-1">', 1) 
text = text.replace('<div class="zone-bar animate reveal">', '<div class="zone-bar animate reveal delay-06">', 1) # Middle
text = text.replace('<div class="zone-bar animate reveal">', '<div class="zone-bar animate reveal delay-03">', 1) # Right

# Slide 10 - Digital crowbar 0%
# The 0% needs to be immediate. It is in <h1 class="hero-title animate hero-reveal"> but it should be standard zero delay
text = re.sub(r'<h1 class="hero-title animate hero-reveal"[^>]*>0%</h1>', r'<h1 class="hero-title animate reveal delay-00" style="font-size: clamp(8rem, 15vw, 12rem); letter-spacing: -0.05em; color: var(--accent-primary);">0%</h1>', text)

# The rest of Slide 10 gets delay-10
text = text.replace('<p class="hero-subtitle animate reveal">Have <strong>never</strong> experienced<br>social media-free life</p>', '<p class="hero-subtitle animate reveal delay-10">Have <strong>never</strong> experienced<br>social media-free life</p>')
text = text.replace('<p class="hero-meta" style="letter-spacing: 2px;">(Generation Alpha)</p>', '<p class="hero-meta animate reveal delay-10" style="letter-spacing: 2px;">(Generation Alpha)</p>')

# Slide 12 - Damage chain
# The boxes are <div class="card animate reveal" style="padding: 20px;">
text = text.replace('<div class="card animate reveal" style="padding: 20px; border-top: 1px solid rgba(192, 132, 252, 0.4);">', '<div class="card animate reveal delay-02" style="padding: 20px; border-top: 1px solid rgba(192, 132, 252, 0.4);">')
text = text.replace('<div class="card animate reveal" style="padding: 20px; border-top: 1px solid rgba(96, 165, 250, 0.4);">', '<div class="card animate reveal delay-04" style="padding: 20px; border-top: 1px solid rgba(96, 165, 250, 0.4);">')
text = text.replace('<div class="card animate reveal" style="padding: 20px; border-top: 1px solid rgba(244, 114, 182, 0.4);">', '<div class="card animate reveal delay-06" style="padding: 20px; border-top: 1px solid rgba(244, 114, 182, 0.4);">')

# Slide 1a (Agenda) - Bullets stagger
text = text.replace('<li style="border-left: 3px solid var(--accent-primary);', '<li class="animate reveal delay-02" style="border-left: 3px solid var(--accent-primary);')
text = text.replace('<li style="border-left: 3px solid #C084FC;', '<li class="animate reveal delay-04" style="border-left: 3px solid #C084FC;')
text = text.replace('<li style="border-left: 3px solid #F472B6;', '<li class="animate reveal delay-06" style="border-left: 3px solid #F472B6;')
text = text.replace('<li style="border-left: 3px solid #10b981;', '<li class="animate reveal delay-08" style="border-left: 3px solid #10b981;')


# Ensure Slide 1 doesn't have duplicate hero-reveals injected mistakenly
# "class="hero-title animate hero-title-slam animate hero-reveal""
text = text.replace('class="hero-title animate hero-title-slam animate hero-reveal"', 'class="hero-title animate hero-title-slam"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("HTML classes injected.")
