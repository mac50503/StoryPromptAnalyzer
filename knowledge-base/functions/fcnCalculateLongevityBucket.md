# fcnCalculateLongevityBucket

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateLongevityBucket`

## Propósito
10/06/2014 Corey Gu US18522 - Modified the conditions.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aSchedulePeriodPayList | List<SchedulePeriodPay> | |
| aPayCrewMemberList | List<PayCrewMember> | |

## Lógica de negocio

```blaze
aSchedulePeriodPay is some SchedulePeriodPay initially null.aPayCrewMember is some PayCrewMember initially null.aPayBucket is some PayBucket initially null.for each SchedulePeriodPay in aSchedulePeriodPayList as an array of SchedulePeriodPay do{aSchedulePeriodPay = it.fcnShow("===>>> ENTERING fcnCalculateLongevityBucket SP = " aSchedulePeriodPay.schedulePeriodName " ...LPBUCKET payValue now = " aSchedulePeriodPay.getPayBucket("LPBUCKET").payValue).aPayCrewMember = fcnGetPayCrewMemberBySchedulePeriodName(aPayCrewMemberList, aSchedulePeriodPay.schedulePeriodName).if (aPayCrewMember <> null and      aPayCrewMember.payCrewMemberInflight <> null and     aPayCrewMember.payCrewMemberInflight.longevityFlag = true) then {fcnShow("===>>> longevityFlag = " aPayCrewMember.payCrewMemberInflight.longevityFlag).bucketsToExclude is a string initially ";300BUCKET;EATBUCKET;EFBUCKET;EFABUCKET;EXPBUCKET;FI1BUCKET;FI2BUCKET;FI3BUCKET;FI4BUCKET;FI5BUCKET;FP1BUCKET;FP2BUCKET;FP3BUCKET;FP4BUCKET;FP5BUCKET;LODOBUCKET;LPBUCKET;MABUCKET;MAABUCKET;MEBUCKET;MEABUCKET;OEBUCKET;OJABUCKET;OJIBUCKET;PPBUCKET;REBUCKET;REPBUCKET;REPABUCKET;RRABUCKET;SAFBUCKET;SCKBUCKET;SKABUCKET;PFSBUCKET;PFSABUCKET;SLRBUCKET;TOTBUCKET;WCPBUCKET;";//Use the base value of the premium buckets instead of the pay value when adding to longevitybucketsToUseBase is a string initially ";ADHBUCKET;ADTBUCKET;AOTBUCKET;ATHBUCKET;CTBUCKET;CTABUCKET;DHBUCKET;DTBUCKET;IPBUCKET;IPABUCKET;JAABUCKET;JAFBUCKET;OTBUCKET;THBUCKET;TTBUCKET;TTABUCKET;MMAVBUCKET;MMADBUCKET;MMVBUCKET;MMDBUCKET;";for each PayBucket in aSchedulePeriodPay.payBucketList as an array of PayBucket do {aPayBucket = it.if (bucketsToExclude contains match (ignoring case)";"aPayBucket.bucketName";" = false and bucketsToUseBase contains match (ignoring case)";"aPayBucket.bucketName";" = false and aPayBucket.payValue > 0) then{fcnDistributeToPayBucket(aSchedulePeriodPay, "LPBUCKET", aPayBucket.payValue, 1.0, null, null, null, null).fcnShow("===>>> fcnCalculateLongevityBucket for SP " aSchedulePeriodPay.schedulePeriodName " just added " aPayBucket.bucketName "'s pay value of "  aPayBucket.payValue " to LPBUCKET ... payValue now = " aSchedulePeriodPay.getPayBucket("LPBUCKET").payValue).}if (bucketsToUseBase contains match (ignoring case)";"aPayBucket.bucketName";" = true and aPayBucket.baseValue > 0) then{fcnDistributeToPayBucket(aSchedulePeriodPay, "LPBUCKET", aPayBucket.baseValue, 1.0, null, null, null, null).fcnShow("===>>> fcnCalculateLongevityBucket  for SP " aSchedulePeriodPay.schedulePeriodName " just added " aPayBucket.bucketName "'s base value of "  aPayBucket.baseValue " to LPBUCKET ... payValue now = " aSchedulePeriodPay.getPayBucket("LPBUCKET").payValue).}}fcnEnforceLongevityPayMax(aSchedulePeriodPay, aPayCrewMember).}fcnShow("===>>> EXITING fcnCalculateLongevityBucket SP = " aSchedulePeriodPay.schedulePeriodName " ...LPBUCKET payValue now = " aSchedulePeriodPay.getPayBucket("LPBUCKET").payValue).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDistributeToPayBucket](fcnDistributeToPayBucket.md)
- [fcnEnforceLongevityPayMax](fcnEnforceLongevityPayMax.md)
- [fcnGetPayCrewMember](fcnGetPayCrewMember.md)
- [fcnGetPayCrewMemberBySchedulePeriodName](fcnGetPayCrewMemberBySchedulePeriodName.md)
- `fcnShow()`

## Historial de cambios

```
10/06/2014 Corey Gu US18522 - Modified the conditions.
10/16/2014 Corey Gu US18705 - Added pay rate of 1.0 to fcnAddToPayBucket.
10/21/2014 Melissa S.  Refactored 4 similar functions into fcnDistributeToPayBucket (Removed fcnAddToPayBucket, fcnCalculateNonFlyPayBucket, fcnCalculatePremiumPayBucket)
12/11/2014 Pedro Loaiza DE5651 - Added a new condition and changed theTrip.tripPay.payValue for theTrip.tripPay.thisMonthPay
12/11/2014 Pedro Loaiza DE5645 - Replaced the list of nonFlyCode with this list WCP,WCI,WCS,SLP,EFL,LME,LMA,IL
01/09/2015 Tim A. DE5645 - Added SL1 to the list of excluded nonfly codes
02/04/2015 Tim A. DE5933 - changed logic of function to add all bucket pay values expect those in a list
08/26/2015 Tim A. DE5933 - removed PERBUCKET AND PEABUCKET from buckets to exclude - DE7298
06/20/2017 Tim A. CREW-65 - added SAFBUCKET to buckets to exclude
```

