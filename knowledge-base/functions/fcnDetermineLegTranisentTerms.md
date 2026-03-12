# fcnDetermineLegTranisentTerms

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnDetermineLegTranisentTerms`

## Propósito
1/8/2015 US16599 Mitesh P - This function should set some basic values for the legs that will be reused throughout the rules

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLeg | LegalityLeg | |
| theGlobalDataCache | GlobalDataCache | |

## Lógica de negocio

```blaze
depLocFromStationMap is some Station initially  theGlobalDataCache.stationMap.get(theLeg.departureLocation).arrLocFromStationMap is some Station initially theGlobalDataCache.stationMap.get(theLeg.arrivalLocation).if depLocFromStationMap is not null then theLeg.scheduledDepartureInLocalTimezone = DateTimeUtilities.convertDateTimeToTimezone(theLeg.scheduledDepartureDateTime, depLocFromStationMap.timezone).if arrLocFromStationMap is not null then theLeg.scheduledArrivalInLocalTimezone = DateTimeUtilities.convertDateTimeToTimezone(theLeg.scheduledArrivalDateTime, arrLocFromStationMap.timezone).
```

## Historial de cambios

```
1/8/2015 US16599 Mitesh P - This function should set some basic values for the legs that will be reused throughout the rules
```

