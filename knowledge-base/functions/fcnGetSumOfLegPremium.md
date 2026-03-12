# fcnGetSumOfLegPremium

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetSumOfLegPremium`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriodPay | DutyPeriodPay | |

## Lógica de negocio

```blaze
retVal is a real initially 0.0.if (aDutyPeriodPay <> null and     aDutyPeriodPay.legPayList <> null and     aDutyPeriodPay.legPayList.size() > 0 andaDutyPeriodPay.rigsGreaterThanPremium = false) then{for each LegPay in aDutyPeriodPay.legPayList as an array of LegPay doretVal += it.payValue - it.basePay.}return retVal.
```

## Llamado por

- [fcnGetSumOfLegPremiumForTrip](fcnGetSumOfLegPremiumForTrip.md)
- [fcnGetSumOfLegPremiumForTripAboveDT](fcnGetSumOfLegPremiumForTripAboveDT.md)
- [fcnGetSumOfLegPremiumForTripAboveOT](fcnGetSumOfLegPremiumForTripAboveOT.md)
- [fcnGetSumOfThisMonthLegPremiumForTrip](fcnGetSumOfThisMonthLegPremiumForTrip.md)
- [fcnSetLegPremiumThisMonth](fcnSetLegPremiumThisMonth.md)
- [fcnSetRigsGreaterThanPremiumForTrip](fcnSetRigsGreaterThanPremiumForTrip.md)

