# rsCalculateDutyPeriodCredits

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Rulesets\rsCalculateDutyPeriodCredits`

## Propósito
09/-02/2014 Corey Gu DE4909, added statement "theDutyPeriod.dutyPeriodPay.payValue = theDutyPeriodPay.sumLegBaseCredits."in ruleNoCreditType1.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | PayDutyPeriod | |
| theDutyPeriodPay | DutyPeriodPay | |
| premiumCodeTrue | boolean | |

## Historial de cambios

```
09/-02/2014 Corey Gu DE4909, added statement "theDutyPeriod.dutyPeriodPay.payValue = theDutyPeriodPay.sumLegBaseCredits."in ruleNoCreditType1.
10/10/2014 Tim a - DE5162 - added new rule ruleForcedCreditType
6/3/2015 - DE6649 - Melissa S - Added new rules for credit type E, added isLegSumGtDHR property
6/9/2015 - DE6671 - Melissa S - Added new rules for credit type P when the duty period is under a reserve block, updated existing P rules to fire when not under a reserve block
6/23/2015 - DE6878 - Melissa S - Modified rules for P credit type.  Trips with R label not under a reserve block should behave as if under reserve block
7/30/2015 - DE7144 - Melissa S - Modified ruleDCreditType to only use DHR, and not to compare the passed in value (base pay)
8/1/2015 - DE7136 - Melissa S - Added setting new proprty theDutyPeriodPay.rigsGreaterThanPremium that will be used in the premium bucket distributon
9/1/2015 - DE7349 - Melissa S - Changed the property being used to look for a RAP Association to use the list on payDutyPeriodInflight
2/7/2017 - CREW-1118 - Mark Bevington - Adding E Label where J or U or V labels exist.
10/04/2024 - Added S label check in ruleForcedCreditType
```

