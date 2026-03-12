# fcnCreatePlnTripPayResponse

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PlnTripPayResponse
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\PlanningPay\Functions\fcnCreatePlnTripPayResponse`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPlnTripPayRequest | PlnTripPayRequest | |

## Lógica de negocio

```blaze
retVal is some PlnTripPayResponse initially null.if (aPlnTripPayRequest <> null) then{aPlnTripPayResponse is a PlnTripPayResponse.retVal = aPlnTripPayResponse.aPlnTripPay is some PlnTripPay initially fcnCreatePlnTripPay(aPlnTripPayRequest.plnPayTrip).aPlnTripPayResponse.plnTripPay = aPlnTripPay.}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnCreatePlnTripPay](fcnCreatePlnTripPay.md)

