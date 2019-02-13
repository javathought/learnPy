import unittest

from mdf.pieces import solve_coins
from mdf.pseudoxml import maxbalise
from mdf.word_distance import distance

from mdf.interets import interets


class TestMdfMethods(unittest.TestCase):

    def test_running(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_coins(self):

        lines = ["6", "3", "2 1", "2 3", "1 4"]
        self.assertEqual(solve_coins(lines), 2)

        lines = ["14", "3", "2 1", "2 4", "2 6"]
        self.assertEqual(solve_coins(lines), 3)

        lines = ["90", "3", "1 1", "2 6", "8 10"]
        self.assertEqual(solve_coins(lines), "IMPOSSIBLE")

        lines = ["85", "3", "2 4", "2 7", "1 70"]
        self.assertEqual(solve_coins(lines), 4)

        lines = ["1", "7", "11 4", "2 10", "28 14", "4 15", "1 21", "2 22", "2 25"]
        self.assertEqual(solve_coins(lines), "IMPOSSIBLE")

        lines = ["133", "4", "18 2", "26 5", "5 12", "1 24"]
        self.assertEqual(solve_coins(lines), 17)

    def test_pseudoxml(self):
        self.assertEqual(maxbalise("wl-l-wpy-y-p"), 'p')
        self.assertEqual(maxbalise("zx-x-zxyz-z-y-x"), 'x')
        self.assertEqual(maxbalise("bc-c-ba-a"), 'a')
        self.assertEqual(maxbalise("nu-u-nim-mo-o-irjlncx-xzd-d-z-cg-gma-a-m-n-l-j-rff-f-fo-onkbwn-nf-f-wra-a-rlbaf-fte"
                                   "sov-v-o-sld-d-l-e-t-a-b-lch-ha-aw-w-c-bxt-t-x-k-net-t-eoif-f-i-ofe-eka-a-kc-c-fyvv-"
                                   "v-v-yx-xsjuuaf-fd-d-a-u-u-j-suewunq-q-n-u-w-er-rmd-dum-mhq-quo-o-utip-p-ivgcm-m-cg-"
                                   "g-gt-t-v-t-h-u-m-u"), 'f')
        self.assertEqual(maxbalise("bisx-xliq-q-i-lagui-ig-gih-h-i-uwz-z-wmevkkehg-g-hi-iop-p-o-e-k-k-v-emfrcdejn-nqnq-"
                                   "q-n-q-jkg-g-kz-z-e-d-c-rye-e-y-f-mujciqzj-j-zo-o-q-ii-i-c-j-u-m-g-ao-o-ssgasbc-c-b-"
                                   "sb-bf-f-a-g-sv-v-iuxdbjs-s-jc-c-b-d-xxiwtr-r-tk-k-w-i-x-us-s-babv-vo-o-b-aynjbi-i-b"
                                   "-jv-v-njk-knah-h-a-n-jjxe-eet-tr-r-e-x-j-yt-th-hzwk-k-wc-c-zcscl-l-c-s-cyu-u-ye-ep-"
                                   "pcnivkgzy-y-z-gy-y-k-vh-h-i-nyeopf-f-p-ov-v-e-ykaarzp-paqgvsgbs-s-bp-p-gj-jhcvv-v-v"
                                   "-ce-e-h-s-v-g-qw-w-a-zyhm-meos-sa-a-opzo-o-zj-j-pbfvn-nv-v-ve-e-f-bk-k-e-hoby-y-bsz"
                                   "v-v-z-s-o-y-rsw-wv-v-s-afi-iyid-d-i-y-f-a-k-cj-jf-fkn-n-k"), 'c')

    def test_distance(self):
        self.assertEqual(distance("arbre","arbore"), 2)
        self.assertEqual(distance("globe","lobe"), 2)
        self.assertEqual(distance("barbe","barre"), 3)
        self.assertEqual(distance("orbe","robe"), 3)
        self.assertEqual(distance("algorithme","logarithme"), 7)
        self.assertEqual(distance("algorithme","rythme"), 11)

    def test_fibre(self):
        self.assertEqual( "4; 0 0; 0 1; 1 0; 1 1", 3)

    def test_interets(self):
        lines = ["4", "0", "-10", "-10","-10","-10"]
        self.assertEqual( interets(lines), 17)


if __name__ == '__main__':
    unittest.main()
