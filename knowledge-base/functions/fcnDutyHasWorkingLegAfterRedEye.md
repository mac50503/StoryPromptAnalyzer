# fcnDutyHasWorkingLegAfterRedEye

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegalityLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnDutyHasWorkingLegAfterRedEye`

## Propósito
4/10/2015 US20013 Mitesh P/Lohit B - This function checks if there is any working leg that is after Red Eye Leg and has a scheduled departure time after the Red Eye Window

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | LegalityDutyPeriod | |
| redEyeEndTime | LocalTime | |
| redEyeLeg | LegalityLeg | |

## Lógica de negocio

```blaze
if (redEyeLeg is not null) then {for each LegalityLeg in theDutyPeriod.contractDutyLegs as an array of LegalityLeg such that (it.scheduledDepartureInLocalTimezone > redEyeLeg.determineArrivalDateTime() andit.scheduledDepartureInLocalTimezone.toLocalTime() > redEyeEndTime and it.isDeadhead is false)do { return it.}}return null.
```

## Historial de cambios

```
4/10/2015 US20013 Mitesh P/Lohit B - This function checks if there is any working leg that is after Red Eye Leg and has a scheduled departure time after the Red Eye Window
04/14/2015 - US20563 - Melissa S - Modified to return the leg instead of a boolean so that the leg information can be used in the message string
```

