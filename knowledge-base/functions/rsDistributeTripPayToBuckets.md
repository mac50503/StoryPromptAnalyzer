# rsDistributeTripPayToBuckets

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Rulesets\rsDistributeTripPayToBuckets`

## Propósito
03/10/2015 Pedro L - DE5881 Removed rule that added excess to RGA bucket because when RGA bucket is updated in rsCalculateRegularPayBucket, it uses proratedPay that already contains the excess

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripPay | TripPay | |
| theSchedulePeriodPay | SchedulePeriodPay | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |
| previousSchedulePeriodPay | SchedulePeriodPay | |

## Historial de cambios

```
03/10/2015 Pedro L - DE5881 Removed rule that added excess to RGA bucket because when RGA bucket is updated in rsCalculateRegularPayBucket, it uses proratedPay that already contains the excess
03/15/2015 Tim A. - DE5777 - added rules ruleTripWithRonDutyPositionAtrue and ruleTripWithRonDutyPositionAfalse
01/05/2015 Akshay M DE6454 - removed F credit type checks, and added U assignment label for OT/OTA bucket rules
05/11/2015 Pedro L - DE6557 Added   - fcnGetTripDistributedBasePay(previousSchedulePeriodPay,theTripPay.sequenceNumber) to the condition in ruleUVLabelForcedPositionAfalse that checks that it is greater
than 0 since the calculation uses that and that is what was causing it to be negative.
05/15/2015 Tim A. DE6559 - refactored rules ruleUVLabelForcedPositionAtrue and ruleUVLabelForcedPositionAfalse to distribute trip base pay - base pay of ineligible duty periods
06/03/2015 Ben L. DE6747 - Deleted rules ruleUVLabelForcedPositionAtrue and ruleUVLabelForcedPositionAfalse and added rules ruleUVLabelNotForced and ruleUVLabelForced
6/12/2015 - Melissa S - DE6653 - Added J assignment labels to ruleUVLabelNotForced and ruleUVLabelForced and renamed to include J in the name
6/16/2015 - Ben Lang - DE6669 - Added logic to use the first leg's scheduleDepartureDateTime for Inflight
6/18/2015 - Melissa S - DE6867 - Updated rules for RON Duty to distribute based on the schedule period the Duty Period falls in, not the trip.  Trips with duty periods in multiple schedule periods were not getting distributed correctly.
8/1/2015 - Melissa S - DE7070 - Fixed distribution - wasn't subtracting already distributed pay because it was in the wrong loop (P credit type)
8/2/2105 - DE7128 - Melissa S - Changed the 2 RON rules to not distribute negative trip excess
3/1/2017 - CREW-1117 - Rachel Starfield - Added E Label to rules.
10/04/2024 - Added new rule ruleSLabelForced for S label, regardsless of reserve or not. Added S label check in ruleJUVELabelNotForced
```

