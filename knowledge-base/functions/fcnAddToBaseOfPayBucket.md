# fcnAddToBaseOfPayBucket

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnAddToBaseOfPayBucket`

## Propósito
PL:10/14/2014: US18646 Initial development

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSchedulePeriodPay | SchedulePeriodPay | |
| theBucketCode | string | |
| theBaseValue | real | |
| thePayRate | real | |
| eventDate | DateTime | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
if (fcnIsDateTimeWithinReportFilterRange(eventDate, reportFilterStart, reportFilterEnd)) then{bucketFoundTrue is a boolean initially false.if (theSchedulePeriodPay.getPayBucket(theBucketCode) <> null) thenbucketFoundTrue = true.thePayBucket is some PayBucket initially theSchedulePeriodPay.getPayBucket(theBucketCode).if (thePayBucket <> null) thenthePayBucket.payRate = thePayRate.theSchedulePeriodPay.addToBucketBaseValue(theBucketCode, theBaseValue).fcnAddTripPayBuckets(theBucketCode, theBaseValue, thePayRate, aTripPay, true).fcnShow("===>>> EXITING fcnAddToBaseOfPayBucket ...SP = " theSchedulePeriodPay.schedulePeriodName  "... added = " fcnRoundUpAt2DecimalPlaces(theBaseValue) " to " theBucketCode " ...new base value = " fcnRoundUpAt2DecimalPlaces(theSchedulePeriodPay.getPayBucket(theBucketCode).baseValue) " ...new pay value = " fcnRoundUpAt2DecimalPlaces(theSchedulePeriodPay.getPayBucket(theBucketCode).payValue) "... pay rate = " theSchedulePeriodPay.getPayBucket(theBucketCode).payRate).}elsefcnShow("===>>> EXITING function fcnAddToBaseOfPayBucket without processing because event date " eventDate " is not within date range from " reportFilterStart " and " reportFilterEnd).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnAddTripPayBuckets](fcnAddTripPayBuckets.md)
- [fcnIsDateTimeWithinReportFilterRange](fcnIsDateTimeWithinReportFilterRange.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

## Llamado por

- [fcnCalculateExperiencePayBucket](fcnCalculateExperiencePayBucket.md)

## Historial de cambios

```
PL:10/14/2014: US18646 Initial development
```

