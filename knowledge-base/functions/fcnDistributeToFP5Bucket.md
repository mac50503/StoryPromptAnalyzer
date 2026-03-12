# fcnDistributeToFP5Bucket

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnDistributeToFP5Bucket`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | PayTrip | |
| theSchedulePeriodPay | SchedulePeriodPay | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |

## Lógica de negocio

```blaze
conusPayRate is a real initially fcnDetermineConusPerDiemPayRate(theTrip.beginDateTime);if (theTrip.startsInSchedulePeriod = (ignoring case) theSchedulePeriodPay.schedulePeriodName and theTrip.nonFlyCode =(ignoring case) ("CCP" or "HOTL" or "IN" or "STQ")) then{if (fcnIsDateTimeWithinReportFilterRange(theTrip.beginDateTime, reportFilterStart, reportFilterEnd)) then{theTrip.tripPay.conusPay += (Duration.newInstance(theTrip.beginDateTime,theTrip.endDateTime).standardMinutes)* conusPayRate/60.fcnShow("===>>> fcnDistributeToFP5Bucket     SP = " theSchedulePeriodPay.schedulePeriodName " ...trip = " theTrip.tripName " ...adding " (Duration.newInstance(theTrip.beginDateTime,theTrip.endDateTime).standardMinutes) * conusPayRate/60 "to conusPay ... conusPay value now = " theTrip.tripPay.conusPay).return (Duration.newInstance(theTrip.beginDateTime,theTrip.endDateTime).standardMinutes);}}// DE6646 - Addining special case for FP5 nonfly code, to ensure cumulative rounding off for all trip durations.else if (theTrip.startsInSchedulePeriod = (ignoring case) theSchedulePeriodPay.schedulePeriodName and theTrip.nonFlyCode =(ignoring case) ("FP5")) then{if (fcnIsDateTimeWithinReportFilterRange(theTrip.beginDateTime, reportFilterStart, reportFilterEnd)) then{theTrip.tripPay.conusPay += theTrip.timeAwayFromBase * conusPayRate/60.fcnShow("===>>> fcnDistributeToFP5Bucket     SP = " theSchedulePeriodPay.schedulePeriodName " ...trip = " theTrip.tripName " ...adding " theTrip.timeAwayFromBase * conusPayRate/60 "to conusPay ... conusPay value now = " theTrip.tripPay.conusPay).return  theTrip.timeAwayFromBase;}}else if (theTrip.startsInSchedulePeriod = (ignoring case) theSchedulePeriodPay.schedulePeriodName and theTrip.nonFlyCode =(ignoring case) ("AS1" or "ASB1" or "ASB2" or "ASB3" or "ASB4")) then{if (theTrip.associatedTrip = null) then{if (fcnIsDateTimeWithinReportFilterRange(theTrip.beginDateTime, reportFilterStart, reportFilterEnd)) then{theTrip.tripPay.conusPay +=  (Duration.newInstance(theTrip.beginDateTime,theTrip.endDateTime).standardMinutes)* conusPayRate/60.fcnShow("===>>> fcnDistributeToFP5Bucket    SP = " theSchedulePeriodPay.schedulePeriodName " ...trip = " theTrip.tripName " ...adding " (Duration.newInstance(theTrip.beginDateTime,theTrip.endDateTime).standardMinutes)* conusPayRate/60" to conusPay ... conusPay value now = " theTrip.tripPay.conusPay).return (Duration.newInstance(theTrip.beginDateTime,theTrip.endDateTime).standardMinutes);}}else{if (fcnIsDateTimeWithinReportFilterRange(theTrip.beginDateTime, reportFilterStart, reportFilterEnd)) then{theTrip.tripPay.conusPay += (Duration.newInstance(theTrip.beginDateTime,theTrip.associatedTrip.beginDateTime).standardMinutes)* conusPayRate/60.fcnShow("===>>> fcnDistributeToFP5Bucket    SP = " theSchedulePeriodPay.schedulePeriodName " ...trip = " theTrip.tripName " ...adding "fcnRoundUpAt2DecimalPlaces( (Duration.newInstance(theTrip.beginDateTime,theTrip.associatedTrip.beginDateTime).standardMinutes)* conusPayRate/60) " to conusPay ... conusPay value now = " theTrip.tripPay.conusPay).return (Duration.newInstance(theTrip.beginDateTime,theTrip.associatedTrip.beginDateTime).standardMinutes).}}}return 0.0.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDetermineConusPerDiemPayRate](fcnDetermineConusPerDiemPayRate.md)
- [fcnIsDateTimeWithinReportFilterRange](fcnIsDateTimeWithinReportFilterRange.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

## Llamado por

- [fcnDistributeToPerDiemBuckets](fcnDistributeToPerDiemBuckets.md)

