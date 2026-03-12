# fcnGetLegalityLegCalendarArray

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnGetLegalityLegCalendarArray`

## Propósito
02/06/2015 Corey Gu - US16610  Initial development

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLegalityTripList | List<LegalityTrip> | |
| theSchedulePeriod | LegalitySchedulePeriod | |

## Lógica de negocio

```blaze
theLegs is some array of LegalityLeg initially an array of LegalityLeg.for each LegalityTrip in theLegalityTripList as an array of LegalityTrip such that (it.ghostedFlag = false) do {if (it.dutyPeriodList <> null and it.dutyPeriodList <> unknown and it.dutyPeriodList.size() > 0) then {for each LegalityDutyPeriod in it.dutyPeriodList as an array of LegalityDutyPeriod do {aDutyPeriod is some LegalityDutyPeriod initially it.for each LegalityLeg in aDutyPeriod.legList as an array of LegalityLeg such that (it.determineDepartureDateTime() >= theSchedulePeriod.schedulePeriodStart.toDateMidnight() and     it.determineDepartureDateTime() <= theSchedulePeriod.schedulePeriodEnd.toDateMidnight()) do{theLegs.append(it).}}}}return theLegs.
```

## Historial de cambios

```
02/06/2015 Corey Gu - US16610  Initial development
03/26/2015 - Melissa S - Changed the -3 hours to use toDateMidnight()
05/12/2015 Corey Gu - US20484 - Added such that (it.ghostedFlag = false) in the for each statement.
```

