# fcnDetermineNonflyTripRest

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnDetermineNonflyTripRest`

## Propósito
12/18/2014 US19195 Mitesh P  - Calculate the Rest value that will be used to determine if Duty values should be combined

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | LegalityTrip | |
| theTripList | List<LegalityTrip> | |
| tripCounter | integer | |

## Lógica de negocio

```blaze
if (fcnNonflyIsForFaaRest(theTrip)) then {restStart is some DateTime.// Initialize default Rest For Duty values in minutestheTrip.restForDuty = 2880.// Call the fcnFindRestForDutyStartBeforeTrip using theTripCounter-1 since we want to start looking for the rest start with the PREVIOUS trip, not the one we are calculating rest forrestStart = fcnFindRestForDutyStartBeforeTrip(theTripList, tripCounter-1).if restStart <> null then {theTrip.restForDuty = fcnGetTimeDiffInMinutes(restStart, theTrip.beginDateTime).}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnFindRestForDutyStartBeforeTrip](fcnFindRestForDutyStartBeforeTrip.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)
- [fcnNonflyIsForFaaRest](fcnNonflyIsForFaaRest.md)

## Historial de cambios

```
12/18/2014 US19195 Mitesh P  - Calculate the Rest value that will be used to determine if Duty values should be combined
03/19/2015 - US20257 - Melissa S - Updated to use fcnNonflyIsForFaaRest instead of isDutyNonFly
```

