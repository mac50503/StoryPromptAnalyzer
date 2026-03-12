# fcnGetTripExcess

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetTripExcess`

## Propósito
trip excess is the calculated trip pay minus the sum of all the duty period calculated pay.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
sumOfDutyPeriods is a real initially 0.tripPay is a real initially 0.sumOfDuties is a real initially 0.if (aTripPay is not equal to null) then {tripPay = aTripPay.payValue.fcnShow("===>>> Entering fcnGetTripExcess for TripPay: " aTripPay.tripName " ...initial trip pay ....." tripPay).if (aTripPay.tripPayInflight <> null) then {tripPay -= aTripPay.tripPayInflight.ronRigTotal.fcnShow("===>>> fcnGetTripExcess for TripPay: " aTripPay.tripName " ...trip pay - trip RIG = trip pay ....." tripPay).}sumOfDuties = fcnGetSumOfDutyCreditValues(aTripPay).fcnShow("===>>> Entering fcnGetTripExcess for TripPay: " aTripPay.tripName " ...trip pay - sum of duty period pay = trip pay ....." tripPay " - "  sumOfDuties).tripPay = fcnRoundUpAt2DecimalPlaces(tripPay).sumOfDuties = fcnRoundUpAt2DecimalPlaces(fcnGetSumOfDutyCreditValues(aTripPay)).fcnShow("===>>> Exiting fcnGetTripExcess for TripPay: " aTripPay.tripName " ...trip pay - sum of duty period pay = trip pay ....." tripPay " - "  sumOfDuties " = " fcnRoundUpAt2DecimalPlaces(tripPay - sumOfDuties)).return fcnRoundUpAt2DecimalPlaces(math().max(0.0, fcnRoundUpAt2DecimalPlaces(tripPay - sumOfDuties))).}return 0.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetSumOfDutyCreditValues](fcnGetSumOfDutyCreditValues.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

## Llamado por

- [fcnDetermineDutyTripExcess](fcnDetermineDutyTripExcess.md)

## Historial de cambios

```
trip excess is the calculated trip pay minus the sum of all the duty period calculated pay.
Ben Lang - US15815 - Reviewed Code
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
7/31/2015 - Melissa S - DE7071 - Rmeoved RON RIG from calculation when computing trip excess
```

