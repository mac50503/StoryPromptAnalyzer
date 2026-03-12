# fcnDistributeToPayBucket

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnDistributeToPayBucket`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aSchedulePeriodPay | SchedulePeriodPay | |
| bucketCode | string | |
| amount | real | |
| rate | real | |
| eventDate | DateTime | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
dateFallsWithinRange is a boolean initially fcnIsDateTimeWithinReportFilterRange(eventDate, reportFilterStart, reportFilterEnd).if (aTripPay <> null and aTripPay.payTrip <> null and aTripPay.payTrip.creditType = "F" and aTripPay.payTrip.basePay = 0.0 and bucketCode <> "300BUCKET") then{fcnShow("===>>> EXITING fcnDistributeToPayBucket ...SP = " aSchedulePeriodPay.schedulePeriodName " ...operation aborted due to trip " aTripPay.tripName " is forced to pay zero").}else if (dateFallsWithinRange is equal to true) then{payBucketFound is a boolean initially false.pb is some PayBucket initially aSchedulePeriodPay.getPayBucket(bucketCode).if (pb <> null) thenpb.payRate = rate.payBucketFound = aSchedulePeriodPay.addToBucketPayValue(bucketCode, amount).fcnAddTripPayBuckets(bucketCode, amount, rate, aTripPay, false).if (payBucketFound) then {fcnShow("===>>> fcnDistributeToPayBucket ...SP = " aSchedulePeriodPay.schedulePeriodName "...bucket = " bucketCode " amount = " fcnRoundUpAt2DecimalPlaces(amount) ", rate = " aSchedulePeriodPay.getPayBucket(bucketCode).payRate ", baseValue = " fcnRoundUpAt2DecimalPlaces(aSchedulePeriodPay.getPayBucket(bucketCode).baseValue) ", payValue = " fcnRoundUpAt2DecimalPlaces(aSchedulePeriodPay.getPayBucket(bucketCode).payValue) " ...new bucket pay value = " fcnRoundUpAt2DecimalPlaces(aSchedulePeriodPay.getPayBucket(bucketCode).payValue)", eventDate = " eventDate).}elsefcnShow("===>>> fcnDistributeToPayBucket ...SP = " aSchedulePeriodPay.schedulePeriodName "...bucket " bucketCode " was not found...").}elsefcnShow("===>>> EXITING fcnDistributeToPayBucket ......SP = " aSchedulePeriodPay.schedulePeriodName "...operation aborted due to event date not falling withing date range filter... event date = " eventDate " ...date range start = " reportFilterStart " ...date range end = " reportFilterEnd).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnAddTripPayBuckets](fcnAddTripPayBuckets.md)
- [fcnIsDateTimeWithinReportFilterRange](fcnIsDateTimeWithinReportFilterRange.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

## Llamado por

- [fcnCalculateHolidayPayBucketFromReserve](fcnCalculateHolidayPayBucketFromReserve.md)
- [fcnCalculateLongevityBucket](fcnCalculateLongevityBucket.md)
- [fcnCalculateTripCpCodePay](fcnCalculateTripCpCodePay.md)
- [fcnDistributeRedEyePremiumToPayBucket](fcnDistributeRedEyePremiumToPayBucket.md)
- [fcnDistributeToLateReturnBuckets](fcnDistributeToLateReturnBuckets.md)

