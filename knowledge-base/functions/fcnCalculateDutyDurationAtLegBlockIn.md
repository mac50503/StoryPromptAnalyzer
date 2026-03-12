# fcnCalculateDutyDurationAtLegBlockIn

## Metadata
- **Tipo**: SRL Function
- **Retorna**: duration
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateDutyDurationAtLegBlockIn`

## Propósito
US18932 11/18/2014 Mitesh P: This function is used to determine a duty period’s duration up to time of the block in for the current leg.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayLeg | PayLeg | |
| thePayDutyPeriod | PayDutyPeriod | |
| isCharter | boolean | |

## Lógica de negocio

```blaze
retVal is a duration.legBlockInToDutyReleaseMins is an integer initially 0.reportDateTime is some DateTime initially a DateTime.releaseDateTime is some DateTime initially a DateTime.// For a Charter trip we want to use the earlier of Original Scheduled Report or Actual Report if Original is not null.// Else we want to use the earlier of Scheduled Report or Actual Report.if (isCharter = true and thePayDutyPeriod.payDutyPeriodInflight.originalScheduledReportDateTime <> null andthePayDutyPeriod.payDutyPeriodInflight.originalScheduledReportDateTime.isBefore(thePayDutyPeriod.reportDateTime)) thenreportDateTime = thePayDutyPeriod.payDutyPeriodInflight.originalScheduledReportDateTime.else if (isCharter = true andthePayDutyPeriod.scheduledReportDateTime.isBefore( thePayDutyPeriod.reportDateTime)) thenreportDateTime = thePayDutyPeriod.scheduledReportDateTime.else if isCharter thenreportDateTime = thePayDutyPeriod.reportDateTime.else {reportDateTime = thePayDutyPeriod.reportDateTime.if (thePayDutyPeriod.payTrip.firstDutyPeriod = thePayDutyPeriod and //// THIS DP IS THE FIRST DP IN THE TRIP    thePayLeg <> null and     thePayDutyPeriod.firstLeg = thePayLeg and    thePayLeg.isDeadhead = true and    thePayLeg.legWorkCodeList.contains("RS")) then {reportDateTime = thePayLeg.scheduledDepartureDateTime.minusMinutes(thePayDutyPeriod.variableReportMinutes).fcnShow("===>>> fcnCalculateDutyDurationAtLegBlockIn trip " thePayDutyPeriod.payTrip.tripNameAndDate " ...DP " thePayDutyPeriod.sequenceNumber " start time of duty duration = first leg skd dep of " thePayLeg.scheduledDepartureDateTime " - variable report minutes of " thePayDutyPeriod.variableReportMinutes " = " reportDateTime).}}if (thePayDutyPeriod.releaseDateTime.isAfter(thePayDutyPeriod.scheduledReleaseDateTime)) then releaseDateTime = thePayDutyPeriod.releaseDateTime.else releaseDateTime = thePayDutyPeriod.scheduledReleaseDateTime.lastLeg is some PayLeg initially thePayDutyPeriod.lastLeg.lastLegBestArr is some DateTime initially lastLeg.determineBestArrivalDateTimeNoEstimated().legBestArr is some DateTime initially thePayLeg.determineBestArrivalDateTimeNoEstimated().fcnShow("===>>> Before adjustment lastLegBestArr " lastLegBestArr ", releaseDateTime " releaseDateTime ", legBestArr" legBestArr).// CREWT-890 - bug fix for DH RS legs, if leg is past release time adjust release time to leg arrival + 30 minutes.if ((lastLegBestArr.equals(releaseDateTime) or lastLegBestArr.isAfter(releaseDateTime)) and  lastLeg.isDeadhead = true and lastLeg.legWorkCodeList.contains("RS")) then {releaseDateTime = lastLegBestArr.plusMinutes(30).}fcnShow("===>>> After adjustment lastLegBestArr " lastLegBestArr ", releaseDateTime " releaseDateTime ", legBestArr" legBestArr). legBlockInToDutyReleaseMins = fcnGetTimeDiffInMinutes(legBestArr, releaseDateTime).combinedDurationMinutes is an integer initially 0.if (isCharter) then combinedDurationMinutes = Duration.newInstance(reportDateTime, releaseDateTime).standardMinuteselsecombinedDurationMinutes = DateTimeUtilities.getMinutesFromHourColonMinuteString(thePayDutyPeriod.dutyPeriodPay.dutyAmount).fcnShow("===>>> leg " thePayLeg.sequenceNumber " legBlockInToDutyReleaseMins = " legBlockInToDutyReleaseMins). fcnShow("===>>> DP " thePayDutyPeriod.sequenceNumber " duty duration = " thePayDutyPeriod.dutyPeriodPay.dutyAmount " ...combinedDurationMinutes = " combinedDurationMinutes). legBlockInMinutes is a integer initially combinedDurationMinutes - legBlockInToDutyReleaseMins.fcnShow("===>>> leg " thePayLeg.sequenceNumber " legBlockInMinutes = " legBlockInMinutes " leg block in duration = " DateTimeUtilities.getHoursAndMinutesStringFromMinutes(legBlockInMinutes)). fcnShow("===>>> in fcnCalculateDutyDurationAtLegBlockIn ...duty amount = " thePayDutyPeriod.dutyPeriodPay.dutyAmount " ...combined duration = " DateTimeUtilities.getHoursAndMinutesStringFromMinutes(combinedDurationMinutes) " leg block in duration = " DateTimeUtilities.getHoursAndMinutesStringFromMinutes(legBlockInMinutes)) .retVal = (legBlockInMinutes) minutes as a duration.fcnShow("===>>> EXITING fcnCalculateDutyDurationAtLegBlockIn ...trip = " thePayDutyPeriod.payTrip.tripNameAndDate " ...DP = " thePayDutyPeriod.sequenceNumber " ...leg = " thePayLeg.sequenceNumber " ...legBlockInMinutes = " legBlockInMinutes " ...retuning " retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)
- `fcnShow()`

## Historial de cambios

```
US18932 11/18/2014 Mitesh P: This function is used to determine a duty period’s duration up to time of the block in for the current leg.
DE5695 06 Jan 2015 Tim A. - TUX always uses duty report to last leg block in time...
DE5723 24 Mar 2015 Tim A. - added combined duration logic
Ben Lang 07/30/2015 - Added code to use original schedule times for charters
8/7/2015 - DE7193 - Melissa S - Removed comparison for release - all types should use the actual release, changed combinedDurationMinutes for charters to be calculated from original report
9/25/2015 - DE7516 - Melissa S - Fix for Report for Charter legs - Shouldn't be adjusted for variable times, variable time calculation was wrong.
```

