import math
from turtle import *
import colorsys
def hearta(k):
    return 15 * math.sin(k)**3
def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)
# Turtle ayarları
setup(1280, 720)
bgcolor("black")
speed(5)
pensize(2)
hideturtle()
tracer(5)
delay(0.01)
# Renk parametreleri
color_depth = 0.7
for i in range(6000):
    # Renk hesaplama (düzeltildi)
    hue = 0.0  # Tam kırmızı
    saturation = max(0.3, min(color_depth + 0.3 * math.sin(i/50), 1.0))  # 0.3-1.0 arası
    value = max(0.3, min(0.5 + 0.5 * math.sin(i/100), 1.0))  # 0.3-1.0 arası
    
    # HSV'den RGB'ye dönüşüm (düzeltildi)
    rgb = colorsys.hsv_to_rgb(
        min(max(hue, 0.0), 1.0),
        min(max(saturation, 0.0), 1.0),
        min(max(value, 0.0), 1.0)
    )
    color(rgb)
    
    # Çizgi kalınlığı
    pensize(abs(math.sin(i/40)) * 3 + 1)
    
    # Kalp çizimi
    goto(hearta(i) * 20, heartb(i) * 20)
    
    # Merkeze dönüş efekti
    if i % 75 == 0:
        goto(0,0)
        update()

update()
done()