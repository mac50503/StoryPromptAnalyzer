# fcnDistributeRedEyePremiumToPayBucket

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDistributeRedEyePremiumToPayBucket`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | PayTrip | |
| theDutyPeriod | PayDutyPeriod | |
| theSchedulePeriodPay | SchedulePeriodPay | |
| thePayLeg | PayLeg | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |
| dpIsUnderReserve | boolean | |

## Lógica de negocio

```blaze
// calculates the amount to distributeredEyeAmount is a real. if(thePayLeg.basePay > thePayLeg.legPay.overflyCredits and thePayLeg.legPay.overflyCredits > 0) then {redEyeAmount = (thePayLeg.basePay - thePayLeg.legPay.overflyCredits) * 0.15;}else{redEyeAmount = thePayLeg.basePay * 0.15;}if (thePayLeg.creditType = (ignoring case)  "F" and thePayLeg.payLegInflight.originalBasePay > 0 and dpIsUnderReserve) then {redEyeAmount = thePayLeg.payLegInflight.originalBasePay * 0.15;}// check the corresponding bucketisABucket is a boolean initially fcnIsABucketApplicable(theTrip, theDutyPeriod, thePayLeg);if(isABucket) then{fcnDistributeToPayBucket(theSchedulePeriodPay, "REPABUCKET",  redEyeAmount, 1.0, fcnGetFirstFlyingLegScheduledDepartureDateTime(theDutyPeriod), reportFilterStart, reportFilterEnd, theTrip.tripPay).}else{fcnDistributeToPayBucket(theSchedulePeriodPay, "REPBUCKET", redEyeAmount, 1.0, fcnGetFirstFlyingLegScheduledDepartureDateTime(theDutyPeriod), reportFilterStart, reportFilterEnd, theTrip.tripPay).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDistributeToPayBucket](fcnDistributeToPayBucket.md)
- [fcnGetFirstFlyingLeg](fcnGetFirstFlyingLeg.md)
- [fcnGetFirstFlyingLegScheduledDepartureDateTime](fcnGetFirstFlyingLegScheduledDepartureDateTime.md)
- [fcnIsABucketApplicable](fcnIsABucketApplicable.md)

