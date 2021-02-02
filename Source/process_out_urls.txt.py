import sys
from urllib.parse import quote

for line in sys.stdin:
	line = line.strip()
	if line == "":
		continue
	spl = line.split(",")
	print(f"extension:{quote(spl[1])}/{spl[0]}")
