from gpiozero import Device, LED, PWMLED, Button
from gpiozero.pins.mock import MockFactory
from unittest.mock import Mock
import time
import sys
from cowsay import kitty as säger
from playsound import playsound as spela_ljud

if sys.platform == 'darwin':
    Device.pin_factory = MockFactory()
    temperatur_läsare = Mock(return_value=(80, 21))
    temperatur_enhet = Mock()
    PWMLED = Mock()
else:
    import Adafruit_DHT.DHT11 as temperatur_enhet
    import Adafruit_DHT.read_retry as temperatur_läsare

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
        säger("Vov!!! jag heter", self.namn)
        self.skäll()

    def slå_hjärtslag(self, hjärtslag_per_sekund=10):
        time.sleep(EN_SEKUND / hjärtslag_per_sekund)
        self.hjärtslag_räknare = self.hjärtslag_räknare + 1

    def nollställ_hjärtslag(self):
        self.hjärtslag_räknare = 0

    def känn_temperatur(self, pinne=temperatur_pinne):
        fuktighet, temperatur = temperatur_läsare(temperatur_enhet, pinne)
        return temperatur

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

    def pulsera_nosen(self, antal=4):
        nos.pulse(n=antal)

    def apport(self):
        print('🦴')
        self.blinka_ögonen(0.2, 10)  # Snabbare än vanligt
        self.skäll()

    def ät(self):
        print('🌭')
        self.blinka_ögonen()
        spela_ljud('ljud/eat.mp3')

    def skäll(self):
        spela_ljud('ljud/vov.wav')

    def lev(self, värmeslag_temparatur_ökning=2):
        while True:
            self.slå_hjärtslag()
            if self.dax_att_känna_efter() is True:
                temperatur_just_nu = self.känn_temperatur()
                print(self.namn, "känner att hans päls just nu är är", temperatur_just_nu, "grader")
                if temperatur_just_nu > temperatur_just_nu + värmeslag_temparatur_ökning:
                    print('🥵') and self.pulsera_nosen()


if __name__ == '__main__':
    hugo = Hund(namn='Hugo')
    hugo.lev()