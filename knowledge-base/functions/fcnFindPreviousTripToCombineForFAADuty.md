# fcnFindPreviousTripToCombineForFAADuty

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnFindPreviousTripToCombineForFAADuty`

## Propósito
12/26/2014 US19126 Mitesh P - This function loops back through the previous trips in order to determine the next previous trip or duty period where Rest For Duty is &gt;= 8 hours and

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripList | List<LegalityTrip> | |
| tripCounter | integer | |

## Lógica de negocio

```blaze
prevTripCounter is an integer initially tripCounter.previousTrip is some LegalityTrip.tempDutyStart is some DateTime.while prevTripCounter >=0 do {previousTrip = theTripList.get(prevTripCounter).if (previousTrip.ghostedFlag = false) then {if (previousTrip.isNonFly = false and previousTrip.tripType<>(ignoring case)"R") then { // Previous Trip is a Flying trip and is not a Reserve Block//Previous duty period that we check for new duty start is the last duty period in the previous triptempDutyStart = fcnFindPreviousDutyToCombineForFAADuty (theTripList, prevTripCounter, previousTrip.dutyPeriodList.size()-1).if tempDutyStart <> nullthenreturn tempDutyStart.} else if (previousTrip.isDutyNonFly = true and (previousTrip.restForDuty >= 480 or previousTrip.restForDuty <0)) then//Previous trip is a Duty NonFly and has 8 or more hours of rest for dutyif (fcnGetPreviousTripAdjustedForAirportStandby(theTripList, prevTripCounter) = previousTrip) thenreturn previousTrip.beginDateTime.}prevTripCounter -=1.}return null.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnFindPreviousDutyToCombineForFAADuty](fcnFindPreviousDutyToCombineForFAADuty.md)
- [fcnGetPreviousTripAdjustedForAirportStandby](fcnGetPreviousTripAdjustedForAirportStandby.md)

## Llamado por

- [fcnDetermineCombinedDutyDurationForDutyPeriod](fcnDetermineCombinedDutyDurationForDutyPeriod.md)
- [fcnDetermineCombinedDutyDurationForTrip](fcnDetermineCombinedDutyDurationForTrip.md)
- [fcnFindPreviousDutyToCombineForFAADuty](fcnFindPreviousDutyToCombineForFAADuty.md)

## Historial de cambios

```
12/26/2014 US19126 Mitesh P - This function loops back through the previous trips in order to determine the next previous trip or duty period where Rest For Duty is &gt;= 8 hours and
returns the FAA Duty start date time for that trip or duty period.
01/29/2014 US19443 Akshay - Added logic for rest nonfly
05/12/2015 US20484 Corey Gu - Added previousTrip.ghostedFlag = false condition.
9/25/2015 - DE7517 - Melissa S - Removed logic for REST nonfly - moved to use the REST value in the "rest for duty" logic instead
05/03/2016 - CSCH-2855 Jaime P - Updated to get previous trip adjusted for airport standby
```

