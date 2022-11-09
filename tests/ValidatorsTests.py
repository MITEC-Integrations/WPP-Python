import os, sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), "src"))

import unittest
from mitWppSdk.validators import *
import mitWppSdk.builders as builders
from datetime import date
from decimal import Decimal
from lxml import etree

class Container:
    ...


class TestValidatorsFunctions(unittest.TestCase):
    # @unittest.skip("disabled")
    def test_stringValidatorSuccess(self):
        validator = StringValidator().minLength(2).maxLength(6)
        value = "value"
        result = validator.go(value)
        self.assertTrue(result.ok)

    # @unittest.skip("disabled")
    def test_stringValidatorFailed(self):
        validator = StringValidator().minLength(2).maxLength(6)
        value = "v"
        result = validator.go(value)
        print("error", result.message)
        self.assertFalse(result.ok)

    # @unittest.skip("disabled")
    def test_numberValidatorSuccess(self):
        validator = NumberValidator().minLength(2).maxLength(6)
        value = 256
        result = validator.go(value)
        self.assertTrue(result.ok)

    # @unittest.skip("disabled")
    def test_numberValidatorFailed(self):
        validator = NumberValidator().minLength(2).maxLength(6)
        value = 2
        result = validator.go(value)
        print("error", result.message)
        self.assertFalse(result.ok)

    # @unittest.skip("disabled")
    def test_numberValidatorNoneError(self):
        validator = NumberValidator().minLength(2).maxLength(6)
        result = validator.go(None)
        print("error", result.message)
        self.assertFalse(result.ok)

    # @unittest.skip("disabled")
    def test_numberValidatorNoneSuccess(self):
        validator = NumberValidator().optional(True).minLength(2).maxLength(6)
        result = validator.go(None)
        self.assertTrue(result.ok)

    # @unittest.skip("disabled")
    def test_shapeValidator(self):
        shape = ShapeValidator[Container]()
        shape.name = StringValidator().minLength(3).maxLength(5)
        shape.amount = FloatValidator().notEmpty()

        c = Container()
        c.name = "Juan"
        c.amount = 4.5

        result = shape.go(c)
        self.assertTrue(result.ok)

    # @unittest.skip("disabled")
    def test_shapeValidatorFailed(self):
        shape = ShapeValidator[Container]()
        shape.name = StringValidator().minLength(3).maxLength(5)
        shape.amount = FloatValidator().notEmpty()

        c = Container()
        c.name = "Nombre Largo"
        c.amount = 4.5

        result = shape.go(c)
        print("error", result.message)
        self.assertFalse(result.ok)

    def test_paymentValidatorSucceds(self):
        bb = builders.PaymentBuilder().withBusiness().idBranch("BRNH").idCompany(
            "CMPY").pwd("pwd").user("user1234").andParent().withUrl().reference("PY_REF0001").amount(
            Decimal(10.50)).clientEmail("mail@mail.com").expirationDate(date(2022, 9, 13)).moneda(
                builders.MonedaType.MXN).promotions("C", "3").andParent().withAditionalData(
                ).append(1, True, "label1", "value1").append(2, False, "label2", "value2").andParent().build()

        validator = PaymentValidator()
        result = validator.validate(bb)
        self.assertTrue(result.ok)

    def test_paymentValidatorFails(self):
        bb = builders.PaymentBuilder().withBusiness().idBranch("BRNH").idCompany(
            "CMPY").pwd("pwd").user("user1234").andParent().withUrl().reference("PY_REF0001").amount(
            Decimal(10.50)).clientEmail("mail@mail.com").expirationDate(date(2022, 9, 13)).moneda(
                builders.MonedaType.MXN).promotions("C", "3").andParent().withAditionalData(
                ).append(1, True, None, "value1").append(2, False, "label2", "value2").andParent().build()

        validator = PaymentValidator()
        result = validator.validate(bb)
        self.assertFalse(result.ok)
        self.assertTrue("datos_adicionales." in result.message)


if __name__ == '__main__':
    unittest.main()
