# fcnDetermineAdjustedTimeWithBase

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnDetermineAdjustedTimeWithBase`

## Propósito
// Determine Duty Period report date time adjusted to the trip's begin location -- US11150

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theReportDateTime | DateTime | |
| theTimezone | string | |

## Lógica de negocio

```blaze
if (theReportDateTime <> null) thenreturn DateTimeUtilities.convertDateTimeToTimezone(theReportDateTime, theTimezone).elsereturn null.
```

## Historial de cambios

```
// Determine Duty Period report date time adjusted to the trip's begin location -- US11150
DE2706 - 1/4/14 - Ben L - Use theDutyPeriodDerivedTerms.reportDateTime instead of theDutyPeriod.reportDateTime
CSCH-573 - Rachel S - Moved from FO to Common. Changing to use DateTime instead of DutyPeriodDervivedTerms.
```

