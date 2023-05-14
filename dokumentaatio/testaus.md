# Testausdokumentti

## Käyttöliittymä
Käyttöliittymää on testattu manuaalisesti. Käyttäjä ei voi virheellisiä syötteitä syöttämällä, tai muutenkaan aiheuttaa virhetilannetta sovelluksessa.

## Sovelluslogiikka
Sovelluslogiikasta vastaavalle luokalle Tool on kirjoitettu kattavat testit testiluokassa test_tool. Test_tool luokan testit kattavat kaikki mahdolliset pelitilanteet ja luokan Tool metodien toiminnan. Myös sovelluslogiikan käyttämät oliot Card, Deck, ja Player on testattu kattavasti vastaavasti testiluokissaan test_card, test_deck ja  test_player.

## Testikattavuus
Alla on kuvakaappaus coverage-report komennon generoimasta testikattavuusraportista. Testikattavuusraportissa ei testata käyttöliittymää, käyttöliittymä on testattu manuaalisesti.

![Testikattavuusraportti](https://github.com/ogvirtan/ot-harjoitustyo/blob/master/dokumentaatio/coverage-report.JPG)

## Järjestelmätestaus

Sovellusta on testattu Linux-ympäristössä käyttöohjeen kuvaamalla tavalla. Määrittelydokumentissa mainitut toiminnallisuudet toimivat, ja käyttöliittymä toimii virheellisilläkin syötteillä.