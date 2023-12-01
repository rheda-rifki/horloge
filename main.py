import time
import keyboard

heure_actuelle = (21, 00, 00 )
heure_reveil = (21, 45, 00)

def alarme(heure_reveil, heure_actuelle):
    if heure_actuelle == heure_reveil:
        print("Leve toi va courir toute ta vie !!")

def format_12h(h, m, s):
    am_pm = "AM" if h < 12 else "PM"
    h = h % 12
    h = 12 if h == 0 else h
    return f"{h:02d}:{m:02d}:{s:02d} {am_pm}"

def afficher_heure(heure_actuelle):
    global en_pause
    en_pause = False
    keyboard.on_press_key('space', on_space)

    format_choisi = input("Choisissez le format d'heure (12H ou 24H) : ")
    print("Pour mettre l'horloge en pause appuyez sur votre barre espace.")

    h, m, s = heure_actuelle
    while True:
        try:
            if en_pause:
                time.sleep(0.1)
                continue

            alarme(heure_reveil, (h, m, s))

            if format_choisi == "12H":
                heure = format_12h(h, m, s)
            elif format_choisi == "24H":
                heure = f"{h:02d}:{m:02d}:{s:02d}"
            else:
                print("Format non valide, utilisation du format 24h par défaut")
                heure = f"{h:02d}:{m:02d}:{s:02d}"

            print(heure, end="\r")
            s += 1

            if s == 60:
                s = 0
                m += 1
                if m == 60:
                    m = 0
                    h += 1
                    if h == 24:
                        h = 0

            time.sleep(1)
        except KeyboardInterrupt:
            break

def espace(keyboard_event):
    global en_pause
    if keyboard_event.event_type == keyboard.KEY_DOWN:
        en_pause = not en_pause

# test
afficher_heure(heure_actuelle)