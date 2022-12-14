pip install pycryptodome
pip install requests
pip install lxml


# SDK Pagos Online

SDK Pagos Online es un modulo python para facilitar la integracion al generador de ligas.

## Instalación

Para compilar y dar mantenimiento al proyecto

```bash
pip install pycryptodome requests lxml
```

## Estructura del proyecto.

**WppClient** es la clase encargada de armar y procesar la petición para la generacion de ligas.

El folder **validators** incluye reglas de validación básicas requeridas para determinar si el objeto puede ser enviado al generador de ligas. 
La documentación de los datos requeridos se pueden encontrar en el sandbox de [Pagos Online](https://sandboxpol.mit.com.mx/generar).

El folder **builders** incluye clases que permiten que los usuarios puedan crear la solicitud de generación de ligas de una forma más intuitiva.

Finalmente, **tests** incluye pruebas unitarias del proyecto, puede ejecutarse con `npm run test`


## Publicación

*TBD*

## Uso
El modulo esta implementado para trabajar con *Python 3.9* o superior.

Es importante observar que este modulo debe implementarse dentro de un ambiente seguro en donde la llave de cifrado no quede expuesta a terceros.

Se debe utilizar una  instancia de la clase *PaymentBuilder* para capturar los datos proporcionados por **MIT**. Posteriormente, se crea una instancia de *WppClient* proporcionando el *endpoint*, *identificador de pagos* y *llave de cifrado* en **hexadecimal**


```python
import mitWppSdk.builders as builders
from mitWppSdk.WppClient import WppClient
from datetime import date
from decimal import Decimal

  def urlIsCreated(self):
    bb = builders.PaymentBuilder().withBusiness().idBranch("BRNH").idCompany(
        "CMPY").pwd("pwd").user("user1234").andParent().withUrl().reference("PYREF0001").amount(
          Decimal(10.50)).clientEmail("mail@mail.com").expirationDate(date(2022, 9, 13)).moneda(
            builders.MonedaType.MXN).promotions("C", "3").andParent().build()

    client = WppClient( "https://sandboxpo.mit.com.mx/gen", "SNDBX123", "5DCC67393750523CD165F17E1EFADD21")
    url = client.getUrlPayment(bb)
    print(url)

urlIsCreated()
```


## Webhook o Http Callback
El **comercio** debe exponer un *http callback* o *URI endpoint* que le permita conocer si el pago del cliente fue **aprobado** o **declinado** y aplicar la lógica correspondiente a su negocio.

Para descifrar el mensaje, se puede utilizar el método `processAfterPaymentResponse` de la clase `WppClient`

```python
    def afterPayment():
        response = "otB4VyAtYh5bW4IeVhM30125kqfmzVxxDlFQRZHCUroq6e1MSISChhDstN1gKKnA%0D%0AOs%2Bdgr...";
        payResponse = client.processAfterPaymentResponse(response);
        print(payResponse["reference"])

afterPayment();
```

## License
[MIT](https://choosealicense.com/licenses/mit/)