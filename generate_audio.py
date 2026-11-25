from pathlib import Path
from gtts import gTTS
import time

folder = Path(__file__).resolve().parent / "audio"
folder.mkdir(exist_ok=True)
words = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
def thai(n):
    if n == 100: return "หนึ่งร้อย"
    if n < 10: return words[n]
    t, o = divmod(n, 10)
    return ("สิบ" if t == 1 else "ยี่สิบ" if t == 2 else words[t] + "สิบ") + ("เอ็ด" if o == 1 else words[o])

for n in range(1, 101):
    target = folder / f"{n}.mp3"
    if target.exists() and target.stat().st_size: continue
    temp = target.with_suffix(".tmp")
    for attempt in range(3):
        try:
            gTTS(thai(n), lang="th").save(str(temp))
            temp.replace(target)
            time.sleep(0.5)
            break
        except Exception:
            if attempt == 2: raise
            time.sleep(3 * (attempt + 1))
    print(n, thai(n))
