# fcnNonFlyRequiresRest

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnNonFlyRequiresRest`

## Propósito
03/12/2015 - US20192 - Melissa S - New function to do the lookup for all nonfly lists that are valid for Requires Rest

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | LegalityTrip | |

## Lógica de negocio

```blaze
return (theTrip.isTrainingNonFly or              theTrip.isAirportStandbyNonFly).
```

## Historial de cambios

```
03/12/2015 - US20192 - Melissa S - New function to do the lookup for all nonfly lists that are valid for Requires Rest
03/19/2015 - US20257 - Melissa S - Modified to use nonfly types save on the trip
```

