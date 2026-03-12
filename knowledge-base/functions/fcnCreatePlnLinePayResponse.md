# fcnCreatePlnLinePayResponse

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PlnLinePayResponse
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\PlanningPay\Functions\fcnCreatePlnLinePayResponse`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPlnLinePayRequest | PlnLinePayRequest | |

## Lógica de negocio

```blaze
retVal is some PlnLinePayResponse initially null.if (aPlnLinePayRequest <> null) then{aPlnLinePayResponse is a PlnLinePayResponse.retVal = aPlnLinePayResponse.aPlnPayTrip is some PlnPayTrip initially null.aPlnTripPay is some PlnTripPay initially null.if (aPlnLinePayRequest.plnPayTripList is not equal to null and aPlnLinePayRequest.plnPayTripList.size() > 0) then     {        for each PlnPayTrip in aPlnLinePayRequest.plnPayTripList as an array of PlnPayTrip do         {               aPlnPayTrip = it.aPlnTripPay = fcnCreatePlnTripPay(aPlnPayTrip).retVal.plnTripPayList.add(aPlnTripPay).}}}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnCreatePlnTripPay](fcnCreatePlnTripPay.md)

