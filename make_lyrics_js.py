"""
Turns lyrics.json into lyrics.js, which the player loads.
(A .js file works when you double-click the HTML from your computer, and on
GitHub Pages. A .json file would be blocked by the browser when opened locally.)

Run it in the same folder as lyrics.json:    python make_lyrics_js.py
Run it again any time lyrics.json changes (for example after the merge step).
"""
import json
import os

here = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(here, "lyrics.json"), encoding="utf-8"))

# keep only songs that actually have lyrics, so the file stays smaller
data = {k: v for k, v in data.items() if v.get("synced") or v.get("plain")}

out = os.path.join(here, "lyrics.js")
with open(out, "w", encoding="utf-8") as f:
    f.write("window.LY=")
    json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    f.write(";")

synced = sum(1 for v in data.values() if v.get("synced"))
print(f"Wrote lyrics.js with {len(data)} songs ({synced} synced, {len(data) - synced} plain only).")
print(f"File size: {os.path.getsize(out) / 1024 / 1024:.1f} MB")
