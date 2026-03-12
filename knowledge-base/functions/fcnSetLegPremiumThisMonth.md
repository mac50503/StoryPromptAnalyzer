# fcnSetLegPremiumThisMonth

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnSetLegPremiumThisMonth`

## Propósito
7/9/2015 - Melissa S - DE7016 - Modified dutyPremiumTotal to come from the total legPremium for the trip instead of just this month's leg premium

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
if (aTripPay <> null and aTripPay.tripPayInflight <> null and aSchedulePeriodPay <> null) then {aTripPay.tripPayInflight.thisMonthLegPremium = fcnGetSumOfThisMonthLegPremiumForTrip(aTripPay, aSchedulePeriodPay).aTripPay.tripPayInflight.legPremium = fcnGetSumOfLegPremiumForTrip(aTripPay).if (aTripPay.payTrip.creditType = "F" and        aTripPay.tripPayInflight.legPremium > 0.0) then{aTripPay.tripPayInflight.dutyPremiumTotal += aTripPay.tripPayInflight.legPremium.aTripPay.tripPayInflight.dutyPremiumTotal = fcnRoundUpAt2DecimalPlaces(aTripPay.tripPayInflight.dutyPremiumTotal).fcnLogRuleFireEvent("ruleInflightAddToTripDutyPremium", "rsDetermineCarryOverDutyPeriodCredits", "adding duty premium of " aTripPay.tripPayInflight.legPremium " to trip = " aTripPay.tripName "'s dutyPremiumTotal ...value now = " aTripPay.tripPayInflight.dutyPremiumTotal).}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetSumOfLegPremium](fcnGetSumOfLegPremium.md)
- [fcnGetSumOfLegPremiumForTrip](fcnGetSumOfLegPremiumForTrip.md)
- [fcnGetSumOfThisMonthLegPremiumForTrip](fcnGetSumOfThisMonthLegPremiumForTrip.md)
- [fcnLogRuleFireEvent](fcnLogRuleFireEvent.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- [rsDetermineCarryOverDutyPeriodCredits](rsDetermineCarryOverDutyPeriodCredits.md)

## Historial de cambios

```
7/9/2015 - Melissa S - DE7016 - Modified dutyPremiumTotal to come from the total legPremium for the trip instead of just this month's leg premium
```

