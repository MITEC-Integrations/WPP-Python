import os, sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), "src"))

import unittest
from mitWppSdk.util import WppHttpHelper


class TestHttpFunctions(unittest.TestCase):
    def test_sendRequest(self):
        helper = WppHttpHelper("https://sandboxpo.mit.com.mx/gen")
        # helper = WppHttpHelper("https://u.mitec.com.mx/gen")
        msg = """<pgs>
    <data0>SNDBX123</data0>
    <data>glLJ1G2RTbWmAOJfI72MgnOLCMW1GN8wFazLjJjShglG35xFs79MYCFdwwKmL5Xr0TIs8YmETI2KjT7ifETvADtVCdLL19X526L6ZLqZTGP6yYR1m4aN6TxV8Ash7QMmb1hscWhFCUSX94qcRncSFrnxmw+FDvk3NgRmeNTLr1j3MM3JSlSAxAoum7E3k9+KQ6TA2rp/YGN8BoAlRpPXrHcSPGM00xR90xbDZrb6Xkm5O8m/pf3h2MxdXAQEI6USwTb133mHV1YllDCW1hQKvm93aCcTMopUdjDI6llg3irQhqHYokqdbDa6Sm1sNxxxSEQC9vAjnsyWPUlhCHNYZTYL1UNUfmvI2blKEOC8yzsvC7siyTH5LiAE5Z3mQjE4yXtQfsD0hg9tARzaBWcVCxoY6X/Uw0KDVTGyAxSi7aq48MO800d9lkydFsoHY1sdi5C8mPl78VVJXNjfgDe8+VbyUaD7UHguGwsIUTRYFBoUe8xSshF2iPObAbHN0FmWvPrE4E2CEjEx2OjkeJp2Awyo82tXpVGQJ+SAONPFtLI=</data>
  </pgs>"""
        msg = "xml" + msg
        resp = helper.post(msg)
        print(resp, end="\n")


if __name__ == '__main__':
    unittest.main()