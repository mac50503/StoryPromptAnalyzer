# fcnMaxFaaRestInWindow

## Metadata
- **Tipo**: SRL Function
- **Retorna**: integer
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnMaxFaaRestInWindow`

## Propósito
5/6/2015 - DE6514 -Melissa S -Changed to use faaRestForWIndow instead of faaRest due to new requirements

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| windowStartDateTime | DateTime | |
| windowEndDateTime | DateTime | |
| tripList | List<LegalityTrip> | |
| tripIndex | integer | |
| dutyPeriodIndex | integer | |

## Lógica de negocio

```blaze
prvDutyIndex is a integer initially dutyPeriodIndex.prvTripIndex is a integer initially tripIndex.dutyPeriodDone is a boolean initially false.tripDone is a boolean initially false.aTrip is some LegalityTrip.aDutyPeriod is some LegalityDutyPeriod. maxRest is an integer initially -1.partialRest  is an integer initially 0.//Because this is a "shared" function and could be called when checking either a trip or a duty period, when it is called for a trip, the dutyPeriodIndex passed in should be -1 so it skips this partif (dutyPeriodIndex <> -1) then {//If we are starting on a duty period, need to process all of the previous duty periods in the trip before moving through the trip listaTrip = tripList.get(tripIndex).while (prvDutyIndex >= 0 and dutyPeriodDone = false) do {aDutyPeriod = aTrip.dutyPeriodList.get(prvDutyIndex).if (aDutyPeriod.reportDateTime.isAfter(windowEndDateTime) = false ) then {if (aDutyPeriod.reportDateTime.isEqual(windowStartDateTime) or aDutyPeriod.reportDateTime.isAfter(windowStartDateTime)) then {if (aDutyPeriod.reportDateTime.minusMinutes(aDutyPeriod.faaRestForWindow).isBefore(windowStartDateTime)) then {// Rest spans the window start – look at partial rest amount inside the windowpartialRest = fcnGetTimeDiffInMinutes(windowStartDateTime, aDutyPeriod.reportDateTime).if (partialRest > maxRest) thenmaxRest = partialRest.} else            if (aDutyPeriod.faaRestForWindow > maxRest) thenmaxRest = aDutyPeriod.faaRestForWindow.  prvDutyIndex = prvDutyIndex -1.} elsedutyPeriodDone = true.} elseprvDutyIndex = prvDutyIndex -1.}prvTripIndex = prvTripIndex -1.}if (dutyPeriodDone = false) then {while ( prvTripIndex >= 0 and tripDone = false) do {       aTrip = tripList.get(prvTripIndex).       if (aTrip.ghostedFlag = false) then { // US20484if (aTrip.isNonFly = true) then {if (aTrip.beginDateTime.isBefore(windowEndDateTime)) then {// Trips beginning within the window range should be evaluated for the right amount of restif (aTrip.beginDateTime.isEqual(windowStartDateTime) or aTrip.beginDateTime.isAfter(windowStartDateTime)) then {if (aTrip.beginDateTime.minusMinutes(aTrip.faaRestForWindow).isBefore(windowStartDateTime)) then {// Rest spans the window start – look at partial rest amount inside the windowpartialRest = fcnGetTimeDiffInMinutes(windowStartDateTime, aTrip.beginDateTime).if (partialRest > maxRest) then {maxRest = partialRest.}} else {if (aTrip.faaRestForWindow > maxRest) then {maxRest = aTrip.faaRestForWindow.}}} else tripDone = true.}} else { // if the trip is not a NonflyprvDutyIndex =  aTrip.dutyPeriodList.size() - 1.while (prvDutyIndex >= 0 and dutyPeriodDone = false) do {aDutyPeriod = aTrip.dutyPeriodList.get(prvDutyIndex).if (aDutyPeriod.reportDateTime.isBefore(windowEndDateTime) ) then {if (aDutyPeriod.reportDateTime.isEqual(windowStartDateTime) or aDutyPeriod.reportDateTime.isAfter(windowStartDateTime)) then {if (aDutyPeriod.reportDateTime.minusMinutes(aDutyPeriod.faaRestForWindow).isBefore(windowStartDateTime)) then {// Rest spans the window start – look at partial rest amount inside the windowpartialRest = fcnGetTimeDiffInMinutes(windowStartDateTime, aDutyPeriod.reportDateTime).if (partialRest > maxRest) then {maxRest = partialRest.}} else            if (aDutyPeriod.faaRestForWindow > maxRest) then {maxRest = aDutyPeriod.faaRestForWindow.}prvDutyIndex = prvDutyIndex -1.} else {dutyPeriodDone = true.tripDone = true.}} elseprvDutyIndex = prvDutyIndex -1.}}       }       prvTripIndex = prvTripIndex -1.}}return maxRest.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)

## Historial de cambios

```
5/6/2015 - DE6514 -Melissa S -Changed to use faaRestForWIndow instead of faaRest due to new requirements
5/7/2015 - DE5641 - Melissa S - Changed to check that report is before OR EQUAL to the window end for cases where the report/release are the same and we still want the max rest to be calculated
05/12/2015 Corey Gu US20484 - Added if (aTrip.ghostedFlag = false) condition
```

