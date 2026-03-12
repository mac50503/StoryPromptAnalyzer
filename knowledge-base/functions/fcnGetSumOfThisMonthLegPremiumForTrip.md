# fcnGetSumOfThisMonthLegPremiumForTrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetSumOfThisMonthLegPremiumForTrip`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |
| aShedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
retVal is a real initially 0.0.if (aTripPay <> null and aShedulePeriodPay <> null and     aTripPay.tripPayInflight <> null) then{for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do{if (fcnDoesDutyPeriodPayBeginInSchedulePeriodPay(it, aShedulePeriodPay)) thenretVal += fcnGetSumOfLegPremium(it).}}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDoesDutyPeriodPayBeginInSchedulePeriodPay](fcnDoesDutyPeriodPayBeginInSchedulePeriodPay.md)
- [fcnGetSumOfLegPremium](fcnGetSumOfLegPremium.md)

## Llamado por

- [fcnSetLegPremiumThisMonth](fcnSetLegPremiumThisMonth.md)

