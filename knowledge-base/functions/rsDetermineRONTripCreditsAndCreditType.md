# rsDetermineRONTripCreditsAndCreditType

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Rulesets\rsDetermineRONTripCreditsAndCreditType`

## Propósito
12/18//2014 Pedro Loaiza DE5702 - Set the trip credit to sum of duty periods and set the credit type to F

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | PayTrip | |
| theSchedulePeriodPay | SchedulePeriodPay | |
| isCrewPayRequest | boolean | |

## Historial de cambios

```
12/18//2014 Pedro Loaiza DE5702 - Set the trip credit to sum of duty periods and set the credit type to F
12/18//2014 Pedro Loaiza DE5695 - Set the trip credit to sum of duty periods + (RON TAB / 3) and set the credit type to F
03/03/2015 Tim A. - DE5965 - added rule ruleForcedTypeDutyPeriodTypeRON
04/08/2015 Tim A. - DE6162 - modifed rules ruleNotForcedDutyPeriodTypeRON, ruleNotForcedTypeDutyPeriodTypeRONTAFB, ruleForcedDutyPeriodTypeRON to not set CT to "F"
04/15/2015 Tim A. - completely re-factored all rules in this ruleset according to new specification from the business (DE6306)
7/7/2015 - Melissa S - Added to logging
7/24/2015 - DE7101 - Melissa S - Changed to use theTrip.tripPay.tripPayInflight.nonRONdutyPeriodBasePay instead of nonRONDutyPeriodBasePay.  nonRONDutyPeriodBasePay was being set to 0.
7/31/2015 - Melissa S - DE7071 - added a condition to make sure we don't add back in duty premium that takes us over the trip pay
8/1/2015 - DE 7071 - Melissa S - Fixed the rounding function being used
8/3/2015 - DE7142 - refactored ruleset to inlcude both CrewPayRequest rules and TripPayRequest rules
2/7/2017 - CREW-1104 - Rachel Starfield - Adding E label logic.
10/04/2024 - Added S label check in rule07CrewPayRequestForced, rule06CrewPayRequestForced
04/24/25 - APIC-1491 - Jeremiah C - Updates for rules 06 and 21 for the J, U, V, E, S premium updates
```

