raspberry_lab
===============

(Denna sida har många länkar som är enklare att följa/klicka om du istället går till https://bit.ly/2SmYVrj om du läser en pappers-version)

## Grattis David !!!

Vi tänkte till din födelsedag skulle få ett litet "paket" 🎁 för att tillåta dig snickra ihop lite enklare elektronik och programmera för att få en liten känsla över hur enkelt det kan vara om man har intresset 😁

Tänkte att inledningsvis att använda en **Raspberry Pi** 🍓 vore enklaste för detta ändanmål då dels kan använda den som en vanlig dator (skriva kod direkt på den) men har också [GPIO](https://www.raspberrypi.org/documentation/usage/gpio/) pinnar som är nyckeln till detta. Med dessa kan vi både läsa elektroniska signaler (3.3 volt) men också skicka ut signalet vilket är toppen för att styra eller läsa av komponenter.

Som programmerings språk finns det flera valmöjligheter, men jag kommer lura över dig till att använda [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) 🐍 som bara är bland de lättaste språken att börja med, dessutom är ett av det bästa "full-spektrum" (utan begränsningar funktionsmässigt) enligt min mening, vare det handlar om att utveckla applikationer, webtjänster, AI, mattematik, skapa automationer i MineCraft ...  eller styra mikrokontrolenheter eller i detta fall "mikro datorenhet". 

<u>**Så vilka förberedelser behövs för att köra loss med lite experiment utöver det du fått...**</u> 

- En mikrousb laddare (minst 1 ampere) för att få liv i Raspberry Pi
- Hörlurar med vanlig 3,5mm uttag... eller bättre en extern högtalare med 3,5mm sladd ingång

<u>**Bra att ha om du lättare ska kunna komma åt / styra Raspberry Pi**</u>

- TV eller skärm med HDMI
- HDMI-kabel
- Kombinerad tangentbord/mus med USB .... eller en USB-hub (helst med egen strömförsörjning) med tangentbord och mus kopplad till .... detta är för Raspberry Pi har väldigt få USB-portar och undviker enheter som drar hög strömstyrka
- Nätverkssladd (om inte ert wifi fungerar)



### Hur börjar jag kopplar du in Raspberry Pi.... med skärm/tangentbord/mus .. 

Jag skulle föreslå att du kopplar in så att du åtminstone kan använda den som dator antingen genom tangentbord (enklast) och/eller koppla upp från din egna stationära dator (jag går genom senare hur).

Om du använder skärm + dator/mus så är det enda du behöver göra är att titta på skärmen medan den startar upp.

<img src="https://raw.githubusercontent.com/engdan77/project_images/master/uPic/hur_koppla_ihop_raspberrypi.jpg" alt="hur_koppla_ihop_raspberrypi" style="zoom:30%;" />

### Kan jag sitta via min dator och styra Raspberry Pi istället ?? ... Ja !!!

I detta fall så klarar du dig utan både skärm, tangentbord/mus ... men den måste komma in på ert nätverk .. förhoppningsvis har jag lyckats för-konfigurera "wifi" USB stickan med ert wifi och kommer automatiskt koppla upp sig (annar kan du följa [denna](https://www.youtube.com/watch?v=lfHRLLRbErw) video-klipp för fixa detta),  om detta misslyckats så går det utmärkt att koppla en nätverkskabel direkt från Raspberry Pi till er hemma-router (kommer alltid fungera).

Du kommer behöva **IP-addressen** till Raspberry Pi, och enklast är om du har skärmen inkopplad och under uppstart bör du se dess IP-address dyka upp på skärmen, ett annat alternativ om du vet hur du kopplar upp mot din router och läsa av där ... sista alternativet är att använda ett Windows program (gratis) som exempelvis Fing du kan ladda ned [här](https://www.fing.com/products/fing-desktop) som bör kunna "scanna" av ditt nätverk och lura ut detta åt dig.

Sedan från din Mac/Windows dator får du ladda ned RealVNC viewer [härifrån](https://www.realvnc.com/en/connect/download/viewer/windows/).

Sedan kör du detta program och väljer att skapa en koppling mot ovan IP-address, och när den frågar efter ett lösenord anger du

```
username: pi
password: raspberrylab
```

### Var anger jag min kod... Hur kommer jag igång? 🥳

När du antingen använder skärmen eller VNC så bör du fått en kod-editor "mu" som är inlagd att starta automatiskt (finns även i hallon-menyn -> programmering). Från denna vyn, kan du välja "**Nytt**", "**Kör**" som du oftast kommer använda. Alla Python program bör ha filändelsen `.py`

![kod_editor](https://raw.githubusercontent.com/engdan77/project_images/master/uPic/kod_editor.jpg)

### Första exempel med en enkel LED lampa för att bli lite varm i kläderna och få en känsla ...

.. jag skäl ett väldigt enkelt exempel från [denna](https://gpiozero.readthedocs.io/en/stable/recipes.html) sida som har många flera bra exempel att följa jag kan varmt rekommendera att göra...
Du bör ha motstånd (100 ohm) och LED lampa som du ka koppla in som nedan, din modell har färre pinnar (26 st) än bilden visar med de pinnar som visas i dessa exempel ligger på samma plats och med samma nummer så dessa exempel ska fungera lika ..

![forsta_exempel.jpg](https://i.loli.net/2021/06/10/B85pb6zq3DJk9EQ.jpg)



Om du skriver en kod nu som

```python
from gpiozero import LED
from time import sleep

red = LED(17)

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)
```



Och klickar på "**Kör**" ✅ så bör denna lampa blinka till du klickar "**Stop**" 🛑

### Vill du lära dig lite med grundläggande Python programmering innan vi kör vidare ...?

I så fall är det toppen 🙌... och jag kan varm rekommendera denna seria av YouTube klipp som förklarar mycket enkelt det absolut mest grundläggande ..

[Python - Grunder - Del 1 - Variabler och listor](https://www.youtube.com/watch?v=iUpCT-oCu1U&t=1637s)

[Python - Grunder - Del 2 - Villkor och loopar](https://www.youtube.com/watch?v=SVBVvtTycFc&t=2221s)

[Python - Grunder - Del 3 - Funktioner](https://www.youtube.com/watch?v=26ciA4FmYfI)

[Python svenska - 18 - Klasser och metoder](https://www.youtube.com/watch?v=iJVk_3H1Rvg)  *(detta är nog lite överkurs men för mitt experiment nedan bra att ha kläm på)*

Nu har du lite kläm på Python som språk ... 



### Vill du bekanta dig lite mer med gpiozero biblioteket, hur du använder Python för att styra GPIO pinnar ...?

Toppen, då kan jag rekommendera denna video nedan ..  📼

[Raspberry Pi - Control GPIO Pins with GPIOzero Library](https://www.youtube.com/watch?v=8N-5rEclspw)

... du bör nu har du nog fått lite kläm på hur man kan snacka med saker med Python .. och du kan gå vidare och experimentera vidare på egen hand ... 



### Vilka mer roliga sensorer och komponenter har du att leka med i leklådan..?

Jo .. du har dessa och med följande exempel du kan testa med

- [LED](https://gpiozero.readthedocs.io/en/stable/recipes.html#led)
- [Tryck knapp](https://gpiozero.readthedocs.io/en/stable/recipes.html#button)
- [Ljus sensor](https://gpiozero.readthedocs.io/en/stable/recipes.html#light-sensor)
- [Avståndsmätare](https://gpiozero.readthedocs.io/en/stable/recipes.html#distance-sensor)
- [Ljud sensor](https://www.youtube.com/watch?v=GiXNUYPrQ7I)
- [DHT11 (temperatur/fuktighet) sensor](https://www.youtube.com/watch?v=KUr8WgSIsfk)
- [Reed-switch](https://medium.com/conectric-networks/playing-with-raspberry-pi-door-sensor-fun-ab89ad499964) (dörr sensor)
- Sladdar, motstånd, kondensator

Om du saknar nåt rekommenderar jag [Kjell & Company](https://www.kjell.com/se) eller [AliExpress](https://www.aliexpress.com/) 🤑



### Vill du ge dig på något mer avancerat ....?

Om du följer kopplings schemat nedan samt kod exemplet nedan som du kan jobba vidare på, så har du lyckats utvecklat en **tamagotchi-hugo** .. 🐶 + 🤖

<img src="https://raw.githubusercontent.com/engdan77/project_images/master/uPic/tamagotchi.png" alt="tamagotchi" style="zoom:50%;" /><img src="/Users/edo/git/my/raspberry_lab/dokument/hugo.png" alt="hugo" style="zoom:50%;" /


Koppla nedan ...

![hund_elektronik](https://raw.githubusercontent.com/engdan77/project_images/master/uPic/hund_elektronik.png)


PS. "motståndet" mot den blåa "temperatur-sensor" ska vara det motstånd som är på 47 Kohm (starkare), du har en uppmärkt för detta.
Det motstånd du har för LED är de svagare som vi inte har markerat upp och bör vara på 100 ohm eller nåt.

... och med nedan kod som är lite mer komplext, men har försökt använda så enkel lätt-läst kod så tror att även om inte alla pusselbitar faller på plats så kommer det mesta visa sig självförklarande .. det fina med Python 😏👍🏻

```python
# Dessa bibliotek används för att förenkla livet
from gpiozero import Device, LED, PWMLED, Button
from gpiozero.pins.mock import MockFactory
from unittest.mock import Mock
import pygame.mixer as mixerenhet
import time
import sys
from cowsay import kitty as säger

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
        hörsel.when_activated = self.apport  # Detta är en s.k. "callback" säger att den hörsel (ljud sensor) registreras ska han "apport"
        mun.when_activated = self.ät  # Detta är motsvarande när hunden matas (knappen) så ska han köra metoden "ät"
        säger(f"Vov!!! nu är jag född och jag heter {self.namn}...\n"
              f"Nu när jag föddes så är jag {self.födsel_temperatur} grader")
        mixerenhet.init()  # Detta är bara för att initiera ljudenheten på Raspberry Pi
        self.skäll()  # Ge ett skall

    def slå_hjärtslag(self, hjärtslag_per_sekund=10):
        # Denna "metod" bestämmer hur ofta/regelbundet hjärtat ska slå, högre = högre hastighet på räknaren
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
        # Denna metod är enbart för att svara på frågan om det är dags för hunden att känna efter sin päls igen baserad på vår "räknare" vi ökar resp. nollställer vid behov
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
        mixerenhet.music.load('ljud/eat.mp3')  # Detta spelar upp ljudet "eat.mp3" som ska ligga i katalogen ljud
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


# Här börjar huvud programmet ... NU KÖR VI !!!!
hugo = Hund(namn='Hugo')  # Vi föder en ny "Hund" med namnet Hugo
hugo.lev()  # Vi talar för hugo att börja leva .... "It's ALIIIIIIVE ... " (citat från "Frankenstein") 🧛
```



... nu .. detta är bara en början .. med de sensors som du har i arsinalen bör du antingen kunna börja nytt projekt eller lägga till flera egenskaper till en Hugo version 2.0 ... 3.0 ...  🤓

Vill du tjuvtitta så har du ett YouTube klipp [här](https://youtu.be/hQaHrYlHHQU) hur det hela blev ...

![hugo_animation](https://raw.githubusercontent.com/engdan77/project_images/master/uPic/hugo_animation.gif)





Lite tips på andra projekt du kanske går snickra på med de dela du fått .. 💡

- Inbrottslarm? Vi kan skicka mail (jag kan ge dig tips hur) när detta sker
- Läsa av avståndet när bilen är parkerad hemma?
- Skicka en väck signal när det blir tillräckligt ljust i rummet?


Ha kul .... 🎊



