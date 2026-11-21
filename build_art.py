"""Local painter (NOT used at runtime): renders entry.png with PIL + DejaVu.
Runtime main.py only copies the embedded PNG (pure stdlib)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, random
W = H = 1024
random.seed(7)
img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)
# soft studio gradient: warm light grey top -> near white floor
for y in range(H):
    t = y / H
    r = int(232 - 18*t); g = int(230 - 16*t); b = int(228 - 12*t)
    d.line([(0, y), (W, y)], fill=(r, g, b))
# subtle radial glow behind product
glow = Image.new("RGB", (W, H), (0,0,0))
gd = ImageDraw.Draw(glow)
gd.ellipse([212, 120, 812, 820], fill=(255, 255, 255))
glow = glow.filter(ImageFilter.GaussianBlur(120))
img = Image.blend(img, Image.composite(glow, Image.new("RGB",(W,H),(255,255,255)), glow.convert("L").point(lambda v: v//4)), 0.5)
d = ImageDraw.Draw(img, "RGBA")
# floor line + soft shadow
d.rectangle([0, 800, W, H], fill=(226, 224, 222))
d.line([0, 800, W, 800], fill=(205, 203, 200), width=2)
sh = Image.new("RGBA", (W, H), (0,0,0,0))
sd = ImageDraw.Draw(sh)
sd.ellipse([300, 790, 724, 850], fill=(60, 55, 50, 90))
sh = sh.filter(ImageFilter.GaussianBlur(18))
img.paste(Image.alpha_composite(img.convert("RGBA"), sh), (0, 0))
d = ImageDraw.Draw(img, "RGBA")
cx, cy = 512, 470  # sphere centre
# ---- chrome stand / base ----
d.rounded_rectangle([392, 700, 632, 800], radius=18, fill=(176, 180, 186), outline=(120, 124, 130), width=3)
d.rounded_rectangle([392, 700, 632, 724], radius=12, fill=(205, 208, 213))
d.rectangle([452, 668, 572, 706], fill=(150, 154, 160), outline=(110, 114, 120), width=2)
# ---- swirling accretion ring (behind sphere) ----
for i in range(260):
    a = random.uniform(0, 2*math.pi)
    rr = random.uniform(150, 235)
    x = cx + rr*math.cos(a)*1.35; y = cy + 40 + rr*math.sin(a)*0.42
    s = random.uniform(2, 7)
    col = random.choice([(124, 92, 220, 200), (168, 130, 255, 200), (90, 160, 255, 180), (255, 170, 220, 160)])
    d.ellipse([x-s, y-s, x+s, y+s], fill=col)
ring = Image.new("RGBA", (W, H), (0,0,0,0))
rd = ImageDraw.Draw(ring)
rd.ellipse([cx-300, cy-95, cx+300, cy+175], outline=(150, 110, 255, 220), width=14)
rd.ellipse([cx-300, cy-95, cx+300, cy+175], outline=(220, 190, 255, 160), width=5)
ring = ring.filter(ImageFilter.GaussianBlur(2))
img.paste(Image.alpha_composite(img.convert("RGBA"), ring), (0, 0))
d = ImageDraw.Draw(img, "RGBA")
# ---- the black sphere (event horizon) ----
d.ellipse([cx-150, cy-150, cx+150, cy+150], fill=(8, 8, 12), outline=(40, 40, 52), width=3)
# glossy highlight
hl = Image.new("RGBA", (W, H), (0,0,0,0))
hd = ImageDraw.Draw(hl)
hd.ellipse([cx-115, cy-125, cx-5, cy-15], fill=(255, 255, 255, 70))
hd.ellipse([cx+60, cy+70, cx+120, cy+120], fill=(140, 120, 255, 50))
hl = hl.filter(ImageFilter.GaussianBlur(12))
img.paste(Image.alpha_composite(img.convert("RGBA"), hl), (0, 0))
d = ImageDraw.Draw(img, "RGBA")
# purple rim light on sphere edge
d.arc([cx-150, cy-150, cx+150, cy+150], start=200, end=340, fill=(170, 130, 255, 220), width=6)
# ---- the key being sucked in (one accessory) ----
key = Image.new("RGBA", (300, 120), (0,0,0,0))
kd = ImageDraw.Draw(key)
kd.ellipse([18, 30, 78, 90], outline=(176, 138, 40, 255), width=10)   # bow
kd.ellipse([32, 44, 64, 76], outline=(176, 138, 40, 255), width=6)
kd.rectangle([74, 52, 250, 68], fill=(196, 158, 52, 255))               # shaft
kd.rectangle([218, 68, 234, 92], fill=(196, 158, 52, 255))             # teeth
kd.rectangle([244, 68, 258, 84], fill=(196, 158, 52, 255))
key = key.rotate(-38, expand=True, resample=Image.BICUBIC)
# motion arcs trailing the key
for r, a0 in [(205, -70), (225, -55), (245, -40)]:
    d.arc([cx-r, cy-r//2-40, cx+r, cy+r//2+60], start=a0, end=a0+55, fill=(150, 130, 220, 170), width=4)
img.paste(key, (cx+150, cy-330), key)
d = ImageDraw.Draw(img, "RGBA")
# small sparks near horizon
for i in range(26):
    a = random.uniform(0, 2*math.pi)
    rr = random.uniform(150, 175)
    x = cx + rr*math.cos(a); y = cy + rr*math.sin(a)
    d.ellipse([x-2, y-2, x+2, y+2], fill=(230, 210, 255, 230))
# ---- product label plate on base ----
d.rounded_rectangle([412, 736, 612, 782], radius=8, fill=(245, 244, 242), outline=(150, 148, 145), width=2)
# ---- text (DejaVu, local only) ----
def font(sz, bold=False):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else "")
    try: return ImageFont.truetype(p, sz)
    except Exception: return ImageFont.load_default()
d.text((512, 84), "NOVA APPLIANCES", font=font(30), fill=(90, 88, 86), anchor="ma")
d.text((512, 118), "CATALOGUE  No. 7  —  IMPOSSIBLE GADGETS", font=font(20), fill=(130, 128, 126), anchor="ma")
d.text((512, 748), "POCKET BLACK HOLE", font=font(22, bold=True), fill=(40, 38, 36), anchor="ma")
d.text((512, 772), "BH-01  ·  $49.99", font=font(16), fill=(110, 108, 106), anchor="ma")
d.text((512, 900), "ONE KEY AT A TIME.", font=font(22), fill=(120, 118, 116), anchor="ma")
img.save("/home/hatch/workspace/makefun-kit/catalogue-kit/repo/entry.png", optimize=True)
print("saved")
