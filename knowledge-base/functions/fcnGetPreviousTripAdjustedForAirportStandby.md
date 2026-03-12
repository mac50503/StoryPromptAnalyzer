# fcnGetPreviousTripAdjustedForAirportStandby

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegalityTrip
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnGetPreviousTripAdjustedForAirportStandby`

## Propósito
05/03/2016 - CSCH-2855 Jaime P - New function to get previous trip takes into account airport standby

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripList | List<LegalityTrip> | |
| tripCounter | integer | |

## Lógica de negocio

```blaze
if (tripCounter -1 >= 0) then {//There is a trip before the previous trip// If the previous trip is an airport standby nonfly, and the trip before it is a reserve // trip and the airport standby starts after the reserve trip and // the reserve trip ends after the airport standbyif(theTripList.get(tripCounter).isAirportStandbyNonFly andtheTripList.get(tripCounter -1).assignmentLabel = (ignoring case) ("R" or "S") andtheTripList.get(tripCounter - 1).beginDateTime <= theTripList.get(tripCounter).beginDateTime andtheTripList.get(tripCounter - 1).endDateTime > theTripList.get(tripCounter).endDateTime) thenreturn theTripList.get(tripCounter - 1) //Return the reserve trip before the Airport Standbyelse return theTripList.get(tripCounter) //Return the previous trip} else return theTripList.get(tripCounter) //Just return the previous trip if there is not one before it
```

## Llamado por

- [fcnFindPreviousTripToCombineForContractDuty](fcnFindPreviousTripToCombineForContractDuty.md)
- [fcnFindPreviousTripToCombineForFAADuty](fcnFindPreviousTripToCombineForFAADuty.md)
- [fcnFindRestForDutyStartBeforeTrip](fcnFindRestForDutyStartBeforeTrip.md)

## Historial de cambios

```
05/03/2016 - CSCH-2855 Jaime P - New function to get previous trip takes into account airport standby
```

