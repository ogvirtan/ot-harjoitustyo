import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)
        self.melkotyhjakortti = Maksukortti(10)
        self.kassapaate = Kassapaate()
    
    def test_luotu_paate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
    
    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_konstruktori_asettaa_maukkaat_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_konstruktori_asettaa_edulliset_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.kortti, None)

    def test_konstruktori_asettaa_kortin_saldon_oikein(self):
        self.assertEqual(self.kortti.saldo, 1000)
    
    def test_luotu_melkotyhjakortti_on_olemassa(self):
        self.assertNotEqual(self.melkotyhjakortti, None)

    def test_konstruktori_asettaa_melkotyhjankortin_saldon_oikein(self):
        self.assertEqual(self.melkotyhjakortti.saldo, 10)

#Riittävästi käteistä
    def test_kassa_muuttuu_oikein_edullinen_kateisella_riittava_valuutta(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
    
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kassa_muuttuu_oikein_maukas_kateisella_riittava_valuutta(self):
        self.kassapaate.syo_maukkaasti_kateisella(410)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_vaihtorahat_oikein_edullinen_kateisella_riittava_valuutta(self):
        back = self.kassapaate.syo_edullisesti_kateisella(250)
    
        self.assertEqual(back, 10)

    def test_vaihtorahat_oikein_maukas_kateisella_riittava_valuutta(self):
        back = self.kassapaate.syo_maukkaasti_kateisella(410)

        self.assertEqual(back, 10)
    
    def test_lounaiden_maara_muuttuu_oikein_kateisella_riittava_valuutta(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.kassapaate.syo_maukkaasti_kateisella(410)

        self.assertTrue(self.kassapaate.maukkaat + self.kassapaate.edulliset, 2)

#Liian vähän käteistä
    def test_kassa_muuttuu_oikein_edullinen_kateisella_vaara_valuutta(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
    
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassa_muuttuu_oikein_maukas_kateisella_vaara_valuutta(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_vaihtorahat_oikein_edullinen_kateisella_vaara_valuutta(self):
        back = self.kassapaate.syo_edullisesti_kateisella(230)
    
        self.assertEqual(back, 230)

    def test_vaihtorahat_oikein_maukas_kateisella_vaara_valuutta(self):
        back = self.kassapaate.syo_maukkaasti_kateisella(390)

        self.assertEqual(back, 390)
    
    def test_lounaiden_maara_muuttuu_oikein_edullinen_kateisella_vaara_valuutta(self):
        self.kassapaate.syo_edullisesti_kateisella(190)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_lounaiden_maara_muuttuu_oikein_maukas_kateisella_vaara_valuutta(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)

        self.assertEqual(self.kassapaate.maukkaat, 0)

#Korttimaksu
#Tarpeeksi saldoa kortilla   
    def test_kassa_ei_muutu_edullinen_kortilla_riittava_valuutta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_kassa_ei_muutu_maukas_kortilla_riittava_valuutta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maksu_onnistui_oikein_edullinen_kortilla_riittava_valuutta(self):
        back = self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertTrue(back)
    
    def test_maksu_onnistui_oikein_maukas_kortilla_riittava_valuutta(self):
        back = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertTrue(back)

    def test_kortin_saldo_oikein_edullinen_kortilla_riittava_valuutta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo, 760)
    
    def test_kortin_saldo_oikein_maukas_kortilla_riittava_valuutta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo, 600)

    def test_lounaiden_maara_muuttuu_oikein_kortilla_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertTrue(self.kassapaate.edulliset, 1)
    
    def test_lounaiden_maara_muuttuu_oikein_kortilla_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertTrue(self.kassapaate.maukkaat, 1)

#Ei tarpeeksi saldoa kortilla
    def test_kassa_ei_muutu_edullinen_kortilla_vaara_valuutta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.melkotyhjakortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_kassa_ei_muutu_maukas_kortilla_vaara_valuutta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.melkotyhjakortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_palauttaa_false_maukkaasti_kortilla_vaara_valuutta(self):
        back = self.kassapaate.syo_maukkaasti_kortilla(self.melkotyhjakortti)

        self.assertFalse(back)

    def test_palauttaa_false_edullinen_kortilla_vaara_valuutta(self):
        back = self.kassapaate.syo_edullisesti_kortilla(self.melkotyhjakortti)

        self.assertFalse(back)

    def test_kortin_saldo_ei_muutu_maukas_kortilla_vaara_valuutta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.melkotyhjakortti)

        self.assertEqual(self.melkotyhjakortti.saldo, 10)
    
    def test_kortin_saldo_ei_muutu_edullinen_kortilla_vaara_valuutta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.melkotyhjakortti)

        self.assertEqual(self.melkotyhjakortti.saldo, 10)

    def test_lounaiden_maara_ei_muutu_maukas_kortilla_vaara_valuutta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.melkotyhjakortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    
    def test_lounaiden_maara_ei_muutu_edullinen_kortilla_vaara_valuutta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.melkotyhjakortti)

        self.assertEqual(self.kassapaate.edulliset, 0)
#Lataus
    def test_kortille_lataus_muuttaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)

        self.assertEqual(self.kortti.saldo, 2000)

    def test_kortille_lataus_muuttaa_kassan_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kortille_negatiivisen_saldon_lataaminen_ei_muuta_kassapaatteen_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_negatiivisen_saldon_lataaminen_ei_muuta_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -100)

        self.assertEqual(self.kortti.saldo, 1000)

    def test_kortille_negatiivisen_saldon_lataaminen_palauttaa_false(self):
        back = self.kassapaate.lataa_rahaa_kortille(self.kortti, -100)

        self.assertFalse(back)