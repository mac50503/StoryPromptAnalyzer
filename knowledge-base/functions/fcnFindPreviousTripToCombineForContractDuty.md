# fcnFindPreviousTripToCombineForContractDuty

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnFindPreviousTripToCombineForContractDuty`

## Propósito
12/30/2014 US19132 Mitesh P - This function loops back through the previous trips in order to determine the next previous trip or duty period where Rest For Duty is &gt;= 8 hours and

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripList | List<LegalityTrip> | |
| tripCounter | integer | |
| combineForDuty | CombineForDuty | |

## Lógica de negocio

```blaze
prevTripCounter is an integer initially tripCounter.previousTrip is some LegalityTrip.tempDutyStart is some DateTime.while (prevTripCounter >=0) do {previousTrip = theTripList.get(prevTripCounter).if (previousTrip.ghostedFlag = false) then {if (previousTrip.isNonFly = false and previousTrip.tripType<>(ignoring case)"R") then { // Previous Trip is a Flying trip// Previous duty period that we check for new duty start is the last duty period in the previous tripapply fcnFindPreviousDutyToCombineForContractDuty (theTripList, prevTripCounter, previousTrip.dutyPeriodList.size()-1, combineForDuty).if(combineForDuty.dutyStartDateTime is not unknown and combineForDuty.dutyStartDateTime is not null) then {combineForDuty.dutyLabels.add(previousTrip.assignmentLabel).prevTripCounter = 0.}} else if (previousTrip.isDutyNonFly = true and previousTrip.restForDuty >= 480) then {// Previous trip is a Duty NonFly and has 8 or more hours of rest for dutyif(fcnGetPreviousTripAdjustedForAirportStandby(theTripList, prevTripCounter) = previousTrip) then {combineForDuty.dutyStartDateTime = previousTrip.contDutyStartDateTime.combineForDuty.dutyLabels.add(previousTrip.assignmentLabel).prevTripCounter = 0.}}}prevTripCounter -=1. }
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnFindPreviousDutyToCombineForContractDuty](fcnFindPreviousDutyToCombineForContractDuty.md)
- [fcnGetPreviousTripAdjustedForAirportStandby](fcnGetPreviousTripAdjustedForAirportStandby.md)

## Llamado por

- [fcnDetermineCombinedDutyDurationForDutyPeriod](fcnDetermineCombinedDutyDurationForDutyPeriod.md)
- [fcnDetermineCombinedDutyDurationForTrip](fcnDetermineCombinedDutyDurationForTrip.md)
- [fcnFindPreviousDutyToCombineForContractDuty](fcnFindPreviousDutyToCombineForContractDuty.md)

## Historial de cambios

```
12/30/2014 US19132 Mitesh P - This function loops back through the previous trips in order to determine the next previous trip or duty period where Rest For Duty is &gt;= 8 hours and
returns the Contract Duty start date time for that trip or duty period.
1/28/2015 US19445 Mitesh P - Updated to use class CombineForDuty instead
05/12/2015 US20484 Corey Gu - Added previousTrip.ghostedFlag = false condition.
6/22/2015 - DE6890 - Melissa S - Updated to add the combined trips labels to combineForDuty when a combine is done for contract duty
9/25/2015 - DE7517 - Melissa S - Removed logic for REST nonfly - moved to use the REST value in the "rest for duty" logic instead
05/03/2016 - CSCH-2855 Jaime P - Updated to get previous trip adjusted for airport standby
```

