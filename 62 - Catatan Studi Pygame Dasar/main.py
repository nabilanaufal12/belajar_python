# Catatan Studi Pygame Dasar

# 1. Inisialisasi Pygame dan Jendela Tampilan
import pygame

pygame.init() # Inisialisasi Pygame
isRun = True # var running game
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar, window_panjang))

# Setup Object Game (Kotak)
x = 250
y = 250
lebar_kotak = 20
panjang_kotak = 20
speed = 5

# 2. Game Loop dan Penanganan Event

while isRun:
    pygame.time.delay(10)
    for event in pygame.event.get(): # Ambil semua event
        if event.type == pygame.QUIT: # Jika event adalah QUIT
            isRun = False # Hentikan loop

    # 4. Input Keyboard dan Pergerakan Objek
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < window_lebar - lebar_kotak:
        x += speed
    if keys[pygame.K_DOWN] and y < window_panjang - panjang_kotak:
        y += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    
    # 3. Menggambar Objek dan Latar Belakang
    window.fill((255, 255, 255)) # Latar belakang putih
    pygame.draw.rect(window, (255, 120, 0), (x, y, lebar_kotak, panjang_kotak)) # Gambar kotak
    
    # 5. Memperbarui Tampilan (Display Update)
    pygame.display.update()

pygame.quit()