# rsFAARestCalculationForDutyPeriod

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Rulesets\rsFAARestCalculationForDutyPeriod`

## Propósito
2/16/2015 US18869 Mitesh P - This ruleset calculates FAA Rest for duty periods

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | LegalityDutyPeriod | |
| theRestValues | RestValues | |

## Historial de cambios

```
2/16/2015 US18869 Mitesh P - This ruleset calculates FAA Rest for duty periods
2/23/2015 US16635 Mitesh P - Added default rule to set faaRest to -1.
4/6/2015 Corey Gu US16625/US16626 - Change faaRest value from 1440 to 10080 in noPriorRelease per Melissa.
4/29/2015 - DE6478 - Melissa S - Updated reserveBlock rule to only fire when lastReserveRelease or priorDutyRelease is known.  Otherwise this rule is overriding the noPriorRelease rule when it shouldn't
5/6/2015 - DE6514 -Melissa S - Added setting new faaRestForWindow property
5/21/2015 - DE6691 - Melissa S - Split nonFirstDutyFlyingTrip into nonFirstDutyFlyingTripNoPriorDuty and nonFirstDutyFlyingTripPriorDuty.  If the only prior duty period in the same trip is all RS deadheads,
and it is the first trip, there won't be a prior duty value to go back to and default rest should be given
6/10/2015 - DE6781 - Melissa S - When a reserve trip starts before the reserve block, the reserve block should be given enough rest so that legalities don't fire.
9/4/2015 - Melissa S - DE7351 - Added setting faaCompRest value
```

