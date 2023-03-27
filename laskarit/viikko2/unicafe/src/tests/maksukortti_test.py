import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        # alustetaan maksukortti, jossa on 10 euroa (1000 senttiä)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")
     
    def test_saldo_ei_mene_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(1001)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(900)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 1.00 euroa")

    def test_ota_rahaa_palauttaa_false(self):
            self.assertFalse(self.maksukortti.ota_rahaa(1001), "Kortti ei anna liian suuren maksun mennä läpi")

    def test_ota_rahaa_palauttaa_true(self):
            self.assertTrue(self.maksukortti.ota_rahaa(900), "Kortti antaa sopivan suuruisen maksun mennä läpi")