# rsDistributeToPremiumPayBuckets

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Rulesets\rsDistributeToPremiumPayBuckets`

## Propósito
US18357:MP:09/10/2014:This ruleset determines the premium pay bucket calculations: basePay, payValue, and payRate.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | PayTrip | |
| theDutyPeriod | PayDutyPeriod | |
| theSchedulePeriodPay | SchedulePeriodPay | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |

## Historial de cambios

```
US18357:MP:09/10/2014:This ruleset determines the premium pay bucket calculations: basePay, payValue, and payRate.
US18588:MP:10/06/2014: Need to ignore CT legs for DT.
10/21/2014 Melissa S.  Refactored 4 similar functions into fcnDistributeToPayBucket (Removed fcnAddToPayBucket, fcnCalculateNonFlyPayBucket, fcnCalculatePremiumPayBucket)
11/11/2014 Pedro L US18924 Update premium pay buckets position A conditions
11/12/2014 Melissa S - DE5527 - Added check to make sure the leg is in the schedule period being checked
03/10/2045 Pedro L DE5881 - Added logic that adds bucket pay value to a transient field to keep track of what has been distributed already to other buckets besides RGA
08/04/2015 Akshay M: DE6198 - Modified rule ruleOvertime1 to add JA premium code logic to pay to the OT Bucket
05/07/2015 Akshay M: DE6491 - Modified ruleOvertime1 and ruleOvertime2, removing assignment label, credit type, and Trip's assignment position checks. Deleted ruleOvertime3 rule, as now it is the same as ruleOvertime2
05/08/2015 Akshay M: DE6513 - Modified ruleDoubleTime1 and ruleDoubleTime2, removing Trip's assignment position checks. Deleted ruleDoubleTime3 rule, as now it is the same as ruleDoubleTime2
05/08/2015 Akshay M: DE6564 - Modified ruleDoubleTimeAndAHalf1 and ruleDoubleTimeAndAHalf2, removing Trip's assignment position checks. Deleted ruleDoubleTimeAndAHalf3 rule, as now it is the same as ruleDoubleTimeAndAHalf2
05/13/2015 Akshay M: DE6619 - Modified ruleTripleTime1 and ruleTripleTime2, removing Trip's assignment position checks. Deleted ruleTripleTime3 rule, as now it is the same as ruleTripleTime2
05/13/2015 Akshay M: DE6620 - Modified ruleTripleTimeAndAHalf1 and ruleTripleTimeAndAHalf2, removing Trip's assignment position checks. Deleted ruleTripleTimeAndAHalf3 rule, as now it is the same as ruleTripleTimeAndAHalf2
05/14/2015 Akshay M: DE6621 - Modified ruleCharterPay1 and ruleCharterPay2, removing Trip's assignment position checks. Deleted ruleCharterPay3 rule, as now it is the same as ruleCharterPay2
05/14/2015 Akshay M: DE6622 - Modified ruleJuniorAvailable1 and ruleJuniorAvailable2, removing Trip's assignment position checks. Deleted ruleJuniorAvailable3 rule, as now it is the same as ruleJuniorAvailable2
7/28/2015 - Melissa S - DE7114 - Modified VJ/JA premium code rules for the OT and AOT buckets to make sure we aren't firing them when the trip has a J label - otherwise we distribute to 2 buckets
7/31/2015 - Melissa S - DE7101 - Modified logic for RIGs vs Premium to use the duty period level comparison for all duty periods in a trip with a RON duty period.
8/1/2015 - DE7136 - Melissa S - Changed to use theDutyPeriodPay.rigsGreaterThanPremium and rigsGreaterThanPremium that had been set in the pay rules
8/2/2105 - DE7128 - Melissa S - Updated RGA/REG rules to set the distributed base pay to the pay value since the multiplier is 1.0 but because of rig vs premium the value in the bucket may be a premium
2/27/2017- CREW-1117 - Rachel Starfield - Adding ruleOvertimeDTBucket and ruleOvertimeADTBucket for E label distribution
05/01/2024 - APIC-1177-Extended-Premium - Jeremiah C. - Added the following rules:  ruleOvertimeExtendedPremiumPayDTBucketPositionAFalse ruleOvertimeExtendedPremiumPayADTBucketPositionATrue ruleOvertimeExtendedPremiumPayDHBucketPositionAFalse ruleOvertimeExtendedPremiumPayADHBucketPositionATrue ruleOvertimeExtendedPremiumPayTTBucketPositionAFalse ruleOvertimeExtendedPremiumPayTTABucketPositionATrue ruleOvertimeExtendedPremiumPayTHBucketPositionAFalse ruleOvertimeExtendedPremiumPayATHBucketPositionATrue
07/01/2024 - APIC-1273 - Jeremiah C. - Added the following rules:  ruleOvertimeExtendedPremiumPayOTBucketPositionATrue ruleOvertimeExtendedPremiumPayAOTBucketPositionATrue ruleOvertimeExtendedPremiumPayDTBucketPayCodeVorJPositionAFalse ruleOvertimeExtendedPremiumPayDTBucketPayCodeVorJPositionATrue ruleOvertimeExtendedPremiumPayJAFBucketPositionAFalse ruleOvertimeExtendedPremiumPayJAABucketPositionATrue
```

