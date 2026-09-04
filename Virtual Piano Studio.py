import pygame
import datetime  # Ditambahkan untuk mencatat waktu/jam bermain

pygame.init()
pygame.mixer.init()

WIDTH = 1150
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virtual Piano Studio - With History")

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (200,200,200)
RED = (255,0,0)

font = pygame.font.SysFont("timesnewroman", 24)

# =====================
# Inisialisasi Suara
# =====================
notes = {
    "C4":"assets/notes/C4.wav",
    "D4":"assets/notes/D4.wav",
    "E4":"assets/notes/E4.wav",
    "F4":"assets/notes/F4.wav",
    "G4":"assets/notes/G4.wav",
    "A4":"assets/notes/A4.wav",
    "B4":"assets/notes/B4.wav",
    "C5":"assets/notes/C5.wav"
}

sounds = {}
for note,path in notes.items():
    sounds[note] = pygame.mixer.Sound(path)

# =====================
# Kunci Piano
# =====================
white_keys = []
start_x = 50

for i,note in enumerate(notes.keys()):
    rect = pygame.Rect(start_x+i*120,150,120,300)
    white_keys.append((rect,note))

# =====================
# KEYBOARD MAP
# =====================
key_map = {
    pygame.K_z:"C4",
    pygame.K_x:"D4",
    pygame.K_c:"E4",
    pygame.K_v:"F4",
    pygame.K_b:"G4",
    pygame.K_n:"A4",
    pygame.K_m:"B4",
    pygame.K_e:"C5"
}

current_note = ""

# ==========================================
# STRUKTUR ARRAY 2D & FUNGSI RIWAYAT TEXT
# ==========================================
# Array 2D ini akan menyimpan data berbentuk: [ [waktu, nada], [waktu, nada] ]
history_log = [] 
file_riwayat = "riwayat_bermain.txt"
waktu_buka = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Tulis tanda sesi baru ke file teks
with open(file_riwayat, "a") as file:
    file.write(f"\n=========================================\n")
    file.write(f" Waktu Buka: {waktu_buka}\n")

def catat_riwayat(waktu_lengkap):
    # Ambil tanggal dan jam lengkap saat tombol ditekan
    waktu_lengkap = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Tetap masukkan ke Array 2D history_log di memori (jika sewaktu-waktu butuh data arraynya)
    data_baru = [waktu_lengkap]
    history_log.append(data_baru)

# =====================
# PLAY NOTE
# =====================
def play_note(note):

    global current_note

    sounds[note].play()

    current_note = note
    
    # PANGGIL FUNGSI RIWAYAT DI SINI
    catat_riwayat(note)


running = True
while running:
    screen.fill((240,240,240))

    title = font.render("Virtual Piano Studio", True, BLACK)
    screen.blit(title,(20,20))

    info = font.render(
        "Z=C4, X=D4, C=E4, V=F4, B=G4, N=A4, M=B4, E=C5",
        True,
        BLACK
    )
    screen.blit(info,(20,60))

    note_text = font.render(f"Current Note: {current_note}", True, RED)
    screen.blit(note_text,(20,100))

    # Teks pemberitahuan riwayat di layar
    fitur_text = font.render("(Setiap nada yang ditekan otomatis tercatat di riwayat_bermain.txt)", True, (100,100,100))
    screen.blit(fitur_text, (20, 460))

    for rect,note in white_keys:
        pygame.draw.rect(screen,WHITE,rect)
        pygame.draw.rect(screen,BLACK,rect,2)
        text = font.render(note,True,BLACK)
        screen.blit(text, (rect.x+35,rect.y+260))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in key_map:
                play_note(key_map[event.key])
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for rect,note in white_keys:
                if rect.collidepoint(mouse_pos):
                    play_note(note)

pygame.quit()