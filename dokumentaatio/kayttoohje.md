# Käyttöohje
## Ohjelman käynnistäminen

Asenna ensin poetry komennolla: poetry install

Sovelluksen voi nyt käynnistää komennolla poetry run invoke start

### Main menu
Sovellus käynnistyy main menuun:
![Main menu](https://github.com/ogvirtan/ot-harjoitustyo/tree/master/dokumentaatio/ko_liitteet/main_menu.JPG)
Main menusta voit lopettaa sovelluksen suorituksen komennolla Q, päästä Play-näkymään komennolla P, asetuksiin komennolla O, ja tilastonäkymään komennolla S. Kustakin alinäkymästä pääsee takaisin main menuun komennolla Q. HUOM! komentojen kirjainkoolla ei ole merkitystä.

### Play-näkymä
Päästäksesi sovelluksen Play-näkymään, kirjoita main menussa ohjeiden mukaisesti komennoksi P. Play-näkymä tarjoaa pelitilanteita loputtomasti, kunnes päätät lopettaa pelaamisen, ja poistua Play-näkymästä kirjoittamalla komennon Q päästäksesi takaisin main menuun. HUOM! komentojen kirjainkoolla ei ole merkitystä. Play-näkymässä näkyy kaikki mahdolliset komennot ennen ensimmäistä komentoa, ja komennot tulostuvat näytölle käyttäjän syöttäneen virheellisen komennon jälkeen. Virheellistä komentoa ei lasketa tilastoihin, eikä pelitilanne muutu ennen kuin jokin sallittu komento on syötetty.
![Esimerkki Play-näkymästä](https://github.com/ogvirtan/ot-harjoitustyo/tree/master/dokumentaatio/ko_liitteet/play_screen_example.JPG)

### Asetukset

Päästäksesi asetuksiin, kirjoita main menussa ohjeiden mukaisesti komennoksi O. Asetuksista voit vaihtaa komennolla 1 luovutuksen pois päältä ja takaisin päälle ja komennolla 2 tuplaamisen käden splittaamisen jälkeen pois päältä ja takaisin päälle. Komennolla Q pääset takaisin main menuun. HUOM! komentojen kirjainkoolla ei ole merkitystä. Asetusten vaikutus peliin on näkyvillä [strategia flowchartissa](https://github.com/ogvirtan/ot-harjoitustyo/blob/master/dokumentaatio/Strategy_flowchart.jpg).
![Asetukset](https://github.com/ogvirtan/ot-harjoitustyo/tree/master/dokumentaatio/ko_liitteet/options_screen.JPG)

### Tilastonäkymä

Päästäksesi Tilastonäkymään, kirjoita main menussa ohjeiden mukaisesti komennoksi S. Tilastonäkymä antaa palautetta Play-näkymässä pelattujen käsien menestyksestä. Halutessasi voit nollata tilaston komennolla R. Takaisin main menuun pääsee komennolla Q. HUOM! komentojen kirjainkoolla ei ole merkitystä.
![Statistics](https://github.com/ogvirtan/ot-harjoitustyo/tree/master/dokumentaatio/ko_liitteet/statistics_screen_example.JPG)