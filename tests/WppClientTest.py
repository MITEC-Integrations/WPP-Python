import os, sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), "src"))

from decimal import Decimal
from datetime import date
from mitWppSdk.WppClient import WppClient
import mitWppSdk.builders as builders
import unittest


class TestHttpFunctions(unittest.TestCase):
    def setUp(self):
        self._client = WppClient(
            "https://sandboxpo.mit.com.mx/gen", "SNDBX123", "5DCC67393750523CD165F17E1EFADD21")

    @unittest.skip("disabled")
    def test_requestWasSent(self):
        bb = builders.PaymentBuilder().withBusiness().idBranch("BRNH").idCompany(
            "CMPY").pwd("pwd").user("user1234").andParent().withUrl().reference("PYREF0001").amount(
            Decimal(10.50)).clientEmail("mail@mail.com").expirationDate(date(2022, 9, 13)).moneda(
                builders.MonedaType.MXN).promotions("C", "3").andParent().build()
        url = self._client.getUrlPayment(bb)
        print(url)

    def test_afterPaymentResponse(self):
        strResponse = "otB4VyAtYh5bW4IeVhM30125kqfmzVxxDlFQRZHCUroq6e1MSISChhDstN1gKKnA%0D%0AOs%2BdgrMxpLDffJQjJ8GJyGeOaOG8LSfUg0vaxVwnTwXEzXFheI%2BbgarDW0fUXS6h%0D%0ARd1jFwMKLduhHrQ2dyE9EijwtdQv6TmI2Gp6tfQaPix0GRHcPZUCAozNyhZWaNIO%0D%0AAqfI%2FRRb8FNHbvYHEEVssRRfeF8f8k%2F8HF5oM4Ec%2BcT848llOgwETNjpGgOAaHi8%0D%0AZwjPk2YBxoqxhFLd8Kht2qnAyOht3SSLXvSG3mx1Cd1NfJGDWfjkFXv0omump%2FF1%0D%0AZEHr7MzgWCPROTfSaWaz1phQO%2BNNmba4lwS2KMMnlp76XQXhHqW3AVvSbtcZyj2i%0D%0APAL5Y3aJI%2BswMXe97IvyUW%2FM6GiBESoSOh4m5TTeEZfmwAT47H81w%2F%2FBRaEmUM92%0D%0A9Pq5kCTdizBOjf9OiZkthM3rTsWJJ9nc93UHCZ%2BTuyTsyDwxoSHJ32cRt2G9M%2Fhq%0D%0AYXNfh8Deh45Fgi8K4gj9KQJ25FUd%2F0mknDMxCva7EbW6oOADKBV3GlBN1RSyJSIt%0D%0A0LIVfVCgFtY1sPdrk8FGhsy7Z3jXb2kpYrUhbMwVGw1Jui4jdNVjsoxWy1Q8MZmP%0D%0AaLoiHGMnijnQXDw9SnyypB9nIhpMhnp2z%2FPlLU%2BJNo9NeO%2BupcQuINIeFDke1cBd%0D%0ASPGUhLMDjBPSBpz8irtRuSHo1QJSILtxKXCe5ifnFFps98dzaAYKL03fwQbWgShg%0D%0AIHfWuuUdE6sHm22lIZeNdN8PvDgJ6MPLuy26wz5dCJUc4s%2BS3XHIQ63jFAnTJ4ig%0D%0AQnvl6DquCWQnMIRejd7JCN%2FEspPLJ52ftT27xJxfg3b0sTeQLcRZflZU56Rj4j%2FP%0D%0AorxVsgze0frAA%2FFc52LJ9LrUiTv9hb27X5JqOtDZ35Qpq3bpPEghZtjOdGptKuB4%0D%0AA0c%2FcCzHwlZbJ7Aakqm2IG2gLOA%2BAqxJYOSSSMz5CjRQuHVXTv8gAK81JrPxM46t%0D%0ABUGVgAKNSbgzADaACDhxPL8GyBwb4ZhMZdCYHUanHGziS9rmhV5ynggidbF3Ssen%0D%0AvK1fvJT9%2F2d5JXQv%2B4TSv3b63nnm173yFS7cqLG3f38Mgz%2B89Vm3FHssKMkme1NH%0D%0AlWT5Q02bpDRmvhI8EIlDr5Fnj8pS6ck4i62fbdBZCaIE2jMUeonGtdqw3Ymy6Sn4%0D%0Ah2eEErVoJmDmesEpHglkFBcwze3XC6cysyx16hdDWJIbIueCbK57jgEC5%2BT4mJ1h%0D%0AsZJC2q7hzFagLcssdicr1w%3D%3D"
        payResponse = self._client.processAfterPaymentResponse(strResponse)
        self.assertIsNotNone(payResponse)
        self.assertEquals(payResponse["reference"], "MIFACTURA001")


if __name__ == '__main__':
    unittest.main()
