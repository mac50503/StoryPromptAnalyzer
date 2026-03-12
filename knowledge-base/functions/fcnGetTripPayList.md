# fcnGetTripPayList

## Metadata
- **Tipo**: SRL Function
- **Retorna**: List<TripPay>
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetTripPayList`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theBlazePayRequest | BlazePayRequest | |

## Lógica de negocio

```blaze
theTripPayList is some List<TripPay> initially null.if (theBlazePayRequest.crewPayRequest is equal to null) then{theTripPayList = an ArrayList.theTripPayList.add(theBlazePayRequest.tripPayResponse.tripPay).}return theTripPayList.
```

