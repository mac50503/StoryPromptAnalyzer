# fcnSetTripNonDeadheadBeginEndTime

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnSetTripNonDeadheadBeginEndTime`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
firstFlyingLeg is some PayLeg initially null.lastFlyingLeg is some PayLeg initially null.aPayTrip is some PayTrip initially null.aPayTrip = aTripPay.payTrip.if (aPayTrip.dutyPeriodList<>null and aPayTrip.dutyPeriodList.size()>0) then{//------------------------------Set Trip's nonDeadheadBeginDateTime----------------------------------if (aPayTrip.firstDutyPeriod.legList <> null and aPayTrip.firstDutyPeriod.legList.size()>0) then{firstFlyingLeg = aPayTrip.firstFlyingLeg.if (firstFlyingLeg <> null) then{aPayTrip.nonDeadheadBeginDateTime = firstFlyingLeg.payDutyPeriod.reportDateTime.}}                              //------------------------------Set Trip's nonDeadheadEndDateTime----------------------------------if (aPayTrip.lastDutyPeriod.legList <> null and aPayTrip.lastDutyPeriod.legList.size() > 0) then{lastFlyingLeg = fcnGetLastFlyingLeg(aPayTrip).//fcnShow("===>>> last flying leg for trip " aPayTrip.tripNameAndDate " is " lastFlyingLeg.sequenceNumber).thePayDutyPeriod is some PayDutyPeriod.limoOFZeroDurationFound is a boolean initially false.if(not fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(aPayTrip.beginDateTime, "IF_2025_LIMO_0_MINUTE_FIX_BLAZE_EFFECTIVE_DATETIME")) then {for each PayDutyPeriod in aPayTrip.dutyPeriodList as an array of PayDutyPeriod such that limoOFZeroDurationFound = false do {thePayDutyPeriod = it.for each PayLeg in thePayDutyPeriod.legList as an array of PayLeg such that limoOFZeroDurationFound = false doif (fcnDetermineLimoOfZeroDuration(it)) then {lastFlyingLeg = it.limoOFZeroDurationFound = true.}}}if (lastFlyingLeg <> null) then{// Use variable release times fron the global data cache, stored in the ayDutyPeriod.variableReleaseMinutes property----if (aPayTrip.lastDutyPeriod.lastLeg <> lastFlyingLeg) then {aPayTrip.nonDeadheadEndDateTime = lastFlyingLeg.determineBestArrivalDateTimeNoEstimated().if (limoOFZeroDurationFound = false) then //// ONLY ADD THE VARAIBLE RELEASE MINUTES IF THE LAST LEG IS NOT A LIMO OF ZERO DURATION….{              aPayTrip.nonDeadheadEndDateTime = aPayTrip.nonDeadheadEndDateTime.plusMinutes(lastFlyingLeg.payDutyPeriod.variableReleaseMinutes).fcnShow("===>>> setting nonDeadheadEndDateTime to lastFlyingLeg plus varable release time = " lastFlyingLeg.determineBestArrivalDateTimeNoEstimated() " + " lastFlyingLeg.payDutyPeriod.variableReleaseMinutes " = " aPayTrip.nonDeadheadEndDateTime).}else{              fcnShow("===>>> setting nonDeadheadEndDateTime to LIMO leg arrival time of = " aPayTrip.nonDeadheadEndDateTime). }}else {aPayTrip.nonDeadheadEndDateTime = lastFlyingLeg.payDutyPeriod.releaseDateTime.fcnShow("===>>> setting nonDeadheadEndDateTime to lastFlyingLeg.payDutyPeriod.releaseDateTime = " aPayTrip.nonDeadheadEndDateTime).}}}}if (aPayTrip.payTripInflight <> null and aPayTrip.payTripInflight.perdiemTripStartDateTime <> null) then{fcnShow("===>>> overloading nonDeadheadBeginDateTime from " aPayTrip.nonDeadheadBeginDateTime " to passed in value for perdiemTripBeginDateTime = " aPayTrip.payTripInflight.perdiemTripStartDateTime).aPayTrip.nonDeadheadBeginDateTime = aPayTrip.payTripInflight.perdiemTripStartDateTime.}if (aPayTrip.payTripInflight <> null and aPayTrip.payTripInflight.perdiemTripEndDateTime <> null) then{fcnShow("===>>> overloading nonDeadheadEndDateTime from " aPayTrip.nonDeadheadEndDateTime " to passed in value for perdiemTripEndDateTime = " aPayTrip.payTripInflight.perdiemTripEndDateTime).aPayTrip.nonDeadheadEndDateTime = aPayTrip.payTripInflight.perdiemTripEndDateTime.}perdiemTripStartDateTime is some DateTime initially aPayTrip.nonDeadheadBeginDateTime;perdiemTripEndDateTime is some DateTime initially aPayTrip.nonDeadheadEndDateTime;if (perdiemTripStartDateTime <> null and perdiemTripEndDateTime <> null) then {aTripPay.perdiemTimeAwayFromBase = Duration.newInstance(perdiemTripStartDateTime, perdiemTripEndDateTime).standardMinutes.fcnShow("===>>> trip = " aTripPay.tripNameAndDate " ...setting perdiemTimeAwayFromBase to minutes from perdiemTripStartDateTime to perdiemTripEndDateTime"). fcnShow("===>>> = " perdiemTripStartDateTime " to " perdiemTripEndDateTime " = " aTripPay.perdiemTimeAwayFromBase " minutes"). }
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDetermineLimoOfZeroDuration](fcnDetermineLimoOfZeroDuration.md)
- [fcnGetLastFlyingLeg](fcnGetLastFlyingLeg.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- `fcnShow()`

## Llamado por

- [fcnSetTripNonDeadheadBeginEndTimes](fcnSetTripNonDeadheadBeginEndTimes.md)

