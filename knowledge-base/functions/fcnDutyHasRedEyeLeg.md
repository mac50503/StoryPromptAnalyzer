# fcnDutyHasRedEyeLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegalityLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnDutyHasRedEyeLeg`

## Propósito
1/8/2015 US16599 Mitesh P - This function looks at the current Duty Period, and checks if there is any Leg that is considered to be in the Red Eye window.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | LegalityDutyPeriod | |
| redEyeStartTime | LocalTime | |
| redEyeEndTime | LocalTime | |

## Lógica de negocio

```blaze
for each LegalityLeg in theDutyPeriod.contractDutyLegs as an array of LegalityLeg such that ((it.limoFlag = false and it.scheduledDepartureInLocalTimezone is not null and it.scheduledArrivalInLocalTimezone is not null) and (// Leg starts in the window(it.scheduledDepartureInLocalTimezone.toLocalTime() >= redEyeStartTime and it.scheduledDepartureInLocalTimezone.toLocalTime() <= redEyeEndTime)or// Leg ends in the window(it.scheduledArrivalInLocalTimezone.toLocalTime() >= redEyeStartTime and it.scheduledArrivalInLocalTimezone.toLocalTime() <= redEyeEndTime)or// Leg spans entire window(it.scheduledDepartureInLocalTimezone.toLocalTime() < redEyeStartTime and it.scheduledArrivalInLocalTimezone.toLocalTime() > redEyeEndTime)or// Leg spans entire window – but starts on previous day(it.scheduledDepartureInLocalTimezone.toLocalDate() < it.scheduledArrivalInLocalTimezone.toLocalDate() and it.scheduledArrivalInLocalTimezone.toLocalTime() > redEyeEndTime)))do{ return it.}return null.
```

## Historial de cambios

```
1/8/2015 US16599 Mitesh P - This function looks at the current Duty Period, and checks if there is any Leg that is considered to be in the Red Eye window.
1/28/2015 US19445 Mitesh P - Updated to use class CombineForDuty instead
4/10/2015 US20013 Mitesh P/Lohit B - Changed to return Red Eye Leg
4/10/2015 Melissa S - Changed to only return red eye leg if not a deadhead
6/11/2015 - DE6795 - Melissa S - LIMO legs should not count as red eye legs
8/22/2105 - DE7269 - Melissa S - Removed condition for &lt;&gt; deadhead.  Deadhead legs need to be considered as red eye legs
```

