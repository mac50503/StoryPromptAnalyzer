# rsCalculatePayBucketsRigs

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Rulesets\rsCalculatePayBucketsRigs`

## Propósito
09/18/2014 Corey Gu US16583- In ruleUnscheduledOvernight1 and ruleUnscheduledOvernight2, changed the way they checked if a crew position is FAA or not.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | PayDutyPeriod | |
| thePreviousDutyPeriod | PayDutyPeriod | |
| theTrip | PayTrip | |
| theSchedulePeriodPay | SchedulePeriodPay | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |
| theTripList | List<PayTrip> | |

## Historial de cambios

```
09/18/2014 Corey Gu US16583- In ruleUnscheduledOvernight1 and ruleUnscheduledOvernight2, changed the way they checked if a crew position is FAA or not.
10/21/2014 Melissa S.  Refactored 4 similar functions into fcnDistributeToPayBucket (Removed fcnAddToPayBucket, fcnCalculateNonFlyPayBucket, fcnCalculatePremiumPayBucket)
11/6/2014 Mitesh P US18923 updated rules as per new A position definition
03/06/2015 Tim A. DE6035 - added logic to increment trip's ronRigTrotal property
03/18/2015 Tim A. DE5777 - added variables ronEndingNonflyCodes, ronEndingNonfly and rules ruleSetRonEndingNonfly, ruleCalculateRONTAFBUsingRonEndingNonfly
4/30/15 - Pedro Loaiza - Added 4 rules and one variable needed for the calculation of EXP.  Each rule has comments that they are needed for EXP calculation
7/6/2105 Tim A. DE6971 - added varaible dutyPeriodContainsAllNonPaidLimos and modified rules ruleUnscheduledOvernight1, ruleUnscheduledOvernight2 and ruleUnscheduledOvernight3 to use it
12/30/2015 - Melissa S - CSCH-1501 - Fixed for a trip with multiple RONs - need to prevent double counting towards RON RIG.
```

