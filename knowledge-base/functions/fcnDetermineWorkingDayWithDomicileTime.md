# fcnDetermineWorkingDayWithDomicileTime

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnDetermineWorkingDayWithDomicileTime`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | LegalityTrip | |

## Lógica de negocio

```blaze
// Check to see if the trip or any of its duty periods should count towards working daysdutyIndex is an integer initially 0.dutyPeriod is some LegalityDutyPeriod.lastReserveBlockLabel is a string initially "".aAssociatedReserveBlockDutyPeriod is some LegalityDutyPeriod.if (workingDaysBlockArray <> null and theTrip.isNonFly = false) then {// All days in O and K label trips will count towards working daysif (theTrip.assignmentLabel = (ignoring case) ("O" or "K")) then {//APIC-1589 minimum Days Off -scheduleaDomicileBeginDateTime is some DateTime.aDomicileBeginDateTime = DateTimeUtilities.convertDateTimeToTimezone(theTrip.beginDateTime, theTrip.tripDomicileTimeZone).aDomicileEndDateTime is some DateTime.aDomicileEndDateTime = DateTimeUtilities.convertDateTimeToTimezone(theTrip.endDateTime, theTrip.tripDomicileTimeZone).fcnAddToWorkingDaysBlockArray(aDomicileBeginDateTime, aDomicileEndDateTime, workingDaysBlockArray);}// R label trips only count as working days if under a K label Reserve Block.  Since K labels have already been counted, we only need to // check duty periods in an R label trip that extend past the end of the reserve block to see if any additional working days need to be addedif (theTrip.assignmentLabel = (ignoring case) ("R" or "S")) then {if (theTrip.dutyPeriodList <> null) then {dutyIndex = theTrip.dutyPeriodList.size() - 1.dutyPeriod = theTrip.dutyPeriodList.get(dutyIndex).// Check to see if the last duty period extends past the end of the reserve block//APIC-1589 check AssociatedReserveBlockDutyPeriod with domicile date timeif( theTrip.dutyPeriodList.get(dutyIndex).associatedReserveBlockDutyPeriod is not null) then {aDomicileDPReportDateTime is some DateTime.aDomicileDPReportDateTime = DateTimeUtilities.convertDateTimeToTimezone(dutyPeriod.reportDateTime, theTrip.tripDomicileTimeZone).aAssociatedReserveBlockDutyPeriod = null.if(fcnIsSameSwaDay(aDomicileDPReportDateTime, theTrip.dutyPeriodList.get(dutyIndex).associatedReserveBlockDutyPeriod.reportDateTime)) then {aAssociatedReserveBlockDutyPeriod=theTrip.dutyPeriodList.get(dutyIndex).associatedReserveBlockDutyPeriod.}}//APIC-1589 check missing AssociatedReserveBlockDutyPeriod with domicile date timeif (theTrip.dutyPeriodList.get(dutyIndex).associatedReserveBlockDutyPeriod = null ) then {aAssociatedReserveBlockDutyPeriod = null.aDomicileDPReportDateTime is some DateTime.aDomicileDPReportDateTime = DateTimeUtilities.convertDateTimeToTimezone(theTrip.dutyPeriodList.get(dutyIndex).reportDateTime, theTrip.tripDomicileTimeZone).for each LegalityDutyPeriod in theReserveBlockDutyPeriods as an array of LegalityDutyPeriod such that (fcnIsSameSwaDay(aDomicileDPReportDateTime, it.reportDateTime)) do {aAssociatedReserveBlockDutyPeriod = it.}}//APIC-1589 check aAssociatedReserveBlockDutyPeriod instead of associatedReserveBlockDutyPeriodif (aAssociatedReserveBlockDutyPeriod = null) then {// Find the label for the last associated reserve blockwhile (dutyIndex >=0) do {dutyPeriod = theTrip.dutyPeriodList.get(dutyIndex).//APIC-1589 check AssociatedReserveBlockDutyPeriod with domicile date timeif(dutyPeriod.associatedReserveBlockDutyPeriod is not null) then {aDomicileDPReportDateTime is some DateTime.aDomicileDPReportDateTime = DateTimeUtilities.convertDateTimeToTimezone(dutyPeriod.reportDateTime, theTrip.tripDomicileTimeZone).aAssociatedReserveBlockDutyPeriod = null.if(fcnIsSameSwaDay(aDomicileDPReportDateTime, dutyPeriod.associatedReserveBlockDutyPeriod.reportDateTime)) then {aAssociatedReserveBlockDutyPeriod=theTrip.dutyPeriodList.get(dutyIndex).associatedReserveBlockDutyPeriod.}}if (dutyPeriod.associatedReserveBlockDutyPeriod = null or aAssociatedReserveBlockDutyPeriod = null) then {// Keep looking until a duty period with an associated reserve block is founddutyIndex = dutyIndex - 1.} else {lastReserveBlockLabel = dutyPeriod.associatedReserveBlockDutyPeriod.legalityTrip.assignmentLabel.// Exit loop once a duty period is found with an associated reserve blockdutyIndex = -1.}}// If the last associated reserve block label is K, add every duty period in the R label trip that extends past the end of the reserve block to the working days listif (lastReserveBlockLabel = (ignoring case) ("K")) then {dutyIndex = theTrip.dutyPeriodList.size() - 1.while (dutyIndex >=0) do {dutyPeriod = theTrip.dutyPeriodList.get(dutyIndex).if (dutyPeriod.associatedReserveBlockDutyPeriod = null) then {//APIC-1589 minimum Days Off -scheduleaDomicileDPReportDateTime is some DateTime.aDomicileDPReportDateTime = DateTimeUtilities.convertDateTimeToTimezone(dutyPeriod.reportDateTime, theTrip.tripDomicileTimeZone).aDomicileDPReleaseDateTime is some DateTime.aDomicileDPReleaseDateTime = DateTimeUtilities.convertDateTimeToTimezone(dutyPeriod.releaseDateTime, theTrip.tripDomicileTimeZone).fcnAddToWorkingDaysBlockArray(aDomicileDPReportDateTime, aDomicileDPReleaseDateTime, workingDaysBlockArray);// Keep looking until a duty period with an associated reserve block is founddutyIndex = dutyIndex - 1.} else {// Exit loop once a duty period is found with an associated reserve blockdutyIndex = -1.}}}}}}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnAddToWorkingDaysBlockArray](fcnAddToWorkingDaysBlockArray.md)
- [fcnIsSameSwaDay](fcnIsSameSwaDay.md)

