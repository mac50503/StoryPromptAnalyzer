# fcnGetDutyPeriodPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetDutyPeriodPay`

## Propósito
7/6/2015 - DE6983 - Melissa S - RON pays base pay for holiday pay

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
if (theDutyPeriod.creditType = "P" or theDutyPeriod.dutyPeriodPay.creditType = "P" or theDutyPeriod.creditType = "F" or theDutyPeriod.dutyPeriodPay.creditType = "F" ortheDutyPeriod.dutyType = "RON")then return theDutyPeriod.dutyPeriodPay.basePay.else if (theDutyPeriod.creditType = "E" or theDutyPeriod.dutyPeriodPay.creditType = "E") then return fcnMaxOf3Numbers(theDutyPeriod.dutyPeriodPay.basePay, theDutyPeriod.dutyPeriodPay.dutyHourRatio, theDutyPeriod.dutyPeriodPay.sumLegBaseCredits).else return fcnMaxOf4Numbers(theDutyPeriod.dutyPeriodPay.basePay, theDutyPeriod.dutyPeriodPay.dutyHourRatio, theDutyPeriod.dutyPeriodPay.sumLegBaseCredits, theDutyPeriod.dutyPeriodPay.dutyPeriodMinimum).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnMaxOf3Numbers](fcnMaxOf3Numbers.md)
- [fcnMaxOf4Numbers](fcnMaxOf4Numbers.md)

## Llamado por

- [fcnGetDutyPeriodPayByIndex](fcnGetDutyPeriodPayByIndex.md)

## Historial de cambios

```
7/6/2015 - DE6983 - Melissa S - RON pays base pay for holiday pay
```

