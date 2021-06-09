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

EN_SEKUND = 1

vänster_öga = LED(23)
höger_öga = LED(24)
nos = PWMLED(18)
mun = Button(22)
hörsel = Button(27)
temperatur_pinne = 25


class Hund():
    def __init__(self, namn):
        self.namn = namn
        self.hjärtslag_räknare = 0
        self.födsel_temperatur = self.känn_temperatur()
        hörsel.when_activated = self.apport
        mun.when_activated = self.ät
        säger(f"Vov!!! nu är jag född och jag heter {self.namn}...\n"
              f"Nu när jag föddes så är jag {self.födsel_temperatur} grader")
        mixerenhet.init()
        self.skäll()

    def slå_hjärtslag(self, hjärtslag_per_sekund=10):
        time.sleep(EN_SEKUND / hjärtslag_per_sekund)
        self.hjärtslag_räknare = self.hjärtslag_räknare + 1

    def nollställ_hjärtslag(self):
        self.hjärtslag_räknare = 0

    def känn_temperatur(self, pinne=temperatur_pinne, antal_försök=10, normal_temp=23):
        fuktighet, temperatur = temperatur_läsare(temperatur_enhet, pinne, retries=antal_försök)
        return temperatur or normal_temp

    def dax_att_känna_efter(self, efter_hur_många_hjärtslag=100):
        self.hjärtslag_räknare = self.hjärtslag_räknare + 1
        if self.hjärtslag_räknare > efter_hur_många_hjärtslag:
            self.nollställ_hjärtslag()
            return True
        else:
            return False

    def blinka_ögonen(self, tid=0.5, antal=6):
        vänster_öga.blink(on_time=tid, off_time=tid, n=antal)
        höger_öga.blink(on_time=tid, off_time=tid, n=antal)

    def pulsera_nosen(self, tid_sekunder=1, antal=4):
        nos.pulse(fade_in_time=tid_sekunder, fade_out_time=tid_sekunder, n=antal, background=False)

    def apport(self):
        print(self.namn, 'springer apport 🦴')
        self.blinka_ögonen(0.2, 10)  # Snabbare än vanligt
        self.skäll()

    def ät(self):
        print(self.namn, 'äter gladligen 🌭')
        self.blinka_ögonen()
        mixerenhet.music.load('ljud/eat.mp3')
        mixerenhet.music.play()

    def skäll(self):
        mixerenhet.music.load('ljud/vov.mp3')
        mixerenhet.music.play()

    def lev(self, värmeslag_temparatur_ökning=1):
        while True:
            self.slå_hjärtslag()
            if self.dax_att_känna_efter() is True:
                temperatur_just_nu = self.känn_temperatur()
                print("Grr.. min päls just nu är", temperatur_just_nu, "grader")
                if temperatur_just_nu is not None and temperatur_just_nu >= self.födsel_temperatur + värmeslag_temparatur_ökning:
                    print('🥵')
                    self.pulsera_nosen()


if __name__ == '__main__':
    hugo = Hund(namn='Hugo')
    hugo.lev()