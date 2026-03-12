# fcnConvertLegToTripDomicileTimeZone

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnConvertLegToTripDomicileTimeZone`

## Propósito
6/20/25 - APIC-1584 -Santosh Kudumu: New function to convert non-transient fileds at Leg level to domicile time zone.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |
| aDomicileTimeZone | string | |

## Lógica de negocio

```blaze
fcnShow("===>>> ENTERING fcnConvertLegToTripDomicileTimeZone with Leg =>..." aPayLeg.sequenceNumber);if(aPayLeg <> null and aPayLeg <> unknown and aDomicileTimeZone <> null and aDomicileTimeZone <> unknown) then {if (aPayLeg.actualInDateTime <> null and aPayLeg.actualInDateTime <> unknown) then {aPayLeg.actualInDateTime = DateTimeUtilities.convertDateTimeToTimezone(aPayLeg.actualInDateTime, aDomicileTimeZone);}if (aPayLeg.actualOutDateTime <> null and aPayLeg.actualOutDateTime <> unknown) then {aPayLeg.actualOutDateTime = DateTimeUtilities.convertDateTimeToTimezone(aPayLeg.actualOutDateTime, aDomicileTimeZone);}if (aPayLeg.estimatedInDateTime <> null and aPayLeg.estimatedInDateTime <> unknown) then {aPayLeg.estimatedInDateTime = DateTimeUtilities.convertDateTimeToTimezone(aPayLeg.estimatedInDateTime, aDomicileTimeZone);}if (aPayLeg.offgroundDateTime <> null and aPayLeg.offgroundDateTime <> unknown) then {aPayLeg.offgroundDateTime = DateTimeUtilities.convertDateTimeToTimezone(aPayLeg.offgroundDateTime, aDomicileTimeZone);}if (aPayLeg.ongroundDateTime <> null and aPayLeg.ongroundDateTime <> unknown) then {aPayLeg.ongroundDateTime = DateTimeUtilities.convertDateTimeToTimezone(aPayLeg.ongroundDateTime, aDomicileTimeZone);}if (aPayLeg.scheduledArrivalDateTime <> null and aPayLeg.scheduledArrivalDateTime <> unknown) then {aPayLeg.scheduledArrivalDateTime = DateTimeUtilities.convertDateTimeToTimezone(aPayLeg.scheduledArrivalDateTime, aDomicileTimeZone);}if (aPayLeg.scheduledDepartureDateTime <> null and aPayLeg.scheduledDepartureDateTime <> unknown) then {aPayLeg.scheduledDepartureDateTime = DateTimeUtilities.convertDateTimeToTimezone(aPayLeg.scheduledDepartureDateTime, aDomicileTimeZone);}}fcnShow("===>>> EXITING fcnConvertLegToTripDomicileTimeZone...");
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Llamado por

- [fcnAssignDutyPeriodReportsOnHoliday](fcnAssignDutyPeriodReportsOnHoliday.md)

## Historial de cambios

```
6/20/25 - APIC-1584 -Santosh Kudumu: New function to convert non-transient fileds at Leg level to domicile time zone.
```

