# rsDetermineTripCreditsAndCreditType

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Rulesets\rsDetermineTripCreditsAndCreditType`

## Propósito
08/06//2014 Mitesh P US17872 -ruleDutySumGtPvNotLateFlt18, ruleDutySumNotGtPvNotLateFlt19  rules modified to ignore THR value for "P" trips that are not late

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | PayTrip | |

## Llamado por

- [fcnModifyDutyAndTripValuesForSplitGuaranty](fcnModifyDutyAndTripValuesForSplitGuaranty.md)

## Historial de cambios

```
08/06//2014 Mitesh P US17872 -ruleDutySumGtPvNotLateFlt18, ruleDutySumNotGtPvNotLateFlt19  rules modified to ignore THR value for "P" trips that are not late
02/172015 Tim A. DE5866 - Added rule ruleNotForcedLabelV
03/06/2015 Tim A. DE6035 - Added rule ruleAddRonRigToTripPay
6/9/2015 - DE6671 - Melissa S - Added new rules for credit type P when the trip is under a reserve block, updated existing P rules to fire when not under a reserve block
8/1/2015 - DE7136 - Melissa S - Added setting theTripPay.tripPayInflight.rigsGreaterThanPremium that will be used in the premium bucket distributon
8/28/2015 - DE7325 - Melissa S - Removed rules ruleForcedTypeNotLabelJVUReserve and ruleForcedTypeNotLabelJVUReserve2, Changed ruleForcedTypeNotLabelJVU to not look at underReserve condition
8/28/2015 - DE7324 - Melissa S - Changed ruleAddDutyPremium to not look at underReserve condition
9/1/2015 - DE7353 - Melissa S - Changed dutySumGtePassedValue to dutySumGtPassedValue
2/7/2017 - CREW-1118 - Mark Bevington - Adding E Label where J or U or V labels exist.
3/1/2017 - CREW-1118 - Rachel Starfield - Fixed handling of forced E label
09/30/2024 - Added S label check in all Forced Scenario and appended S at the end of name for ruleForcedTypeNotLabelJVUES and for ruleAddDutyPremium added S check
10/04/2024 - Added ruleForcedTypeLabelS new rule for S label. This will be done regardless if it is reserve or not
```

