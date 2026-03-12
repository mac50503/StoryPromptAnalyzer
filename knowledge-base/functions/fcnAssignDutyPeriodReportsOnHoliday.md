# fcnAssignDutyPeriodReportsOnHoliday

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnAssignDutyPeriodReportsOnHoliday`

## Propósito
US18085 - Melissa S - 7/29/2014 - New function that loops through all of the PayTrips and PayDutyPeriods and sets the reportsOnHoliday field

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayTrip | PayTrip | |
| theSwaHolidayList | List<SwaHoliday> | |

## Lógica de negocio

```blaze
fcnShow("===>>> ENTERING function fcnAssignDutyPeriodReportsOnHoliday with PayTrip and SWAHoliday List ").if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(thePayTrip.beginDateTime, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").previousDP is some PayDutyPeriod initially a PayDutyPeriod.if (thePayTrip.dutyPeriodList is not equal to null and thePayTrip.dutyPeriodList.size() > 0) then {for each PayDutyPeriod in thePayTrip.dutyPeriodList as an array of PayDutyPeriod do {//APIC-1585 & 1586 Domicile Day conversionif(if2025NewDomicileDayPayEffectiveDateActiveFlag) then {// Function to convert non-transient fileds at DP level to domicile time zone.fcnConvertDutyPeriodToTripDomicileTimeZone(it, thePayTrip.tripDomicileTimeZone).// Function to convert non-transient fileds for DP first leg to domicile time zone.fcnConvertLegToTripDomicileTimeZone(it.firstLeg, thePayTrip.tripDomicileTimeZone).// Function to convert non-transient fileds for DP last leg to domicile time zone.if(it.firstLeg.equals(it.lastLeg) =false) then {fcnConvertLegToTripDomicileTimeZone(it.lastLeg, thePayTrip.tripDomicileTimeZone).}// APIC-1563if ((it is not equal to thePayTrip.firstDutyPeriod)    and (previousDP.reportsOnHoliday = false)    and (fcnReportsOnHoliday(it.reportDateTime.minusDays(1), theSwaHolidayList))) then{it.afterCompleteRestOnHoliday = true.}previousDP = it.}it.reportsOnHoliday = fcnReportsOnHoliday(it.reportDateTime, theSwaHolidayList).}}fcnShow("===>>> EXITING function fcnAssignDutyPeriodReportsOnHoliday ").
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnConvertDutyPeriodToTripDomicileTimeZone](fcnConvertDutyPeriodToTripDomicileTimeZone.md)
- [fcnConvertLegToTripDomicileTimeZone](fcnConvertLegToTripDomicileTimeZone.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- [fcnReportsOnHoliday](fcnReportsOnHoliday.md)
- `fcnShow()`

## Llamado por

- [fcnCreateCrewPayResponse](fcnCreateCrewPayResponse.md)
- [fcnCreateTripPayResponse](fcnCreateTripPayResponse.md)

## Historial de cambios

```
US18085 - Melissa S - 7/29/2014 - New function that loops through all of the PayTrips and PayDutyPeriods and sets the reportsOnHoliday field
CREW-4750 - 4/23/2018 - Refactored function so trip request can use as well
APIC-1586-07/01/2025-Santosh Kudumu-Domicile Day Changes
```

