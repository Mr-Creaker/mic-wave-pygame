from pygame import *   
import sounddevice as sd
import scipy.io.wavfile as wav 
import random
# === Налаштування ===
fs = 44100     # Частота дискретизації (кількість вимірів за секунду)
chunk = 1024   # Кількість семплів (відліків) за один кадр
width, height = 800, 400  
track = ["mic-wave-pygame\\Calvin Harris feat. Pharrell Williams, Katy Perry & Big Sean - Feels.mp3"
        ,"mic-wave-pygame\\Pharrell Williams - Happy.mp3"]


init()
screen = display.set_mode((width, height))
display.set_caption("Live Audio (Mic)")
mytrack=random.choice(track)
mixer.music.load(mytrack)
mixer.music.play()
clock = time.Clock()

btn = Rect(400,200,350,80)
rect_color ="white"
btn_text ="Запис"
f= font.SysFont("Arial",32)
def startRecord():
    global recording
    recording= sd.rec(int(fs*3),samplerate=fs,channels=2,dtype="float32")
def stopRecord():
    global recording
    sd.stop()
    if recording is not None:
        wav.write("mywav.wav",fs,recording)
def play_wav_and_voice():
    mixer.music.load(mytrack)
    mixer.music.play()
    myvoice =mixer.Sound("mywav.wav")
    myvoice.play()

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            if btn.collidepoint(e.pos):
                rect_color = "red"
                btn_text="СТОП"
                is_recording =True
                mixer.music.load(mytrack)
                mixer.music.play()
                startRecord()
            else:
                rect_color = "white"
                btn_text="Запис"
                is_recording =False
                stopRecord()
                play_wav_and_voice()

    screen.fill((0, 0, 0))
    draw.rect(screen,rect_color,btn)
    text_suface =f.render(btn_text,True,"black")
    screen.blit(text_suface,(btn.rect.x+20,btn.rect.y+20))

    display.update()
    clock.tick(60)

quit()
