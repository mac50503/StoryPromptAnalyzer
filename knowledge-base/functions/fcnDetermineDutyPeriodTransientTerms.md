# fcnDetermineDutyPeriodTransientTerms

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnDetermineDutyPeriodTransientTerms`

## Propósito
28 Nov '14 Akshay M - US19123 Initial code

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | LegalityDutyPeriod | |
| theTrip | LegalityTrip | |
| theGlobalDataCache | GlobalDataCache | |
| theLegBlockTimeList | List<LegBlockTime> | |

## Lógica de negocio

```blaze
totalLegs is an integer initially 0.theLeg is some LegalityLeg.legs is some List<LegalityLeg> initially theDutyPeriod.legList.rsLegCount is an integer initially 0.// Since for Legality variableReportMinutes is not use for any calculationsd, just keeping this code when the toggle is OFF, as if is ON, the table will no longer come to Blaze.if(not fcnIsConfigCollectionToggleON("IF_VARIABLE_REPORT_TIME_NEW_TABLE_INFO")) then {// Calculate Variable report Date timetheGlobalDataCache.calculateVariableReportTimes(theDutyPeriod).} // Calculate Variable release Date timetheGlobalDataCache.calculateVariableReleaseTimes(theDutyPeriod).// If a manual release date time has been sent , it should override the regular release date time so that the manual time will get used in all rulesif (theDutyPeriod.manualReleaseDateTime<>null) then {theDutyPeriod.releaseDateTime=theDutyPeriod.manualReleaseDateTime.}// Flying Trips:  Report to Release of Duty Period, unless there are DH's at the end (then Report to end of the last flying leg)if (theTrip.isNonFly = false and theTrip.tripType <>(ignoring case) "R") then {// FAA Duty Start will always be the Report DateTime (Unless Duty has all deadheads, then it will be cleared)theDutyPeriod.faaDutyStartDateTime = theDutyPeriod.reportDateTime.// If there is a manual release date time, that will override all other times and be used for FAA Duty with no adjustmentsif (theDutyPeriod.manualReleaseDateTime<>null) then {theDutyPeriod.faaDutyEndDateTime=theDutyPeriod.manualReleaseDateTime.theDutyPeriod.faaDutyDuration=fcnGetTimeDiffInMinutes(theDutyPeriod.faaDutyStartDateTime, theDutyPeriod.faaDutyEndDateTime).} else {// If the Duty ends with Deadhead legs, walk backwards to find the last leg that isn’t a // deadhead.  If all legs are deadheads, FAA duty will be 0, and FAA Report/Release will be // clearedif (theDutyPeriod.lastLeg.isDeadhead) then {totalLegs = theDutyPeriod.legList.size().while (totalLegs > 0) do {theLeg = legs.get(totalLegs - 1).if (theLeg.isDeadhead = false) then {theDutyPeriod.faaDutyEndDateTime = theLeg.determineArrivalDateTime().plusMinutes(theDutyPeriod.faaVariableReleaseMinutes).totalLegs = 1.}totalLegs = totalLegs - 1.}// DE6616 - LIMO at the end should be leg's block-in (NO variable relase added)} else if (theDutyPeriod.lastLeg.limoFlag = true) then {theDutyPeriod.faaDutyEndDateTime = theDutyPeriod.lastLeg.determineArrivalDateTime().// All other cases are block-in + variable release} else {theDutyPeriod.faaDutyEndDateTime = theDutyPeriod.lastLeg.determineArrivalDateTime().plusMinutes(theDutyPeriod.faaVariableReleaseMinutes).}// If no new FAA End DateTime has been found, all legs are deadheads.  Clear FAA Duty Valuesif (theDutyPeriod.faaDutyEndDateTime = null) then {theDutyPeriod.faaDutyStartDateTime = null.theDutyPeriod.faaDutyDuration = 0.} else { theDutyPeriod.faaDutyDuration = fcnGetTimeDiffInMinutes(theDutyPeriod.faaDutyStartDateTime, theDutyPeriod.faaDutyEndDateTime).}}// Contract Duty Calculations// Contract Duty Start will default to Duty Period Report DateTime.  Will only be overridden in the case of a Duty Period with all RS deadheadstheDutyPeriod.contDutyStartDateTime = theDutyPeriod.reportDateTime.// If there is a manual release date time , that will override all other times and be used for contract duty with no adjustmentsif (theDutyPeriod.manualReleaseDateTime<>null) then {theDutyPeriod.contDutyEndDateTime=theDutyPeriod.manualReleaseDateTime.theDutyPeriod.contDutyDuration=fcnGetTimeDiffInMinutes(theDutyPeriod.contDutyStartDateTime, theDutyPeriod.contDutyEndDateTime).} else {// Regardless of the Duty Period’s position on the Trip, if the last leg is a LIMO, use block-inif (theDutyPeriod.lastLeg.limoFlag = true) then {theDutyPeriod.contDutyEndDateTime = theDutyPeriod.lastLeg.determineArrivalDateTime();// If Duty Period ends with waived deadheads, use the last flying leg’s block-in + Contract Variable Release Time} else if (theDutyPeriod.lastLeg.legWorkCodeList <> null and theDutyPeriod.lastLeg.legWorkCodeList <> unknown and theDutyPeriod.lastLeg.legWorkCodeList.contains ("RS")) then {totalLegs = theDutyPeriod.legList.size().while (totalLegs > 0) do {theLeg = legs.get(totalLegs - 1).if (theLeg.legWorkCodeList = null or (theLeg.legWorkCodeList <> null and theLeg.legWorkCodeList.contains("RS") = false)) then {theDutyPeriod.contDutyEndDateTime = theLeg.determineArrivalDateTime().plusMinutes(theDutyPeriod.contVariableReleaseMinutes).totalLegs = 1.}totalLegs = totalLegs -1.}// US20466 - All other Duty Periods will use last leg’s block-in + Contract Variable Release Time } else {// APIC-1427 - use the Contractual Release Time update tableif (fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(theTrip.beginDateTime, "IF_2025_DUTY_DAY_DEF_BLAZE_EFFECTIVE_DATETIME")) then {if ( theDutyPeriod.contVariableReleaseMinutes > 0) then {theDutyPeriod.contDutyEndDateTime = theDutyPeriod.lastLeg.determineArrivalDateTime().plusMinutes(theDutyPeriod.contVariableReleaseMinutes).} else {theDutyPeriod.contDutyEndDateTime = theDutyPeriod.releaseDateTime;}} else {//theDutyPeriod.contDutyEndDateTime = theDutyPeriod.lastLeg.determineArrivalDateTime().theDutyPeriod.contDutyEndDateTime = theDutyPeriod.lastLeg.determineArrivalDateTime().plusMinutes(theDutyPeriod.contVariableReleaseMinutes).}}if (theDutyPeriod.contDutyEndDateTime <> null) then {// Calculate the Contract Duty DurationtheDutyPeriod.contDutyDuration = fcnGetTimeDiffInMinutes(theDutyPeriod.contDutyStartDateTime, theDutyPeriod.contDutyEndDateTime).} else {// If no new Contract End DateTime has been found, there is no Contract Duty.  Clear FAA Duty ValuestheDutyPeriod.contDutyStartDateTime = null.theDutyPeriod.contDutyDuration = 0.}}}// Loop through legs to calculate Leg's Block Time for returning calculated values, and to determine deadhead leg countdutyLegs is an integer initially theDutyPeriod.legList.size().deadheadLegCount is an integer initially 0.rsDeadheadLegCount is an integer initially 0.while (dutyLegs > 0) do {theLeg = legs.get(dutyLegs - 1).// Calculate leg's block timecalculatedLegBlockTime is an integer initially fcnDetermineLegBlockTime(theLeg).// Return leg's block time only if it changedif (theLegBlockTimeList <> null and theLeg.flightBlockTime <> calculatedLegBlockTime) then {theLegBlockTimeList.add(a LegBlockTime initially {it.sequenceNumber = theLeg.sequenceNumber, it.blockTime = calculatedLegBlockTime}).}// Calculate duty period's block time as sum of all legs.theDutyPeriod.calculatedBlockTime += calculatedLegBlockTime.// Add to deadhead count if legs is a deadheadif (theLeg.isDeadhead = true) then {deadheadLegCount += 1.}// DE6699if (theLeg.legWorkCodeList <> null and theLeg.legWorkCodeList <> unknown and theLeg.legWorkCodeList.contains ("RS")) then {rsDeadheadLegCount += 1.}//CSCH-1735 if(theLeg.legCrewPosition = null or theLeg.legCrewPosition = "") then {theLeg.legCrewPosition = theTrip.assignmentCrewPosition.}dutyLegs = dutyLegs - 1.}// Determine if all legs are deadheadsif (deadheadLegCount = theDutyPeriod.legList.size()) then {theDutyPeriod.allDeadheads = true.}// Determine if all legs are RS deadheadsif (rsDeadheadLegCount = theDutyPeriod.legList.size()) then {theDutyPeriod.allRSDeadheads = true.}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDetermineLegBlockTime](fcnDetermineLegBlockTime.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)
- [fcnIsConfigCollectionToggleON](fcnIsConfigCollectionToggleON.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- [ping](ping.md)

## Historial de cambios

```
28 Nov '14 Akshay M - US19123 Initial code
12/11/2014 Mitesh P - US19182 - variable release/report time
1.19.2015 Melissa S - US19407 - Fixed error in logic checking for legWorkCodeList (added null check)
12/12/2014 Mitesh P - US19194 - Added condition to handle all deadhead legs.
12/16/2014 Mitesh P - US19130 - Added logic for contract Duty period start end and duty duration
12.30.2014 Melissa S - Added check for a null or unknown leg work code list
03.11.2015 - DE6015 - Melissa S - Changed to calculate contract duty for charter trips
04/06/2015 - US20466 - Melissa S - Removed RON duty periods from working days array (Minimum Days Off Rule)
04/06/2015 - US20466 - Melissa S - Removed last DutyPeriod in trip logic for contract duty calculations.  Per the IF customers, last DutyPeriod in trip should also use last leg's block-in + variable release instead of Release
04/30/2015 - US20172 - Mitesh P - Store Reserve Block DPs
5/1/2015 - DE6474 - Melissa S - Changed to use last block-in + FAA variable release time for the default FAA duty instead of the value passed from CSS
5/1/2015 - US20752 - Melissa S - Changed to use block-in + FAA variable release time for duty periods that end in deadheads
5/5/2015 - DE6510/DE6520 - Melissa S - Setting allRSDeadheads property to be used for rest and duty calculations
5/14/2015 - DE6616 - Melissa S - Variable release should not be added to FAA duty for a LIMO leg - should end at block-in
05/22/2015 Corey Gu DE6699 - Replaced "theLeg.legWorkCodeList.contains ("RS"))" for "theDutyPeriod.lastLeg.legWorkCodeList.contains ("RS")) " to decide if to increment rsDeadheadLegCount.
```

