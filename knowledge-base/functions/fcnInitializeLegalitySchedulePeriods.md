# fcnInitializeLegalitySchedulePeriods

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnInitializeLegalitySchedulePeriods`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLegalityTripList | List<LegalityTrip> | |
| theSchedulePeriodList | List<LegalitySchedulePeriod> | |

## Lógica de negocio

```blaze
if (theLegalityTripList is not equal to null and    theLegalityTripList is not equal to unknown and    theLegalityTripList.size() > 0 andtheSchedulePeriodList is not equal to null and    theSchedulePeriodList is not equal to unknown andtheSchedulePeriodList.size() > 0) then{theLegalitySchedulePeriod is some LegalitySchedulePeriod initially null.for each LegalitySchedulePeriod in theSchedulePeriodList as an array of LegalitySchedulePeriod do{theLegalitySchedulePeriod = it.for each LegalityTrip in theLegalityTripList as an array of LegalityTrip such that (it.beginDateTime >= theLegalitySchedulePeriod.schedulePeriodStart and it.beginDateTime <= theLegalitySchedulePeriod.schedulePeriodEnd) do{theLegalitySchedulePeriod.legalityTripList.add(it).if (it.dutyPeriodList is not equal to null and    it.dutyPeriodList is not equal to unknown and    it.dutyPeriodList.size() > 0) then{for each LegalityDutyPeriod in it.dutyPeriodList as an array of LegalityDutyPeriod do{aDutyPeriod is some LegalityDutyPeriod initially it.if (aDutyPeriod.legList <> null and aDutyPeriod.legList.size() > 0) then{for each LegalityLeg in aDutyPeriod.legList as an array of LegalityLeg such that (it.actualInDateTime <> null and it.actualInDateTime >= theLegalitySchedulePeriod.schedulePeriodStart and it.actualInDateTime <= theLegalitySchedulePeriod.schedulePeriodEnd) do{theLegalitySchedulePeriod.legalityLegList.add(it).}}}}}}}
```

