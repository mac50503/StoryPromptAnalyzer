# fcnBuildTripCalculatedValuesList

## Metadata
- **Tipo**: SRL Function
- **Retorna**: TripCalculations
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnBuildTripCalculatedValuesList`

## Propósito
5/1/2015 - DE6474 - Melissa S - Changed Duty Sum to use Report-Release instead of FAA Duty Duration

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | LegalityTrip | |
| theSchedulePeriodList | List<BaseSchedulePeriod> | |

## Lógica de negocio

```blaze
returnTripCalculations is a boolean initially false.theTripCalculations is some TripCalculations initially a TripCalculations.theTripCalculations.tripName = theTrip.tripName.// Build TripCalculations TAFBif(theTrip.dutyPeriodList <> null and theTrip.dutyPeriodList.size() > 0) then {// Initialize TAFB start/end based on the first and last duty periods in the triptafbStart is some DateTime initially theTrip.firstDutyPeriod.reportDateTime.tafbEnd is some DateTime initially theTrip.lastDutyPeriod.releaseDateTime.// Walk through the duty periods at the beginning to skip any duty period with all RS deadheadscounter is a integer initially 0.while (counter < theTrip.dutyPeriodList.size()) do {if (theTrip.dutyPeriodList.get(counter).allRSDeadheads = false) then {tafbStart = theTrip.dutyPeriodList.get(counter).reportDateTime.counter = theTrip.dutyPeriodList.size().}counter += 1.}// Walk through the duty periods at the end to skip any duty period with all RS deadheadscounter = theTrip.dutyPeriodList.size() - 1.while (counter >= 0) do {if (theTrip.dutyPeriodList.get(counter).allRSDeadheads = false) then {tafbEnd = theTrip.dutyPeriodList.get(counter).releaseDateTime.counter = 0.}counter -= 1.}timeAwayFromBase is an integer initially Duration.newInstance(tafbStart, tafbEnd).standardMinutes.if (theTrip.timeAwayFromBase <> timeAwayFromBase) then {theTripCalculations.timeAwayFromBase = timeAwayFromBase.returnTripCalculations = true.}}dutyPeriodDutyDurationSum is an integer initially 0.dutyPeriodBlockSum is an integer initially 0.dpIndex is an integer initially 0.if (theTrip.dutyPeriodList <> null) then {while(dpIndex < theTrip.dutyPeriodList.size()) do {// DE6474 - Changed Duty Sum to use Report-Release instead of FAA Duty DurationdutyPeriodDutyDurationSum += Duration.newInstance(theTrip.dutyPeriodList.get(dpIndex).reportDateTime, theTrip.dutyPeriodList.get(dpIndex).releaseDateTime).standardMinutes.dutyPeriodBlockSum += theTrip.dutyPeriodList.get(dpIndex).calculatedBlockTime.dpIndex = dpIndex + 1.}}// Build TripCalculations Duty Durationif (theTrip.dutyDuration is available and dutyPeriodDutyDurationSum is available and theTrip.dutyDuration <> dutyPeriodDutyDurationSum) then {theTripCalculations.dutyDuration = dutyPeriodDutyDurationSum.returnTripCalculations = true.}// Build TripCalculations Block Timeif (theTrip.blockTime is available and dutyPeriodBlockSum is available and theTrip.blockTime <> dutyPeriodBlockSum) then {theTripCalculations.blockTime = dutyPeriodBlockSum.returnTripCalculations = true.}// Find next SchedulePeriod's StartnextSchedulePeriodStart is some DateTime.schedulePeriodIndex is an integer initially 0.schedulePeriodFound is a boolean initially false.if (theSchedulePeriodList <> null) then {while (schedulePeriodFound = false and schedulePeriodIndex < theSchedulePeriodList.size()) do {if (theTrip.firstDutyPeriod <> null and (theTrip.firstDutyPeriod.reportDateTime.isBefore(theSchedulePeriodList.get(schedulePeriodIndex).schedulePeriodStart) = false) and (theTrip.firstDutyPeriod.reportDateTime.isAfter(theSchedulePeriodList.get(schedulePeriodIndex).schedulePeriodEnd) = false)) then {if (schedulePeriodIndex + 1 < theSchedulePeriodList.size()) then {nextSchedulePeriodStart = theSchedulePeriodList.get(schedulePeriodIndex + 1).schedulePeriodStart.schedulePeriodFound = true.}}schedulePeriodIndex +=1.}}// Build TripCalculations BlockTimeCarryOut based on the next SchedulePeriodtripCarryOutBlock is an integer initially 0.dpIndex = 0.if (theTrip.dutyPeriodList <> null and nextSchedulePeriodStart is known) then {while(dpIndex < theTrip.dutyPeriodList.size()) do {legIndex is an integer initially 0.theLegList is some List<LegalityLeg> initially theTrip.dutyPeriodList.get(dpIndex).legList.if (theLegList <> null) then {while(legIndex < theLegList.size()) do {leg is some LegalityLeg initially theLegList.get(legIndex).// If the leg is on or after the next schedule period start add to carry out blockif (leg.determineDepartureDateTime().equals(nextSchedulePeriodStart) or leg.determineDepartureDateTime().isAfter(nextSchedulePeriodStart)) then {tripCarryOutBlock = tripCarryOutBlock + fcnDetermineLegBlockTime(leg)..}legIndex = legIndex + 1.}}dpIndex = dpIndex + 1.}}// If we couldn't find the next schedule period for any reason, don't return anything since we couldn't calculate the valueif (nextSchedulePeriodStart is known and theTrip.blockTimeCarryOut <> tripCarryOutBlock) then {theTripCalculations.blockTimeCarryOut = tripCarryOutBlock.returnTripCalculations = true.}// Only return the intialized TripCalculations if one of the values has been set.if (returnTripCalculations = true) then {return theTripCalculations.} else {return null.}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDetermineLegBlockTime](fcnDetermineLegBlockTime.md)

## Historial de cambios

```
5/1/2015 - DE6474 - Melissa S - Changed Duty Sum to use Report-Release instead of FAA Duty Duration
8/12/2015 - DE7212 - Melissa S - Fix for TAFB calculation.  We weren't looking at the 1st duty period when looping through starting at the end of the duty period list
```

