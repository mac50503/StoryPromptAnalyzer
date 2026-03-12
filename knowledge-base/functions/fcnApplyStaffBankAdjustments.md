# fcnApplyStaffBankAdjustments

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnApplyStaffBankAdjustments`

## Propósito
08/20/2014 Corey Gu US18401 - Initial development

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSchedulePeriodPay | SchedulePeriodPay | |
| thePayCrewMember | PayCrewMember | |
| reportFilterBegin | DateTime | |
| reportFilterEnd | DateTime | |

## Lógica de negocio

```blaze
experienceBuckets is a string initially ";ADHBUCKET;ADTBUCKET;AOTBUCKET;ATHBUCKET;DHBUCKET;DTBUCKET;IFBUCKET;IFABUCKET;JAABUCKET;".experienceBuckets = experienceBuckets "JAFBUCKET;OTBUCKET;REGBUCKET;RGABUCKET;THBUCKET;TTBUCKET;TTABUCKET;UBBUCKET;UBABUCKET;".experienceBuckets = experienceBuckets "ONBUCKET;ONABUCKET;".payAdjustmentCode is a string.bucketFound is a boolean initially false.pb is some PayBucket initially null.yearsOfExperience is an integer initially Years.yearsBetween(thePayCrewMember.payCrewMemberInflight.seniorityDateTime, theSchedulePeriodPay.schedulePeriod.schedulePeriodStart.withDayOfMonth(15)).years.fcnShow("===>>> fcnApplyStaffBankAdjustments ...SP = " theSchedulePeriodPay.schedulePeriodName "  ... reportFilterBegin = " reportFilterBegin " ... reportFilterBegin = " reportFilterEnd).pa is some PayAdjustment initially null.payAdjustmentAmount is a real initially 0.0.for each PayAdjustment in theSchedulePeriodPay.payAdjustmentList  as an array of PayAdjustment do{if (fcnIsDateTimeWithinReportFilterRange(it.effectiveDateTime, reportFilterBegin, reportFilterEnd)) then{pa = it.payAdjustmentCode = pa.adjustmentCode.select payAdjustmentCodecase "FSBUCKET" : payAdjustmentCode = "EATBUCKET".case "WCPBUCKET" : payAdjustmentCode = "OJIBUCKET".case "LVPBUCKET" : payAdjustmentCode = "PERBUCKET".case "LVABUCKET" : payAdjustmentCode = "PFABUCKET".case "SLPBUCKET" : payAdjustmentCode = "SCKBUCKET".case "SLABUCKET" : payAdjustmentCode = "SKABUCKET".case "JDABUCKET" : payAdjustmentCode = "JRABUCKET".case "JDBUCKET" : payAdjustmentCode = "JRYBUCKET".pb = theSchedulePeriodPay.getPayBucket(payAdjustmentCode).if (pb <> null) thenfcnShow("===>>> BEFORE ADJUSTMENT OF " it.amount " TO " payAdjustmentCode " ...base = " pb.baseValue " ...rate = " pb.payRate " ...pay value = " pb.payValue).// ADDED WITH DEFECT DE6737...if (payAdjustmentCode = (ignoring case) ("FP1BUCKET" or "FP2BUCKET" or "FP3BUCKET" or "FP4BUCKET" or "FP5BUCKET" or "FI1BUCKET" or "FI2BUCKET" or "FI3BUCKET" or "FI4BUCKET" or "FI5BUCKET")) then{perDiemTimeAdjustment is a real initially fcnGetHoursInDecimalFormatFromHoursAndMinutes(pa.amount).perDiemAmountAdjusment is a real initially (perDiemTimeAdjustment * pb.payRate).perDiemAmountAdjusment = fcnRoundUpAt2DecimalPlaces(perDiemAmountAdjusment).bucketFound = theSchedulePeriodPay.addToBucketPayValue(payAdjustmentCode, perDiemAmountAdjusment).fcnShow("===>>> calling addToBucketPayValue for " payAdjustmentCode  " …adjustment amount  = " perDiemAmountAdjusment " ...bucket found = " bucketFound).}// ADDED WITH USER STORY US19042...else if (payAdjustmentCode = (ignoring case) ("300BUCKET" or "EATBUCKET" or "LPBUCKET" or "OEBUCKET")) then{bucketFound = theSchedulePeriodPay.addToBucketPayValue(payAdjustmentCode, pa.amount).fcnShow("===>>> calling addToBucketPayValue for " payAdjustmentCode  " …adjustment amount  = " it.amount " ...bucket found = " bucketFound).}else{bucketFound = theSchedulePeriodPay.addToBucketBaseValue(payAdjustmentCode, pa.amount).fcnShow("===>>> calling addToBucketBaseValue for " payAdjustmentCode  " …adjustment amount  = " it.amount " ...bucket found = " bucketFound).}if (bucketFound and yearsOfExperience >= 25 and experienceBuckets contains match (ignoring case)";"payAdjustmentCode";") then{bucketFound = theSchedulePeriodPay.addToBucketBaseValue("EXPBUCKET", pa.amount);if (bucketFound) then{theSchedulePeriodPay.getPayBucket("EXPBUCKET").baseValue = math().max(0.0, theSchedulePeriodPay.getPayBucket("EXPBUCKET").baseValue).    //// DE7625 - no negative values for EXP buckettheSchedulePeriodPay.getPayBucket("EXPBUCKET").payValue = math().max(0.0, theSchedulePeriodPay.getPayBucket("EXPBUCKET").payValue).    //// DE7625 - no negative values for EXP bucket}fcnShow("===>>> calling addToBucketBaseValue for EXPBUCKET …adjustment amount  = " it.amount " ...bucket found = " bucketFound).}if (pb <> null) thenfcnShow("===>>> AFTER ADJUSTMENT OF " pa.amount " TO " payAdjustmentCode " ...base = " pb.baseValue " ...rate = " pb.payRate " ...pay value = " pb.payValue).}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetHoursInDecimalFormatFromHoursAndMinutes](fcnGetHoursInDecimalFormatFromHoursAndMinutes.md)
- [fcnIsDateTimeWithinReportFilterRange](fcnIsDateTimeWithinReportFilterRange.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

## Historial de cambios

```
08/20/2014 Corey Gu US18401 - Initial development
10/21/2014 Melissa S.  Refactored 4 similar functions into fcnDistributeToPayBucket (Removed fcnAddToPayBucket, fcnCalculateNonFlyPayBucket, fcnCalculatePremiumPayBucket)
11/12/2104 Tim A. 4 adjustment codes apply to bucket pay value, all others apply to bucket base value
10/14/2015 Tim A. - DE7625 - no negative values for EXP bucket due to staff bank adjustments
10/05/2017 Tim A. - PayCalcs - added data analytics code to staff bank adjustments
08/23/2018 Rachel S. CREW-10064 - PayCalcs - removed data analytics code
```

