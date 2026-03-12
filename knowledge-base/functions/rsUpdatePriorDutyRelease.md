# rsUpdatePriorDutyRelease

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Rulesets\rsUpdatePriorDutyRelease`

## Propósito
2/16/2015 US18869 Mitesh P - This ruleset updates information about a previous duty period so that is can be used in the Rest calculations

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | LegalityDutyPeriod | |
| theRestValues | RestValues | |

## Historial de cambios

```
2/16/2015 US18869 Mitesh P - This ruleset updates information about a previous duty period so that is can be used in the Rest calculations
5/5/2015 - DE6510 - Melissa S - Not setting priorDutyRelease if the DutyPeriod has all RS deadheads
9/24/2015 - DE7351 - Melissa S - Added logic/split rules to update the new priorDutyReleaseUnderReserve property
10/20/2015 - DE7648 - Melissa S - Added new rule reserveBlockResetPriorDutyReleaseUnderReserve to reset the priorDutyReleaseUnderReserve for a new set of reserve blocks
08/04/2022 - APIC-531 - Alex F - Added logic for setting lastReserveRelease after 10 hour rest effective date
```

