# Dessa bibliotek används för att förenkla livet
from gpiozero import Device, LED, PWMLED, Button
from gpiozero.pins.mock import MockFactory
from unittest.mock import Mock
import pygame.mixer as mixerenhet
import time
import sys
from cowsay import kitty as säger

if sys.platform == 'darwin':
    Device.pin_factory = MockFactory()
    temperatur_läsare = Mock(return_value=(80, 21))
    temperatur_enhet = Mock()
    PWMLED = Mock()
else:
    import Adafruit_DHT
    temperatur_enhet = Adafruit_DHT.DHT11
    temperatur_läsare = Adafruit_DHT.read_retry


# Detta är en s.k. "konstant" variabel bara för göra koden mer lättläst längre ned
EN_SEKUND = 1

# Alla delar (objekt) utav hunden som kommer användas med lättlästa namn
vänster_öga = LED(23)
höger_öga = LED(24)
nos = PWMLED(18)
mun = Button(22)
hörsel = Button(27)
temperatur_pinne = 25

# Detta är i objekt-orienterad-programmering en "klass" som representerar en hund
class Hund():
    def __init__(self, namn):
        # En hund har "egna" egenskaper som inte behöver vara samma för andra hundar
        self.namn = namn
        self.hjärtslag_räknare = 0
        self.födsel_temperatur = self.känn_temperatur()  # Vad är temperaturen vid födsel för att jämföra med senare
        # När vi föder en hund vill vi att den ska veta/göra följande
        hörsel.when_activated = self.apport
        mun.when_activated = self.ät
        säger(f"Vov!!! nu är jag född och jag heter {self.namn}...\n"
              f"Nu när jag föddes så är jag {self.födsel_temperatur} grader")
        mixerenhet.init()
        self.skäll()

    def slå_hjärtslag(self, hjärtslag_per_sekund=10):
        # Denna "metod" bestämmer hur ofta/regelbundet hjärtat ska slå
        time.sleep(EN_SEKUND / hjärtslag_per_sekund)
        self.hjärtslag_räknare = self.hjärtslag_räknare + 1

    def nollställ_hjärtslag(self):
        # Vi använder denna för att bestämma "intervaller" mellan exempelvis hur ofta hunden ska känna på sin päls
        self.hjärtslag_räknare = 0

    def känn_temperatur(self, pinne=temperatur_pinne, antal_försök=10, normal_temp=23):
        # Denna metod/egenskap kommer lära hunden att känna på sin päls
        fuktighet, temperatur = temperatur_läsare(temperatur_enhet, pinne, retries=antal_försök)
        return temperatur or normal_temp

    def dax_att_känna_efter(self, efter_hur_många_hjärtslag=100):
        # Denna metod är enbart för att svara på frågan om det är dags för hunden att känna efter sin päls igen
        self.hjärtslag_räknare = self.hjärtslag_räknare + 1
        if self.hjärtslag_räknare > efter_hur_många_hjärtslag:
            self.nollställ_hjärtslag()
            return True
        else:
            return False

    def blinka_ögonen(self, tid=0.5, antal=6):
        # Denna metod bestämmer hur hunden ska blinka med sina ögon
        vänster_öga.blink(on_time=tid, off_time=tid, n=antal)
        höger_öga.blink(on_time=tid, off_time=tid, n=antal)

    def pulsera_nosen(self, tid_sekunder=1, antal=4):
        # Denna metod bestämmer hur hundens nästa ska pulsera
        nos.pulse(fade_in_time=tid_sekunder, fade_out_time=tid_sekunder, n=antal, background=False)

    def apport(self):
        # Denna metod kallar vi på när vi vill att han ska springa apport
        print(self.namn, 'springer apport 🦴')
        self.blinka_ögonen(0.2, 10)  # Snabbare än vanligt
        self.skäll()

    def ät(self):
        # Denna metod talar om vad som händer när hunden äter
        print(self.namn, 'äter gladligen 🌭')
        self.blinka_ögonen()
        mixerenhet.music.load('ljud/eat.mp3')
        mixerenhet.music.play()

    def skäll(self):
        # Denna metod lär hunden hur han ska låta när han skäller
        mixerenhet.music.load('ljud/vov.mp3')
        mixerenhet.music.play()

    def lev(self, värmeslag_temparatur_ökning=1):
        # Denna metod kallar som sista steg vid "init" (födsel) när valpen börjar leva
        while True:
            self.slå_hjärtslag()  # Vi slår ett hjärtslag
            if self.dax_att_känna_efter() is True:  # Bara om tillräckligt många hjärtslag ska hunden känna efter
                temperatur_just_nu = self.känn_temperatur()  # ... då ska han känna efter temperatur
                print("Grr.. min päls just nu är", temperatur_just_nu, "grader")
                if temperatur_just_nu is not None and temperatur_just_nu >= self.födsel_temperatur + värmeslag_temparatur_ökning:
                    # Om temeperaturen överstiger värmeslag ska vi göra nedan
                    print('🥵')
                    self.pulsera_nosen()


# Här börjar huvud programmet
hugo = Hund(namn='Hugo')  # Vi föder en ny "Hund" med namnet Hugo
hugo.lev()  # Vi talar för hugo att börja leva