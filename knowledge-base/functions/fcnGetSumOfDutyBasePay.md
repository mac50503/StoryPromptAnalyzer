# fcnGetSumOfDutyBasePay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetSumOfDutyBasePay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripPay | TripPay | |

## Lógica de negocio

```blaze
sumOfDutyBaseCredits is a real initially 0.if (theTripPay.dutyPeriodPayList is not equal to null and     theTripPay.dutyPeriodPayList.size() > 0) then{for each DutyPeriodPay in theTripPay.dutyPeriodPayList as an array of DutyPeriodPay do{sumOfDutyBaseCredits = sumOfDutyBaseCredits + fcnRoundUpAt2DecimalPlaces(it.basePay).}}return fcnRoundUpAt2DecimalPlaces(sumOfDutyBaseCredits).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)

