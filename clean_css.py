import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove all ".slide.active .something { ... }" rules
content = re.sub(r'\.slide\.active\s+\.[a-zA-Z0-9_-]+\s*\{\s*opacity:\s*1[^{}]*\}', '', content)
# For hero-line, etc.
content = re.sub(r'\.slide\.active\s+\.[a-zA-Z0-9_-]+\s*\{\s*opacity:\s*1;\s*\}', '', content)

# 2. Strip "opacity: 0;", "transform: translateY(...);", and "transition: ...;" from base classes
content = re.sub(r'\s*opacity:\s*0;\s*transform:\s*translateY\([0-9-a-z%]+\)(?:\s*scale\([0-9.]+\))?;\n?', '\n', content)
content = re.sub(r'\s*transition:\s*opacity\s+[0-9a-z. ,]+\n?', '\n', content)
content = re.sub(r'\s*opacity:\s*0;\s*transition:\s*[0-9a-z. ,]+\n?', '\n', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS cleaned.")
