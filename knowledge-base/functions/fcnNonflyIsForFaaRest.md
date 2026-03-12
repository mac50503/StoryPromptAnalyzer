# fcnNonflyIsForFaaRest

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnNonflyIsForFaaRest`

## Propósito
03/19/2015 - US20257 - Melissa S - New function

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | LegalityTrip | |

## Lógica de negocio

```blaze
return (theTrip.isTrainingNonFly or theTrip.isMiscNonFly or theTrip.isAirportStandbyNonFly or theTrip.isMiscWorkingNonFly).
```

## Llamado por

- [fcnDetermineNonflyTripRest](fcnDetermineNonflyTripRest.md)
- [fcnDetermineTripAdditionalTransientTerms](fcnDetermineTripAdditionalTransientTerms.md)
- [fcnFindRestForDutyStartBeforeTrip](fcnFindRestForDutyStartBeforeTrip.md)

## Historial de cambios

```
03/19/2015 - US20257 - Melissa S - New function
```

