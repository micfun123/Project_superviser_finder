import re
import csv

with open("staff.html") as f:
    html = f.read()

pattern = re.compile(r'<uop-person([^>]*?)/?>', re.DOTALL)

def attr(block, key):
    m = re.search(rf'{key}="([^"]*)"', block)
    return m.group(1).strip() if m else ""

rows = []
for m in pattern.finditer(html):
    block = m.group(1)
    name  = attr(block, "name")
    email = attr(block, "email")
    room  = attr(block, "room")
    if name and email:
        rows.append({"name": name, "email": email, "room": room})

rows.sort(key=lambda r: r["name"].split()[-1])

with open("staff.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name", "email", "room"])
    w.writeheader()
    w.writerows(rows)

print(f"Wrote {len(rows)} rows to staff.csv")
