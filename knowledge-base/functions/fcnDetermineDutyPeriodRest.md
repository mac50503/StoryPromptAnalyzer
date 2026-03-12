# fcnDetermineDutyPeriodRest

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnDetermineDutyPeriodRest`

## Propósito
12/02/2014 Corey Gu US19125 - Initial development

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | LegalityDutyPeriod | |
| dutyPeriodCounter | integer | |
| theTrip | LegalityTrip | |
| theTripList | List<LegalityTrip> | |
| tripCounter | integer | |

## Lógica de negocio

```blaze
// 1st Duty Period In Trip and has Contract DutyrestStart is some DateTime.// First duty on first trip - Set the rest to the default valueif (dutyPeriodCounter = 0 and tripCounter = 0) then {theDutyPeriod.restForDuty  = 2880.// Only calculate rest for duty for DutyPeriods on flying trips - no reserve blocks} else if (theTrip.isNonFly = false and theTrip.tripType <> (ignoring case) "R") then {// First duty and NOT on the first trip - Look back to previous trips to find restif (dutyPeriodCounter = 0) then {// Call the function using theTripCounter-1 since we want to start looking for the rest start with the PREVIOUS trip, not the one we want to calculate rest forrestStart = fcnFindRestForDutyStartBeforeTrip(theTripList, tripCounter-1).if (restStart <> null) then {theDutyPeriod.restForDuty = fcnGetTimeDiffInMinutes(restStart, theDutyPeriod.reportDateTime).} else {theDutyPeriod.restForDuty  = 2880.}// Not 1st Duty Period in Trip and has Contract Duty} else if (dutyPeriodCounter > 0) then {// Call the function using theDutyPeriodCounter-1 since we want to start looking for the rest start with the PREVIOUS Duty Period, not the one we want to calculate rest forrestStart = fcnFindRestForDutyStartBetweenDutiesInATrip(theTripList, tripCounter, dutyPeriodCounter - 1).if (restStart <> null) then {theDutyPeriod.restForDuty = fcnGetTimeDiffInMinutes(restStart, theDutyPeriod.reportDateTime).} else {theDutyPeriod.restForDuty  = 2880.}}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnFindRestForDutyStartBeforeTrip](fcnFindRestForDutyStartBeforeTrip.md)
- [fcnFindRestForDutyStartBetweenDutiesInATrip](fcnFindRestForDutyStartBetweenDutiesInATrip.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)

## Historial de cambios

```
12/02/2014 Corey Gu US19125 - Initial development
12/18/2014 US19195 Mitesh P  - Completely refactored to call new function to get the Rest for Duty start date time
12.30.2104 Melissa S - Set the default rest for the first duty on the first trip
03.11.2015 - DE6015 - Melissa S - Modified to not look at contractDuty &gt; 0
```

