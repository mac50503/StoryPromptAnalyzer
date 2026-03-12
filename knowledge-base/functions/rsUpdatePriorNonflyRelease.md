# rsUpdatePriorNonflyRelease

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Rulesets\rsUpdatePriorNonflyRelease`

## Propósito
2/16/2015 US18869 Mitesh P - This ruleset updates information about a previous nonfly so that is can be used in the Rest calculations

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | LegalityTrip | |
| theRestValues | RestValues | |

## Historial de cambios

```
2/16/2015 US18869 Mitesh P - This ruleset updates information about a previous nonfly so that is can be used in the Rest calculations
03/19/2015 - US20257 - Melissa S - Modified to use fcnNonflyIsForFaaRest instead of isDutyNonFly
03/25/2015 - US16631 - Melissa S - Modified to use value saved in durationBeginToEnd instead of calculating here
9/24/2015 - DE7351 - Melissa S - Added logic/split rules to update the new priorDutyReleaseUnderReserve property
```

