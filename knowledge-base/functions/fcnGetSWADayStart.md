# fcnGetSWADayStart

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnGetSWADayStart`

## Propósito
04/09/2015 - US20485 - Melissa S - New function to calculate the start of the SWA day for a given DateTime

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| originalDateTime | DateTime | |

## Lógica de negocio

```blaze
if (originalDateTime.hourOfDay < 3) then {return originalDateTime.minusDays(1).withTime(3,0,0,0).} else {return originalDateTime.withTime(3,0,0,0).}
```

## Llamado por

- [fcnDetermineTripTransientTerms](fcnDetermineTripTransientTerms.md)
- [fcnGetTrainingRenewDate](fcnGetTrainingRenewDate.md)

## Historial de cambios

```
04/09/2015 - US20485 - Melissa S - New function to calculate the start of the SWA day for a given DateTime
```

