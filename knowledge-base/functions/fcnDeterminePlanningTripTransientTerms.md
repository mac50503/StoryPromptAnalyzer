# fcnDeterminePlanningTripTransientTerms

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnDeterminePlanningTripTransientTerms`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | LegalityTrip | |
| theGlobalDataCache | GlobalDataCache | |

## Lógica de negocio

```blaze
highestLegCountDutyPeriod is some LegalityDutyPeriod initially null;smallestTfpDutyPeriod is some LegalityDutyPeriod initially null;previousDutyPeriod is some LegalityDutyPeriod initially null;if (theTrip.languageMap = null) then {theTrip.languageMap = a LinkedHashMap.}for each LegalityDutyPeriod in theTrip.dutyPeriodList as an array of LegalityDutyPeriod do {// Find Duty Period with the highest leg countif (highestLegCountDutyPeriod is null or it.legList.size() > highestLegCountDutyPeriod.legList.size()) then {highestLegCountDutyPeriod = it;}// Determine if the Duty Period is a Single Deadhead (Only has one leg and that leg is a deadhead) if (it.legList.size() = 1 and it.firstLeg.isDeadhead) then {it.singleDeadhead = true;}if (it.singleDeadhead = false and it.isShortback = false and (smallestTfpDutyPeriod is null or it.tfp < smallestTfpDutyPeriod.tfp)) then {smallestTfpDutyPeriod = it;}// Calculate the Duty Period's FAA Restif (previousDutyPeriod is null) then {it.faaRest = 0;} else {it.faaRest = fcnGetTimeDiffInMinutes(previousDutyPeriod.releaseDateTime, it.reportDateTime);}previousDutyPeriod = it;// Determine number of languages on a Tripif (theGlobalDataCache <> null and theGlobalDataCache.stationMap <> null) then {for each LegalityLeg in it.legList as an array of LegalityLeg do {// Only consider languages on active legsif (it.isDeadhead = false) then { departureStationObject is some Station initially theGlobalDataCache.stationMap.get(it.departureLocation);arrivalStationObject is some Station initially theGlobalDataCache.stationMap.get(it.arrivalLocation);if (departureStationObject <> null and departureStationObject.languageCode <> null and theTrip.languageMap.containsKey(departureStationObject.languageCode) = false) then {theTrip.languageMap.put(departureStationObject.languageCode, it);}if (arrivalStationObject <> null and arrivalStationObject.languageCode <> null and theTrip.languageMap.containsKey(arrivalStationObject.languageCode)=false) then {theTrip.languageMap.put(arrivalStationObject.languageCode, it);}}}}}if (highestLegCountDutyPeriod <> null) then {highestLegCountDutyPeriod.mostLegsInTrip = true;}if (smallestTfpDutyPeriod <> null) then {smallestTfpDutyPeriod.smallestTfpInTrip = true;}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)

