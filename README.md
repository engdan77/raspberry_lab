raspberry_lab
===============

## Grattis David !!!

Vi tänkte till din födelsedag skulle få ett litet "paket" för att tillåta dig snickra ihop lite enklare elektronik och programmera för att få en liten känsla över hur enkelt det kan vara om man har intresset 😁

Tänkte att inledningsvis att använda en Raspberry Pi 🍓 vore enklaste för detta ändanmål då dels kan använda den som en vanlig dator (skriva kod direkt på den) men har också [GPIO](https://www.raspberrypi.org/documentation/usage/gpio/) pinnar som är nyckeln till detta. Med dessa kan vi både läsa elektroniska signaler (3.3 volt) men också skicka ut signalet vilket är toppen för att styra eller läsa av komponenter.

Som programmerings språk finns det flera valmöjligheter, men jag kommer lura över dig till att använda [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) 🐍 som bara är bland de lättaste språken att börja med, dessutom är ett av det bästa "full-spektrum" (utan begränsningar funktionsmässigt) enligt min mening, vare det handlar om att utveckla applikationer, webtjänster, AI, mattematik eller mikrokontrolenheter. 

Så vilka förberedelser behövs för att köra loss med lite experiment utöver det du fått... 

- En mikrousb laddare (minst 1 ampere) för att få liv i Raspberry Pi
- Hörlurar med vanlig 3,5mm uttag... eller bättre en extern högtalare med 3,5mm sladd ingång

Bra att ha om du lättare ska kunna komma åt / styra Raspberry Pi

- TV eller skärm med HDMI
- HDMI-kabel
- Kombinerad tangentbord/mus med USB .... eller en USB-hub (helst med egen strömförsörjning) med tangentbord och mus kopplad till .... detta är för Raspberry Pi har väldigt få USB-portar och undviker enheter som drar hög strömstyrka
- Nätverkssladd (om inte ert wifi fungerar)

<img src="/Users/edo/git/my/raspberry_lab/dokument/hur_koppla_ihop_raspberrypi.jpg" alt="hur_koppla_ihop_raspberrypi" style="zoom:30%;" />

### Hur börjar jag kopplar du in Raspberry Pi.... med skärm/tangentbord/mus .. 

Jag skulle föreslå att du kopplar in så att du åtminstone kan använda den som dator antingen genom tangentbord (enklast) och/eller koppla upp från din egna stationära dator (jag går genom senare hur).

Om du använder skärm + dator/mus så är det enda du behöver göra är att titta på skärmen medan den startar upp.

### Kan jag sitta via min dator och styra Raspberry Pi istället ?? ... Ja !!!

I detta fall så klarar du dig utan både skärm, tangentbord/mus ... men den måste komma in på ert nätverk .. förhoppningsvis har jag lyckats för-konfigurera "wifi" USB stickan med ert wifi och kommer automatiskt koppla upp sig,  om detta misslyckats så går det utmärkt att koppla en nätverkskabel direkt från Raspberry Pi till er hemma-router (kommer alltid fungera).

Du kommer behöva IP-addressen till Raspberry Pi, och enklast är om du har skärmen inkopplad och under uppstart bör du se dess IP-address dyka upp på skärmen, ett annat alternativ om du vet hur du kopplar upp mot din router och läsa av där ... sista alternativet är att använda ett Windows program (gratis) som exempelvis Fing du kan ladda ned [här](https://www.fing.com/products/fing-desktop).

Sedan från din Mac/Windows dator får du ladda ned RealVNC [härifrån](https://www.realvnc.com/en/connect/download/viewer/windows/).

Sedan kör du detta program och väljer att skapa en koppling mot ovan IP-address, och när den frågar efter ett lösenord anger du

```
username: pi
password: raspberrylab
```

 ![kod_editor](/Users/edo/git/my/raspberry_lab/dokument/kod_editor.jpg)

### Var anger jag min kod...?

När du antingen använder skärmen eller VNC så bör du fått en kod-editor "mu" som är inlagd att starta automatiskt.
Från denna vyn, kan du välja "**Nytt**", "**Kör**" som du oftast kommer använda. Alla Python program bör ha filändelsen `.py`

### Första exempel för att bli lite varm i kläderna ...

.. jag skäl ett väldigt enkelt exempel från [denna](https://gpiozero.readthedocs.io/en/stable/recipes.html) sida som har många flera bra exempel att följa ...
Du bör ha motstånd (100 ohm) och LED lampa som du ka koppla in som nedan, din modell har färre pinnar (26 st) än bilden visar med de pinnar som visas i dessa exempel ligger på samma plats och med samma nummer så dessa exempel ska fungera lika ..

![forsta_exempel](/Users/edo/git/my/raspberry_lab/dokument/forsta_exempel.jpg)

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



Och klickar på "**Kör**" så bör denna lampa blinka till du klickar "**Stop**"

### Vill du lära dig lite med grundläggande Python programmering innan vi kör vidare ...?

I så fall är det toppen 🙌... och jag kan varm rekommendera denna seria av YouTube klipp som förklarar mycket enkelt det absolut mest grundläggande ..

[Python - Grunder - Del 1 - Variabler och listor](https://www.youtube.com/watch?v=iUpCT-oCu1U&t=1637s)
[Python - Grunder - Del 2 - Villkor och loopar](https://www.youtube.com/watch?v=SVBVvtTycFc&t=2221s)
[Python - Grunder - Del 3 - Funktioner](https://www.youtube.com/watch?v=26ciA4FmYfI)
[Python svenska - 18 - Klasser och metoder](https://www.youtube.com/watch?v=iJVk_3H1Rvg)

Nu har du lite kläm på Python som språk ... 

### Vill du bekanta dig lite mer med gpiozero, hur du använder Python för att styra GPIO pinnar ...?

Toppen, då kan jag rekommendera denna 🤪
[Raspberry Pi - Control GPIO Pins with GPIOzero Library](https://www.youtube.com/watch?v=8N-5rEclspw)
... nu har du nog fått lite kläm på hur man kan snacka med saker med Python .. 


Vilka mer roliga sensorer och komponenter har du att leka med i leklådan..?

Jo .. du har dessa och med följande exempel du kan testa med

- [LED](https://gpiozero.readthedocs.io/en/stable/recipes.html#led)
- [Tryck knapp](https://gpiozero.readthedocs.io/en/stable/recipes.html#button)
- [Ljus sensor](https://gpiozero.readthedocs.io/en/stable/recipes.html#light-sensor)
- [Avståndsmätare](https://gpiozero.readthedocs.io/en/stable/recipes.html#distance-sensor)
- [Ljud sensor](https://www.youtube.com/watch?v=GiXNUYPrQ7I)
- [DHT11 (temperatur/fuktighet) sensor](https://www.youtube.com/watch?v=KUr8WgSIsfk)
- Sladdar, motstånd, kondensator

Om du saknar nåt rekommenderar jag [Kjell & Company](https://www.kjell.com/se) eller [AliExpress](https://www.aliexpress.com/) 🤑

### Vill du ge dig på något mer avancerat ....?

Om du följer kopplings schemat nedan samt kod exemplet nedan som du kan jobba vidare på, så har du lyckats utvecklat en **tamagotchi-hugo** .. 😅🐶

<img src="/Users/edo/git/my/raspberry_lab/dokument/tamagotchi.png" alt="tamagotchi" style="zoom:50%;" /><img src="/Users/edo/git/my/raspberry_lab/dokument/hugo.png" alt="hugo" style="zoom:50%;" />

Koppla nedan ...

![hund_elektronik](/Users/edo/git/my/raspberry_lab/dokument/hund_elektronik.png)



... och med nedan kod som är lite mer komplext, men har försökt använda så enkel lätt-läst kod så tror att även om inte alla pusselbitar faller på plats så kommer det mesta visa sig självförklarande .. det fina med Python 😏👍🏻

```python
```









