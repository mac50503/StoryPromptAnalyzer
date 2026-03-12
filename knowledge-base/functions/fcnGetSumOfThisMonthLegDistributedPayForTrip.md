# fcnGetSumOfThisMonthLegDistributedPayForTrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetSumOfThisMonthLegDistributedPayForTrip`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |
| aShcedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
retVal is a real initially 0.0.if (aTripPay <> null and aShcedulePeriodPay <> null) then{for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do{if (fcnDoesDutyPeriodPayBeginInSchedulePeriodPay(it, aShcedulePeriodPay)) thenretVal += it.distributedPay.}}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDoesDutyPeriodPayBeginInSchedulePeriodPay](fcnDoesDutyPeriodPayBeginInSchedulePeriodPay.md)

