# fcnSetTripPositionA

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnSetTripPositionA`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripPay | TripPay | |

## Lógica de negocio

```blaze
//Initialize trip pay inflight if it is nullif (theTripPay.tripPayInflight is null) then{theTripPayInflight is some TripPayInflight initially a TripPayInflight.theTripPay.tripPayInflight = theTripPayInflight.}if (theTripPay.payTrip.assignmentCrewPosition = "FAA" or  theTripPay.tripClass = "P" or      ((theTripPay.nonFlyCode <> null or theTripPay.nonFlyCode <> unknown) and      (theTripPay.assignmentLabel = "P" or theTripPay.assignmentLabel = "H" ))) thentheTripPay.tripPayInflight.positionA = true.elsetheTripPay.tripPayInflight.positionA = false.fcnShow("===>>> fcnSetTripPositionA ... trip pay inflight position A for " theTripPay.tripName " = " theTripPay.tripPayInflight.positionA).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

