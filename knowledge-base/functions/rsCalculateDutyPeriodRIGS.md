# rsCalculateDutyPeriodRIGS

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Rulesets\rsCalculateDutyPeriodRIGS`

## Propósito
Ben Lang - US16984 - 7/1/2014

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | PayDutyPeriod | |
| theDutyPeriodPay | DutyPeriodPay | |
| thePreviousDutyPeriod | PayDutyPeriod | |
| theTripList | List<PayTrip> | |

## Historial de cambios

```
Ben Lang - US16984 - 7/1/2014
Tim Albright - US18524 - 9/25/2014
Tim Albright - DE6064 - 03/19/2015
Tim Albright - US18524 - 9/30/2014 - added rules for calculating duty amount to consider associated airport stanbys
6/17/2017 - DE6577 - Melissa S - Changed DHR Calculation.  Instead of comparing scheduled duration vs actual duration, the DHR start/end
7/1/2015 - DE6910 - Melissa S - Updated ruleDetermineDhrStart - Original report time for this rule should come from the payDutyPeriodInflight.originalScheduledReportDateTime and not the scheduledReportDateTime
Tim Albright - DE7397 - 9/16/2015 - added ruleSetRigsGreaterThanPremium
10/6/2015 - DE7555 - Melissa S - Updated all calculations related to DHR to use new common function shared by fcnCalculateThrAndAdgAndDhr
12/11/2024 - APIC-1441 - Added new rule ruleAdjustPayValueForEDDLeg
12/19/2024 - APIC-1450 - Added new rule ruleAdjust_DPSumLegTotalCredits_With_PremiumLabelForcedEDDLegs_When_RigsGreaterThanPremium
```

