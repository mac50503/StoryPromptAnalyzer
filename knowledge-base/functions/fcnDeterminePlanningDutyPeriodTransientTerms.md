# fcnDeterminePlanningDutyPeriodTransientTerms

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnDeterminePlanningDutyPeriodTransientTerms`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | LegalityDutyPeriod | |
| theTrip | LegalityTrip | |

## Lógica de negocio

```blaze
if theTrip.tripType <> "R" then {theDutyPeriod.faaDutyStartDateTime = theDutyPeriod.reportDateTime.theDutyPeriod.faaDutyEndDateTime = theDutyPeriod.releaseDateTime.theDutyPeriod.faaDutyDuration = fcnGetTimeDiffInMinutes(theDutyPeriod.faaDutyStartDateTime, theDutyPeriod.faaDutyEndDateTime).theDutyPeriod.contDutyStartDateTime = theDutyPeriod.reportDateTime.theDutyPeriod.contDutyEndDateTime = theDutyPeriod.releaseDateTime.theDutyPeriod.contDutyDuration = theDutyPeriod.faaDutyDuration.// Determine if a duty period has only deadheadsif (exactly 0 LegalityLeg in theDutyPeriod.legList as an array of LegalityLeg satisfies(it.isDeadhead = false)) then {              theDutyPeriod.allDeadheads = true.}// Determine the number of aircraft / route changes within a dutypreviousRoute is a string initially theDutyPeriod.legList.get(0).route.for each LegalityLeg in theDutyPeriod.legList as an array of LegalityLeg do {if (previousRoute <> it.route) then {theDutyPeriod.numRouteChanges += 1.}previousRoute = it.route.}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)

