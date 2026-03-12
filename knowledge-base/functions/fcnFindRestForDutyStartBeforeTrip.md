# fcnFindRestForDutyStartBeforeTrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnFindRestForDutyStartBeforeTrip`

## Propósito
12/18/2014 US19195 Mitesh P  - This function will loop back through the previous trips in order to determine where Rest For Duty should start before a trip, or before the first duty period in a trip

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripList | List<LegalityTrip> | |
| tripCounter | integer | |

## Lógica de negocio

```blaze
prevTripCounter is an integer initially tripCounter.previousTrip is some LegalityTrip.tempRestStart is some DateTime.while prevTripCounter >=0 do {previousTrip = theTripList.get(prevTripCounter).if (previousTrip.ghostedFlag = false) then {if (previousTrip.isNonFly = false) then {// Previous Trip is a Flying trip. Previous duty period that we check for rest start is the last duty period in the previous triptempRestStart = fcnFindRestForDutyStartBetweenDutiesInATrip (theTripList, prevTripCounter, previousTrip.dutyPeriodList.size() -1 ). if tempRestStart <> null thenreturn tempRestStart.} else if fcnNonflyIsForFaaRest(previousTrip) then {// Previous trip is a Duty NonFlyif (fcnGetPreviousTripAdjustedForAirportStandby(theTripList, prevTripCounter) = previousTrip) thenreturn previousTrip.endDateTime.} else if (previousTrip.nonFlyCode = (ignoring case)"REST") then {// When Previous trip is a REST nonfly, this should be counted as part of the Rest for Dutyreturn previousTrip.beginDateTime.}}prevTripCounter -= 1.}return null.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnFindRestForDutyStartBetweenDutiesInATrip](fcnFindRestForDutyStartBetweenDutiesInATrip.md)
- [fcnGetPreviousTripAdjustedForAirportStandby](fcnGetPreviousTripAdjustedForAirportStandby.md)
- [fcnNonflyIsForFaaRest](fcnNonflyIsForFaaRest.md)

## Llamado por

- [fcnDetermineDutyPeriodRest](fcnDetermineDutyPeriodRest.md)
- [fcnDetermineNonflyTripRest](fcnDetermineNonflyTripRest.md)
- [fcnFindRestForDutyStartBetweenDutiesInATrip](fcnFindRestForDutyStartBetweenDutiesInATrip.md)

## Historial de cambios

```
12/18/2014 US19195 Mitesh P  - This function will loop back through the previous trips in order to determine where Rest For Duty should start before a trip, or before the first duty period in a trip
03/19/2015 - US20257 - Melissa S - Modified to use fcnNonflyIsForFaaRest instead of isDutyNonFly
05/12/2015 - US20484 - Corey Gu - Added previousTrip.ghostedFlag = false ro the if statement.
9/25/2015 - DE7517 - Melissa S - Added logic for REST nonfly - if a REST nonfly is before the duty, count in the "rest for duty" amount
05/03/2016 - CSCH-2855 Jaime P - Updated to get previous trip adjusted for airport standby
```

