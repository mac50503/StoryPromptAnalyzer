# fcnCalculateThrAndAdgAndDhr

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateThrAndAdgAndDhr`

## Propósito
7/24/2015 - MS - Replaced fcnTripHasRonDuty with fcnTripContainsRON. (We had 2 identical functions in place.)

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
dpIndex is an integer initially 0.if (aTripPay <> null and aTripPay.tripPayInflight <> null) then{fcnShow("===>>> ENTERING fcnCalculateThrAndAdgAndDhr for trip " aTripPay.tripNameAndDate " ... duty period count = " aTripPay.dutyPeriodPayList.size()).aPayTrip is some PayTrip initially aTripPay.payTrip.aPayDutyPeriod is some PayDutyPeriod initially null.aPayLeg is some PayLeg initially null.tripHasRonDuty is a boolean initially false.if (aPayTrip <> null) then {   tripHasRonDuty = aPayTrip.containsRON.}//// FIRST RE-CALCULATE TIME AWAY FROM BASE...if (aPayTrip <> null and      aPayTrip.firstDutyPeriod <> null and        aPayTrip.firstDutyPeriod.scheduledReportDateTime <> null and        aPayTrip.lastDutyPeriod is known and        aPayTrip.lastDutyPeriod.scheduledReleaseDateTime <> null) then{fcnShow("===>>> trip " aTripPay.tripNameAndDate " ...original passed in TimeAwayFromBase = " aPayTrip.timeAwayFromBase " minutes ...in hours:minutes =  " DateTimeUtilities.getHoursAndMinutesString(aTripPay.timeAwayFromBase)).fcnShow("===>>> trip " aTripPay.tripNameAndDate " ...first DP skd report =  " DateTimeUtilities.getShortDateTimeString(aPayTrip.firstDutyPeriod.scheduledReportDateTime) " ... last DP skd release = " DateTimeUtilities.getShortDateTimeString(aPayTrip.lastDutyPeriod.scheduledReleaseDateTime)).aPayTrip.timeAwayFromBase = fcnGetTimeDiffInMinutes(aPayTrip.firstDutyPeriod.scheduledReportDateTime, aPayTrip.lastDutyPeriod.scheduledReleaseDateTime).aTripPay.timeAwayFromBase = aPayTrip.timeAwayFromBase.fcnShow("===>>> trip " aTripPay.tripNameAndDate " ...diff in minutes =  " fcnGetTimeDiffInMinutes(aPayTrip.firstDutyPeriod.scheduledReportDateTime, aPayTrip.lastDutyPeriod.scheduledReleaseDateTime) " ...diff in hours:minutes =  " DateTimeUtilities.getHoursAndMinutesString(aTripPay.timeAwayFromBase)).fcnShow("===>>> trip " aTripPay.tripNameAndDate " ... new timeAwayFromBase = " aTripPay.timeAwayFromBase " ...skd report = " DateTimeUtilities.getShortDateTimeString(aPayTrip.firstDutyPeriod.scheduledReportDateTime) " ...skd release = " DateTimeUtilities.getShortDateTimeString(aPayTrip.lastDutyPeriod.scheduledReleaseDateTime)). }//// NOW ADJUST TIME AWAY FROM BASE...if (aPayTrip <> null and    aPayTrip.timeAwayFromBase <> unknown and        aPayTrip.lastDutyPeriod <> null and        aPayTrip.lastDutyPeriod.lastLeg <> null and        aPayTrip.lastDutyPeriod.lastLeg.actualInDateTime <> null and        aPayTrip.lastDutyPeriod.lastLeg.scheduledArrivalDateTime <> null and        aPayTrip.lastDutyPeriod.lastLeg.actualInDateTime.isAfter(aPayTrip.lastDutyPeriod.lastLeg.scheduledArrivalDateTime)) then{aTripPay.timeAwayFromBase = aPayTrip.timeAwayFromBase + fcnGetTimeDiffInMinutes(aPayTrip.lastDutyPeriod.lastLeg.scheduledArrivalDateTime, aPayTrip.lastDutyPeriod.lastLeg.actualInDateTime).fcnShow("===>>> last leg = " aPayTrip.lastDutyPeriod.lastLeg.sequenceNumber  " ...skd arr time = " DateTimeUtilities.getShortDateTimeString(aPayTrip.lastDutyPeriod.lastLeg.scheduledArrivalDateTime)" ...actual arrival time = " DateTimeUtilities.getShortDateTimeString(aPayTrip.lastDutyPeriod.lastLeg.actualInDateTime) " ...diff in minutes = " fcnGetTimeDiffInMinutes(aPayTrip.lastDutyPeriod.lastLeg.scheduledArrivalDateTime, aPayTrip.lastDutyPeriod.lastLeg.actualInDateTime) " ...diff in hours:minutes =  " DateTimeUtilities.getHoursAndMinutesString(fcnGetTimeDiffInMinutes(aPayTrip.lastDutyPeriod.lastLeg.scheduledArrivalDateTime, aPayTrip.lastDutyPeriod.lastLeg.actualInDateTime))).}//// NOW CALCULATE THR...if (aTripPay.timeAwayFromBase <> unknown and aTripPay.timeAwayFromBase > 0 and tripHasRonDuty = false) then {aTripPay.tripPayInflight.thrValue = fcnRoundUpAt2DecimalPlaces(aTripPay.timeAwayFromBase / (3 * 60)).aTripPay.tripHourRatio =  aTripPay.tripPayInflight.thrValue.fcnShow("===>>> trip " aTripPay.tripNameAndDate " ...THR = timeAwayFromBase passed in = " aTripPay.timeAwayFromBase " / (3 * 60) = "   aTripPay.tripPayInflight.thrValue "...tripHasRonDuty = " tripHasRonDuty).}//// NOW CALCULATE ADG AND DHR...if (aPayTrip <> null and aPayTrip.dutyPeriodList <> null and aPayTrip.dutyPeriodList.size() > 0) then {if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(aPayTrip.beginDateTime,"IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME");while (dpIndex < aPayTrip.dutyPeriodList.size()) do {aPayDutyPeriod = aPayTrip.dutyPeriodList.get(dpIndex).//// ADG CALCULATION...if((not if2025NewDomicileDayPayEffectiveDateActiveFlag or fcnIsCharter(aPayTrip) = true or aPayTrip.dutyPeriodList.size() = 1)and (aPayDutyPeriod.dutyType = null or (aPayDutyPeriod.dutyType <>  null and aPayDutyPeriod.dutyType = (ignoring case) "RON" = false))) then {aTripPay.tripPayInflight.adgValue += 6.5.fcnShow("===>>> trip " aTripPay.tripNameAndDate "'s non-RON DP " aPayDutyPeriod.sequenceNumber " contributes 6.5 to ADG ... value now = " aTripPay.tripPayInflight.adgValue).}//// DHR CALCULATION...fcnCalculateDHR(aPayDutyPeriod).fcnShow("===>>> trip " aTripPay.tripNameAndDate " ...DP = " aPayDutyPeriod.dutyPeriodPay.sequenceNumber " ...DHR (after rounding) = " aPayDutyPeriod.dutyPeriodPay.dutyHourRatio).dpIndex += 1.}//// ADG CALCULATION- Domicile Day-Multi-DP excluding chartersif ((aPayDutyPeriod.dutyType = null or (aPayDutyPeriod.dutyType <>  null and aPayDutyPeriod.dutyType = (ignoring case) "RON" = false))and (if2025NewDomicileDayPayEffectiveDateActiveFlag and aPayTrip.dutyPeriodList.size() > 1 and fcnIsCharter(aPayTrip) = false)) then {if(aPayTrip.numberOfDomicileDays is known)then {aTripPay.tripPayInflight.adgValue = 6.5 * aPayTrip.numberOfDomicileDays;fcnShow("===>>> trip " aTripPay.tripNameAndDate "'s non-RON DP " aPayDutyPeriod.sequenceNumber " contributes 6.5 * # of domicile days to ADG ..." aPayTrip.numberOfDomicileDays "value now = " aTripPay.tripPayInflight.adgValue).}}}fcnShow("===>>> EXITING fcnCalculateThrAndAdgAndDhr for trip " aTripPay.tripNameAndDate " ... THR = " aTripPay.tripPayInflight.thrValue " ...ADG = " aTripPay.tripPayInflight.adgValue).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnCalculateDHR](fcnCalculateDHR.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)
- [fcnIsCharter](fcnIsCharter.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

## Historial de cambios

```
7/24/2015 - MS - Replaced fcnTripHasRonDuty with fcnTripContainsRON. (We had 2 identical functions in place.)
10/6/2015 - DE7555 - Melissa S - Moved DHR calculation to a function to keep it logically separate from other calculations
4/5/2016 - CSCH-2723 - Melissa S - Refactored for performance to use while loops and indexes instead of casting to Blaze arrays
APIC-1501 -07/15/2025 - Santosh Kudumu - Updated adg calculation based on no of domicile days
```

