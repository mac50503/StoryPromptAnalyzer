# rsCalculateRegularPayBucket

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Rulesets\rsCalculateRegularPayBucket`

## Propósito
10/15/2014:MP:US18618. Restructured REG rules as per new req.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripPay | TripPay | |
| theSchedulePeriodPay | SchedulePeriodPay | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |

## Historial de cambios

```
10/15/2014:MP:US18618. Restructured REG rules as per new req.
10/20/2014:BL:US18452. Do not add Reserve trip pay to the REG and RGA buckets
11/05/2014 Pedro L - US18920 Update existing Pay Bucket logic to reference the new isPositionA boolean in the rule conditions
12/10/2014 Ben Lang - Updated regular rules to use the fcnDoesDutyPeriodPayBeginInSchedulePeriodPay function (DE5696)
12/29/2014 Melissa S DE5706 - Corrected error in new Force rule that didn't check crew position and was always using REGBUCKET
01/19/2015 Tim A. DE5779 - added code to back out overtime and overnight bucket pay values from REG/RGA to prevent double dipping (distributing same pay into more than one bucket)
03/10/2015 Pedro L - DE5881 Added distributedPay to ruleRegularPayBucketTripPositionA to get the correct RGA bucket value
22 Jan 2015 TimA. US19475 - refactoring distribution of trip level pay to buckets to instead distribe duty period level pay
03/16/2015 Ben Lang DE6063 - Deleted ruleForcedTripBaseGtDutyBasePositionAfalse rule. This logic is handled by prorated pay.
05/11/2015 Pedro L DE6473 Added the rule ruleRegularPayBucketTripPositionNotANotFAAForcedLabelV
06/03/2015 Ben L DE6473 - Changed the ruleRegularPayBucketTripPositionNotANotFAAForcedLabelV rule to ruleRegularPayBucketTripPositionNotAForcedLabelUV and cleaned up the ruleRegularPayBucketTripPositionA rule
06/16/2015 - Ben Lang - DE6669 - Added logic to use the first leg's scheduleDepartureDateTime for Inflight
```

