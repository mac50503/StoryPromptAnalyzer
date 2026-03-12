# rsFAARestCalculationForNonfly

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Rulesets\rsFAARestCalculationForNonfly`

## Propósito
2/16/2015 US18869 Mitesh P - This ruleset calculates FAA Rest for Nonfly trips

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | LegalityTrip | |
| theRestValues | RestValues | |

## Historial de cambios

```
2/16/2015 US18869 Mitesh P - This ruleset calculates FAA Rest for Nonfly trips
2/23/2015 US16635 Mitesh P - Added default rule to set faaRest to -1.
03/19/2015 - US20257 - Melissa S - Modified to use fcnNonflyIsForFaaRest instead of isDutyNonFly
4/6/2015 Corey Gu US16625/US16626 - Change faaRest value from 1440 to 10080 in noPriorRelease per Melissa.
5/6/2015 - DE6514 -Melissa S - Added setting new faaRestForWindow property
9/4/2015 - Melissa S - DE7351 - Added setting faaCompRest value
```

