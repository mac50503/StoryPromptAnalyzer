# fcnShowPlnLegPaySummary

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\PlanningPay\Functions\fcnShowPlnLegPaySummary`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPlnLegPay | PlnLegPay | |

## Lógica de negocio

```blaze
aPayLeg is some PayLeg initially aPlnLegPay.payLeg.fcnShow("............Planning Leg: " aPlnLegPay.sequenceNumber " " aPayLeg.departureLocation "-" aPayLeg.arrivalLocation" ...skd dep time = " DateTimeUtilities.getShortDateTimeString(aPayLeg.scheduledDepartureDateTime) " ...skd arr time = " DateTimeUtilities.getShortDateTimeString(aPayLeg.scheduledArrivalDateTime)).fcnShow("...............leg pay = " fcnRoundUpAt2DecimalPlaces(aPlnLegPay.payValue)  " ...credit type = " aPlnLegPay.creditType).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

## Llamado por

- [fcnShowPlnTripPaySummary](fcnShowPlnTripPaySummary.md)

