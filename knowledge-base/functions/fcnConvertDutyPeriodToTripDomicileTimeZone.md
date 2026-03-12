# fcnConvertDutyPeriodToTripDomicileTimeZone

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnConvertDutyPeriodToTripDomicileTimeZone`

## Propósito
6/20/25 - APIC-1584 -Santosh Kudumu: New function to convert non-transient fileds at Duty Period level to domicile time zone.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |
| aDomicileTimeZone | string | |

## Lógica de negocio

```blaze
fcnShow("===>>> ENTERING fcnConvertDutyPeriodToTripDomicileTimeZone with DP=>..." aPayDutyPeriod.sequenceNumber);if(aPayDutyPeriod <> null and aPayDutyPeriod <> unknown and aDomicileTimeZone <> null and aDomicileTimeZone <> unknown) then {if(aPayDutyPeriod.scheduledReportDateTime <> null and aPayDutyPeriod.scheduledReportDateTime <> null) then {aPayDutyPeriod.scheduledReportDateTime = DateTimeUtilities.convertDateTimeToTimezone(aPayDutyPeriod.scheduledReportDateTime,aDomicileTimeZone);}if(aPayDutyPeriod.scheduledReleaseDateTime <> null and aPayDutyPeriod.scheduledReleaseDateTime <> null) then {aPayDutyPeriod.scheduledReleaseDateTime = DateTimeUtilities.convertDateTimeToTimezone(aPayDutyPeriod.scheduledReleaseDateTime,aDomicileTimeZone);}if(aPayDutyPeriod.contactTime <> null and aPayDutyPeriod.contactTime <> null) then {aPayDutyPeriod.contactTime = DateTimeUtilities.convertDateTimeToTimezone(aPayDutyPeriod.contactTime,aDomicileTimeZone);}if(aPayDutyPeriod.manualReleaseDateTime <> null and aPayDutyPeriod.manualReleaseDateTime <> null) then {aPayDutyPeriod.manualReleaseDateTime = DateTimeUtilities.convertDateTimeToTimezone(aPayDutyPeriod.manualReleaseDateTime,aDomicileTimeZone);}if(aPayDutyPeriod.originalReleaseDateTime <> null and aPayDutyPeriod.originalReleaseDateTime <> null) then {aPayDutyPeriod.originalReleaseDateTime = DateTimeUtilities.convertDateTimeToTimezone(aPayDutyPeriod.originalReleaseDateTime,aDomicileTimeZone);}if(aPayDutyPeriod.releaseDateTime <> null and aPayDutyPeriod.releaseDateTime <> null) then {aPayDutyPeriod.releaseDateTime = DateTimeUtilities.convertDateTimeToTimezone(aPayDutyPeriod.releaseDateTime,aDomicileTimeZone);}if(aPayDutyPeriod.reportDateTime <> null and aPayDutyPeriod.reportDateTime <> null) then {aPayDutyPeriod.reportDateTime = DateTimeUtilities.convertDateTimeToTimezone(aPayDutyPeriod.reportDateTime,aDomicileTimeZone);}}fcnShow("===>>> EXITING fcnConvertDutyPeriodToTripDomicileTimeZone...");
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Llamado por

- [fcnAssignDutyPeriodReportsOnHoliday](fcnAssignDutyPeriodReportsOnHoliday.md)

## Historial de cambios

```
6/20/25 - APIC-1584 -Santosh Kudumu: New function to convert non-transient fileds at Duty Period level to domicile time zone.
```

