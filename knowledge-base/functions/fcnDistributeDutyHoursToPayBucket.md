# fcnDistributeDutyHoursToPayBucket

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnDistributeDutyHoursToPayBucket`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aSchedulePeriodPay | SchedulePeriodPay | |
| bucketCode | string | |
| amount | real | |
| eventDate | DateTime | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
dateFallsWithinRange is a boolean initially fcnIsDateTimeWithinReportFilterRange(eventDate, reportFilterStart, reportFilterEnd).if (dateFallsWithinRange is equal to true) then{pb is some PayBucket initially aSchedulePeriodPay.getPayBucket(bucketCode).if (pb <> null) then {pb.dutyHours = pb.dutyHours + amount;fcnShow("===>>> fcnDistributeDutyHoursToPayBucket ...SP = " aSchedulePeriodPay.schedulePeriodName "...bucket = " bucketCode " amount = " fcnRoundUpAt2DecimalPlaces(amount) ", dutyHours = " fcnRoundUpAt2DecimalPlaces(aSchedulePeriodPay.getPayBucket(bucketCode).dutyHours)", eventDate = " eventDate).}elsefcnShow("===>>> fcnDistributeDutyHoursToPayBucket ...SP = " aSchedulePeriodPay.schedulePeriodName "...bucket " bucketCode " was not found...").}elsefcnShow("===>>> EXITING fcnDistributeDutyHoursToPayBucket ......SP = " aSchedulePeriodPay.schedulePeriodName "...operation aborted due to event date not falling withing date range filter... event date = " eventDate " ...date range start = " reportFilterStart " ...date range end = " reportFilterEnd).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeWithinReportFilterRange](fcnIsDateTimeWithinReportFilterRange.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

