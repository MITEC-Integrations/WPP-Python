import os, sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), "src"))

import mitWppSdk.builders as builders
from datetime import date
from decimal import Decimal
from lxml import etree
import unittest

class TestBuilderFunctions(unittest.TestCase):

    @unittest.skip("disabled")
    def test_buildBusinessObject(self):
        bb = builders.BusinessBuilder().idBranch("BRNH").idCompany(
            "CMPY").pwd("pwd").user("user").build()
        print(etree.tostring(bb, pretty_print=True).decode("utf-8"))


    @unittest.skip("disabled")
    def test_buildsUrlObject(self):
        bb = builders.UrlBuilder().reference("PY_REF0001").amount(Decimal(10.50)).clientEmail(
            "mail@mail.com").expirationDate(date(2022, 9, 13)).moneda(builders.MonedaType.MXN).promotions("C", "3").build()
        print(etree.tostring(bb, pretty_print=True).decode("utf-8"))


    @unittest.skip("disabled")
    def test_buildsData3ds(self):
        bb = builders.B3dsBuilder().email("th@mail.com").phone("1133557799").address(
            "4001 Sul street").city("city").state("PU").zipCode("14794").isoCountry("MEX").build()
        print(etree.tostring(bb, pretty_print=True).decode("utf-8"))

    @unittest.skip("disabled")
    def test_buildsAdditionalData(self):
        bb = builders.AditionalDataArrayBuilder().append(
            1, True, "label", "value").append(2, False, "label2", "value2").build()
        print(etree.tostring(bb, pretty_print=True).decode("utf-8"))


    def test_buildsRoot(self):
        bb = builders.PaymentBuilder().paymentMethod(builders.PaymentMethodType.APY).withBusiness().idBranch("BRNH").idCompany(
            "CMPY").pwd("pwd").user("user").andParent().withUrl().reference("PY_REF0001").amount(
            Decimal(10.50)).clientEmail("mail@mail.com").expirationDate(date(2022, 9, 13)).moneda(
                builders.MonedaType.MXN).promotions("C", "3").andParent().withAditionalData(
                ).append(1, True, "label1", "value1").append(2, False, "label2", "value2").andParent().build()
        print(etree.tostring(bb, pretty_print=True).decode("utf-8"))

if __name__ == '__main__':
    unittest.main()