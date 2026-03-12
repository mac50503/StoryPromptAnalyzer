# fcnCalculate16HrsDutyDurationEDD

## Metadata
- **Tipo**: SRL Function
- **Retorna**: duration
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculate16HrsDutyDurationEDD`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayDutyPeriod | PayDutyPeriod | |
| isCharter | boolean | |

## Lógica de negocio

```blaze
retVal is a duration.combinedDurationMinutes is an integer initially 0.combinedDurationHours is a integer initially 0.nonCombinedDurationMinutes is a integer initially 0.nonCombinedDurationHours is a integer  initially 0.reportDateTime is some DateTime initially a DateTime.releaseDateTime is some DateTime initially a DateTime.// For a Charter trip we want to use the earlier of Original Scheduled Report or Actual Report if Original is not null.// Else we want to use the earlier of Scheduled Report or Actual Report.if (isCharter = true and thePayDutyPeriod.payDutyPeriodInflight.originalScheduledReportDateTime <> null andthePayDutyPeriod.payDutyPeriodInflight.originalScheduledReportDateTime.isBefore(thePayDutyPeriod.reportDateTime)) thenreportDateTime = thePayDutyPeriod.payDutyPeriodInflight.originalScheduledReportDateTime.else if (isCharter = true andthePayDutyPeriod.scheduledReportDateTime.isBefore( thePayDutyPeriod.reportDateTime)) thenreportDateTime = thePayDutyPeriod.scheduledReportDateTime.else if isCharter thenreportDateTime = thePayDutyPeriod.reportDateTime.else {reportDateTime = thePayDutyPeriod.reportDateTime.if (thePayDutyPeriod.payTrip.firstDutyPeriod = thePayDutyPeriod and //// THIS DP IS THE FIRST DP IN THE TRIP    thePayDutyPeriod.firstLeg <> null and     thePayDutyPeriod.firstLeg.isDeadhead = true and    thePayDutyPeriod.firstLeg.legWorkCodeList.contains("RS")) then{reportDateTime = thePayDutyPeriod.firstLeg.scheduledDepartureDateTime.minusMinutes(thePayDutyPeriod.variableReportMinutes).fcnShow("===>>> trip " thePayDutyPeriod.payTrip.tripNameAndDate " ...DP " thePayDutyPeriod.sequenceNumber " start time of duty duration = first leg skd dep of " thePayDutyPeriod.firstLeg.scheduledDepartureDateTime " - variable report minutes of " thePayDutyPeriod.variableReportMinutes " = " reportDateTime).}}// For all trips, use Actual ReleasereleaseDateTime = thePayDutyPeriod.releaseDateTime.lastNonRSLeg is some PayLeg initially thePayDutyPeriod.lastLeg.if(lastNonRSLeg is null or (lastNonRSLeg.legWorkCodeList <> null and lastNonRSLeg.legWorkCodeList.contains("RS") = true)) then {lastNonRSLeg =  fcnGetLastNonRSLegInDuty(thePayDutyPeriod).}if (thePayDutyPeriod.payTrip.lastDutyPeriod = thePayDutyPeriod) then {combinedDurationMinutes = DateTimeUtilities.getMinutesFromHourColonMinuteString(thePayDutyPeriod.dutyPeriodPay.dutyAmount).combinedDurationHours = math().truncate(combinedDurationMinutes / 60).nonCombinedDurationMinutes = Duration.newInstance(reportDateTime, releaseDateTime).standardMinutes.nonCombinedDurationHours = Duration.newInstance(reportDateTime, releaseDateTime).standardHours.} else {combinedDurationMinutes = DateTimeUtilities.getMinutesFromHourColonMinuteString(thePayDutyPeriod.dutyPeriodPay.dutyAmount).combinedDurationHours = math().truncate(combinedDurationMinutes / 60).if(lastNonRSLeg <> null) then {nonCombinedDurationMinutes = Duration.newInstance(reportDateTime,lastNonRSLeg.determineBestArrivalDateTimeNoEstimated()).standardMinutes.nonCombinedDurationHours = Duration.newInstance(reportDateTime, lastNonRSLeg.determineBestArrivalDateTimeNoEstimated()).standardHours.}}combinedHoursMinutesString is a string initially DateTimeUtilities.getHoursAndMinutesStringFromMinutes(combinedDurationMinutes).nonCombinedHoursMinutesString is a string initially DateTimeUtilities.getHoursAndMinutesStringFromMinutes(nonCombinedDurationMinutes).if(lastNonRSLeg <> null) then {fcnShow("===>>> in fcnCalculateActualDutyDuration  ... dutyAmount = " thePayDutyPeriod.dutyPeriodPay.dutyAmount " ...report = " reportDateTime " ...release = " releaseDateTime " ...last leg best arr = " lastNonRSLeg.determineBestArrivalDateTimeNoEstimated()).}fcnShow("===>>> in fcnCalculateActualDutyDuration for DP " thePayDutyPeriod.sequenceNumber ", COMPARING combined hours:minutes of " combinedHoursMinutesString " to non-combined hours:minutes of " nonCombinedHoursMinutesString).if (combinedDurationMinutes > nonCombinedDurationMinutes) then {fcnShow("===>>> combined duration "  combinedHoursMinutesString " is greater than non-combined duration " nonCombinedHoursMinutesString " by " combinedDurationMinutes - nonCombinedDurationMinutes " minutes so returning combined duration").retVal = (combinedDurationMinutes) minutes as a duration.} else if (thePayDutyPeriod.payTrip.lastDutyPeriod = thePayDutyPeriod) thenretVal = (Duration.newInstance(reportDateTime, releaseDateTime).standardMinutes " minutes") as a duration.else  {if(lastNonRSLeg <> null) then {retVal =  (Duration.newInstance(reportDateTime, lastNonRSLeg.determineBestArrivalDateTimeNoEstimated()).standardMinutes " minutes") as a duration.}}fcnShow("===>>> in fcnCalculateActualDutyDuration for DP " thePayDutyPeriod.sequenceNumber " returning actual duty duration of " retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnCalculateActualDutyDuration](fcnCalculateActualDutyDuration.md)
- [fcnGetLastNonRSLegInDuty](fcnGetLastNonRSLegInDuty.md)
- `fcnShow()`

