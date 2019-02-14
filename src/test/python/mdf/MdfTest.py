import unittest

from mdf.Pole_vault import pole_vault
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

    # def test_distance(self):
    #     self.assertEqual(distance("arbre","arbore"), 2)
    #     self.assertEqual(distance("globe","lobe"), 2)
    #     self.assertEqual(distance("barbe","barre"), 3)
    #     self.assertEqual(distance("orbe","robe"), 3)
    #     self.assertEqual(distance("algorithme","logarithme"), 7)
    #     self.assertEqual(distance("algorithme","rythme"), 11)

    def test_interets(self):
        lines = ["4", "0", "-10", "-10","-10","-10"]
        self.assertEqual(17, interets(lines))

    def test_pole_vault(self):
        lines = ["9", "aaaaaa 4.25 S", "bbbbbb 4.25 E", "bbbbbb 4.25 S", "bbbbbb 4.30 E", "aaaaaa 4.30 E", "aaaaaa 4.30 E", "aaaaaa 4.30 E"]
        self.assertEqual("aaaaaa", pole_vault(lines))
        lines = ["7", "aaaaaa 4.25 S", "bbbbbb 4.25 E", "aaaaaa 4.27 E", "bbbbbb 4.30 S", "aaaaaa 4.30 S", "bbbbbb 4.35 E", "aaaaaa 4.38 E"]
        self.assertEqual("KO", pole_vault(lines))

        # Concours numéro : 1
        # Votre code a renvoyé :
        lines = ["7", "gviywn 4.08 S",
        "vntbip 4.1 S ",
        "mhbdpx 4.12 S",
        "ovjerf 4.17 S",
        "xzjabm 4.17 S",
        "vntbip 4.27 S",
        "xzjabm 4.27 S",
        "mhbdpx 4.28 S",
        "ovjerf 4.3 S ",
        "gviywn 4.34 S",
        "mhbdpx 4.36 S",
        "ovjerf 4.42 S",
        "mhbdpx 4.43 S",
        "xzjabm 4.47 S",
        "luxzim 4.54 S",
        "ovjerf 4.56 S",
        "vntbip 4.57 S",
        "mhbdpx 4.58 S",
        "luxzim 4.62 S",
        "xzjabm 4.65 S",
        "gviywn 4.66 S",
        "ovjerf 4.71 S",
        "mhbdpx 4.71 S",
        "vntbip 4.73 S",
        "jvldsq 4.75 S",
        "euaosi 4.76 S",
        "mhbdpx 4.76 S",
        "luxzim 4.77 S",
        "xzjabm 4.78 S",
        "gviywn 4.81 S",
        "vntbip 4.86 S",
        "mhbdpx 4.88 S",
        "jvldsq 4.9 S ",
        "ovjerf 4.9 S ",
        "xzjabm 4.92 S",
        "gviywn 4.92 S",
        "euaosi 4.96 S",
        "ovjerf 4.96 S",
        "eqbfnj 4.97 S",
        "xzjabm 5.0 S ",
        "xzjabm 5.05 S",
        "vntbip 5.05 S",
        "euaosi 5.07 S",
        "gviywn 5.07 S",
        "jvldsq 5.1 S ",
        "eqbfnj 5.11 S",
        "vntbip 5.11 S",
        "gviywn 5.14 S",
        "luxzim 5.15 S",
        "euaosi 5.17 S",
        "gviywn 5.19 S",
        "mhbdpx 5.2 S ",
        "xzjabm 5.22 S",
        "euaosi 5.22 S",
        "luxzim 5.23 S",
        "ovjerf 5.26 S",
        "jvldsq 5.28 S",
        "xzjabm 5.32 S",
        "mhbdpx 5.35 S",
        "eqbfnj 5.36 S",
        "euaosi 5.39 S",
        "vntbip 5.41 S",
        "jvldsq 5.41 S",
        "mhbdpx 5.42 S",
        "ovjerf 5.46 S",
        "gviywn 5.46 S",
        "eqbfnj 5.47 S",
        "mhbdpx 5.53 S",
        "luxzim 5.54 S",
        "jvldsq 5.58 S",
        "mhbdpx 5.58 S",
        "gviywn 5.6 S ",
        "xzjabm 5.65 S",
        "luxzim 5.66 S",
        "mhbdpx 5.66 S",
        "xzjabm 5.71 S",
        "jvldsq 5.72 S",
        "eqbfnj 5.73 S",
        "euaosi 5.74 S",
        "gviywn 5.76 S",
        "mhbdpx 5.79 S",
        "eqbfnj 5.8 S ",
        "ovjerf 5.81 S",
        "xzjabm 5.85 S",
        "jvldsq 5.9 S ",
        "eqbfnj 5.91 S",
        "xzjabm 5.95 S",
        "jvldsq 5.96 S",
        "euaosi 5.98 S",
        "luxzim 6.0 S ",
        "xzjabm 6.01 S",
        "euaosi 6.04 S",
        "mhbdpx 6.04 S",
        "gviywn 6.05 S",
        "vntbip 6.06 S",
        "jvldsq 6.06 S",
        "ovjerf 6.07 S",
        "xzjabm 6.08 S",
        "eqbfnj 6.11 S",
        "jvldsq 6.13 S",
        "vntbip 6.17 S",
        "mhbdpx 6.2 S ",
        "gviywn 6.22 S",
        "ovjerf 6.23 S",
        "eqbfnj 6.29 S",
        "euaosi 6.29 S",
        "gviywn 6.3 S ",
        "xzjabm 6.32 S",
        "vntbip 6.32 S",
        "jvldsq 6.39 S",
        "ovjerf 6.4 S ",
        "xzjabm 6.42 E",
        "xzjabm 6.42 S",
        "eqbfnj 6.42 E",
        "eqbfnj 6.42 S",
        "euaosi 6.42 E",
        "euaosi 6.42 S",
        "mhbdpx 6.42 E",
        "mhbdpx 6.42 S",
        "gviywn 6.45 S",
        "jvldsq 6.55 E",
        "jvldsq 6.55 S",
        "gviywn 6.55 S",
        "euaosi 6.56 S",
        "mhbdpx 6.56 S",
        "vntbip 6.6 E ",
        "vntbip 6.6 S ",
        "eqbfnj 6.61 S",
        "jvldsq 6.62 E",
        "mhbdpx 6.67 E",
        "gviywn 6.69 E",
        "gviywn 6.69 S",
        "eqbfnj 6.71 E",
        "eqbfnj 6.71 S",
        "euaosi 6.74 S",
        "jvldsq 6.76 E",
        "jvldsq 6.76 S",
        "eqbfnj 6.77 S",
        "ovjerf 6.77 E",
        "ovjerf 6.77 S",
        "xzjabm 6.82 S",
        "luxzim 6.89 E"]

        self.assertEqual("xzjabm", pole_vault(lines))

        lines = [1,
            "pdhzos 4.09 S",
            "pthxdo 4.12 S",
            "xzvgpj 4.15 S",
            "pdhzos 4.21 S",
            "xzvgpj 4.27 S",
            "pthxdo 4.3 S ",
            "xzvgpj 4.35 S",
            "pthxdo 4.36 S",
            "woyxbf 4.44 S",
            "xzvgpj 4.52 S",
            "woyxbf 4.54 S",
            "xzvgpj 4.62 S",
            "woyxbf 4.67 S",
            "pthxdo 4.79 S",
            "pdhzos 4.8 S ",
            "bxjitn 4.82 S",
            "xzvgpj 4.87 S",
            "pdhzos 4.87 S",
            "woyxbf 4.92 S",
            "bxjitn 4.92 S",
            "pthxdo 4.95 S",
            "xzvgpj 4.96 S",
            "pdhzos 4.98 S",
            "plgxzc 4.99 S",
            "kwexzq 5.02 S",
            "woyxbf 5.03 S",
            "pthxdo 5.04 S",
            "xzvgpj 5.05 S",
            "bxjitn 5.07 S",
            "pthxdo 5.12 S",
            "woyxbf 5.14 S",
            "plgxzc 5.18 S",
            "woyxbf 5.24 S",
            "bxjitn 5.24 S",
            "pthxdo 5.29 S",
            "fsihar 5.29 S",
            "plgxzc 5.3 S ",
            "pthxdo 5.34 S",
            "woyxbf 5.34 S",
            "fsihar 5.35 S",
            "bxjitn 5.35 S",
            "pdhzos 5.38 S",
            "pthxdo 5.39 S",
            "kwexzq 5.39 S",
            "plgxzc 5.4 S ",
            "woyxbf 5.45 S",
            "xzvgpj 5.46 S",
            "pthxdo 5.48 S",
            "plgxzc 5.49 S",
            "bxjitn 5.5 S ",
            "pdhzos 5.51 S",
            "woyxbf 5.54 S",
            "kwexzq 5.57 S",
            "pthxdo 5.63 S",
            "bxjitn 5.65 S",
            "fsihar 5.73 S",
            "pdhzos 5.74 S",
            "plgxzc 5.75 S",
            "kwexzq 5.77 S",
            "xzvgpj 5.81 S",
            "fsihar 5.83 S",
            "pthxdo 5.83 S",
            "pthxdo 5.89 S",
            "pdhzos 5.89 S",
            "kwexzq 5.9 S ",
            "xzvgpj 5.9 S ",
            "woyxbf 5.91 S",
            "kwexzq 5.97 S",
            "fsihar 5.99 S",
            "plgxzc 6.04 S",
            "xzvgpj 6.05 S",
            "pthxdo 6.08 S",
            "bxjitn 6.09 S",
            "kwexzq 6.1 S ",
            "fsihar 6.16 S",
            "kwexzq 6.19 S",
            "woyxbf 6.2 S ",
            "plgxzc 6.22 S",
            "fsihar 6.23 S",
            "xzvgpj 6.23 S",
            "pthxdo 6.25 S",
            "pdhzos 6.29 S",
            "woyxbf 6.35 E",
            "woyxbf 6.35 S",
            "xzvgpj 6.36 S",
            "pdhzos 6.36 S",
            "bxjitn 6.38 E",
            "bxjitn 6.38 E",
            "bxjitn 6.38 S",
            "kwexzq 6.39 E",
            "pthxdo 6.43 S",
            "plgxzc 6.45 S",
            "woyxbf 6.49 S",
            "plgxzc 6.51 E",
            "plgxzc 6.51 S",
            "bxjitn 6.55 S",
            "bxjitn 6.67 S",
            "pthxdo 6.69 S",
            "plgxzc 6.74 S",
            "bxjitn 6.75 E",
            "kwexzq 6.82 S",
            "pthxdo 6.82 S",
            "xzvgpj 6.82 E",
            "xzvgpj 6.82 E",
            "xzvgpj 6.82 E",
            "bxjitn 6.83 S",
            "fsihar 6.84 E",
            "fsihar 6.84 E",
            "fsihar 6.84 E",
            "plgxzc 6.86 S",
            "kwexzq 6.88 E",
            "woyxbf 6.88 E",
            "woyxbf 6.88 S",
            "pdhzos 6.9 S ",
            "pthxdo 6.95 S",
            "pdhzos 6.97 S",
            "plgxzc 7.0 S ",
            "bxjitn 7.0 S ",
            "kwexzq 7.04 S",
            "kwexzq 7.1 S ",
            "plgxzc 7.11 S",
            "pthxdo 7.13 E",
            "pthxdo 7.13 E",
            "pthxdo 7.13 S",
            "pdhzos 7.24 E",
            "pdhzos 7.24 S",
            "plgxzc 7.26 S",
            "kwexzq 7.28 S",
            "pthxdo 7.32 E",
            "pthxdo 7.32 S",
            "kwexzq 7.34 E",
            "kwexzq 7.34 E",
            "woyxbf 7.34 E",
            "plgxzc 7.35 E",
            "plgxzc 7.35 S",
            "bxjitn 7.39 E",
            "bxjitn 7.39 S",
            "pdhzos 7.42 S",
            "kwexzq 7.43 E",
            "pdhzos 7.47 E",
            "bxjitn 7.49 S",
            "pthxdo 7.5 E "
        ]

        self.assertEqual("bxjitn", pole_vault(lines))
    # lu
        # Résultat attendu : euaosi


if __name__ == '__main__':
    unittest.main()
