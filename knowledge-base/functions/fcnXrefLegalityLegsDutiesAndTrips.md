# fcnXrefLegalityLegsDutiesAndTrips

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnXrefLegalityLegsDutiesAndTrips`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aLegalityTripList | List<LegalityTrip> | |

## Lógica de negocio

```blaze
if (aLegalityTripList <> null and aLegalityTripList.size() > 0) then{aLegalityTrip is some LegalityTrip initially null.aLegalityDutyPeriod is some LegalityDutyPeriod initially null.aLegalityLeg is some LegalityLeg initially null.for each LegalityTrip in aLegalityTripList as an array of LegalityTrip do {aLegalityTrip = it.if (aLegalityTrip.dutyPeriodList <> null and aLegalityTrip.dutyPeriodList.size() > 0) then{for each LegalityDutyPeriod in aLegalityTrip.dutyPeriodList as an array of LegalityDutyPeriod do{aLegalityDutyPeriod = it.fcnXrefLegalityDutyPeriodToLegalityTrip(aLegalityDutyPeriod, aLegalityTrip).if (aLegalityDutyPeriod.legList <> null and aLegalityDutyPeriod.legList.size() > 0) then{for each LegalityLeg in aLegalityDutyPeriod.legList as an array of LegalityLeg do{aLegalityLeg = it.fcnXrefLegalityLegToLegalityDutyPeriod(aLegalityLeg, aLegalityDutyPeriod).}}}}}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnXrefLegalityDutyPeriodToLegalityTrip](fcnXrefLegalityDutyPeriodToLegalityTrip.md)
- [fcnXrefLegalityLegToLegalityDutyPeriod](fcnXrefLegalityLegToLegalityDutyPeriod.md)

