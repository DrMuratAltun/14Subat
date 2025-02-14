import math
import colorsys
from turtle import *

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * \
           math.cos(2*k) - 2 * \
           math.cos(3*k) - \
           math.cos(4*k)

# Turtle ayarları
setup(1280, 720)  # Pencere boyutu
speed(0)          # En yüksek çizim hızı
bgcolor("black")  # Siyah arka plan
pensize(2)        # Başlangıç çizgi kalınlığı
hideturtle()      # Kursörü gizle
tracer(10)        # Çizim hızını artırma

# Kalp çizim döngüsü
for i in range(6000):
    # Gökkuşağı renk geçişi
    hue = i / 25  # Renk değişim hızını ayarla
    rgb = colorsys.hsv_to_rgb(hue%360/360, 0.8, 1.0)
    color(rgb)
    
    # Dinamik çizgi kalınlığı
    pensize(abs(math.sin(i/30)) * 4 + 1)
    
    # Kalp koordinatlarına hareket
    goto(hearta(i) * 20, heartb(i) * 20)
    
    # Merkeze dönüş (yıldız efekti için)
    if i % 50 == 0:
        goto(0,0)
        update()  # Ara çıktıları göster

# Çizimi tamamla
update()
done()