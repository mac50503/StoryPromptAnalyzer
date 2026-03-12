# fcnGetSumOfDutyCreditValues

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetSumOfDutyCreditValues`

## Propósito
Ben Lang - US15815 - Reviewed Code - This code calculates sums up the payValues of a certain trip

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripPay | TripPay | |

## Lógica de negocio

```blaze
sumOfDutyCredits is a real initially 0.if (theTripPay.dutyPeriodPayList is not equal to null and     theTripPay.dutyPeriodPayList.size() > 0) then{for each DutyPeriodPay in theTripPay.dutyPeriodPayList as an array of DutyPeriodPay do{sumOfDutyCredits = sumOfDutyCredits + fcnRoundUpAt2DecimalPlaces(it.payValue).}}return fcnRoundUpAt2DecimalPlaces(sumOfDutyCredits).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)

## Llamado por

- [fcnGetTripExcess](fcnGetTripExcess.md)

## Historial de cambios

```
Ben Lang - US15815 - Reviewed Code - This code calculates sums up the payValues of a certain trip
```

