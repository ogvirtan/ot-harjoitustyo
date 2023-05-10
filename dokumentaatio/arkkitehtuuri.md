# Arkkitehtuuri
![Tässä on sovelluksen pakkauskaavio.](https://github.com/ogvirtan/ot-harjoitustyo/blob/master/dokumentaatio/package_diagram.PNG)

Sovellus koostuu entities pakkauksesta löytyvistä strategiatyökaluun tarvittavista osista. Services pakkauksen Tool.py luokka yhdistää entities kansion sisällön toimivaksi sovelluslogiikaksi. Pakkaus UI on käyttöliittymä, joka mahdollistaa sovelluslogiikan Services käytön.


## Käyttöliittymä

Käyttöliittymä koostuu neljästä ruudusta: Menu-, Options-, Statistics- ja Play-näkymästä. Menu näkymästä voi oikean komennon kirjoittamalla päästä muihin näkymiin tai sulkea sovelluksen. Options-valikossa voi vaikuttaa siihen, millä säännöillä peliä pelataan pelinäkymässä. Statistics näkymä kertoo miten olet menestynyt pelinäkymässä, ja antaa vaihtoehdon nollata tilastot. Pelinäkymässä näet komennot, kätesi ja jakajan päällimmäisen kortin. Tämän informaation pohjalta valitset strategian; saat välittömän palautteen strategian oikeellisuudesta, ja uusi pelitilanne ilmestyy ruudulle. Käyttäjän syöttäessä väärän syötteen komennot tulostuvat uudelleen ja sovellus kertoo edellisen komennon olleen virheellinen.

## Sovelluslogiikka

Luokka Tool, joka vastaa sovelluslogiikasta luo, seuraa, päivittää ja arvioi pelitilannetta. Pelitilanteeseen tarvittavat oliot ovat: Card(kortti), Deck(pakka); joka koostuu korteista, ja Player(pelaaja/talo) joiden välistä pelitilannetta seurataan. Sovelluslogiikka tarjoaa loputtomasti satunnaisia pelitilanteita, joihin käyttäjä reagoi käyttöliittymän välityksellä. Luokan Tool metodiin strategy() on koodattu kaikki mahdolliset pelitilanteet ja niille optimaaliset strategiat. Pelaajan menestymistä seurataan sanakirja-olion tracking_dict avulla, joka kirjaa oikein ja väärin menneet pelivalinnat.