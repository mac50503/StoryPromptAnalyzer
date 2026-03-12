# fcnBuildDutyPeriodCalculatedValuesLists

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnBuildDutyPeriodCalculatedValuesLists`

## Propósito
5/1/2015 - DE6474 - Melissa S - Changed Duty Sum to use Report-Release instead of FAA Duty Duration

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | LegalityDutyPeriod | |
| theDutyPeriodBlockTimeList | List<DutyPeriodBlockTime> | |
| theDutyPeriodDutyDurationList | List<DutyPeriodDutyDuration> | |
| theDutyPeriodRestList | List<DutyPeriodRest> | |

## Lógica de negocio

```blaze
// Only return changed block timesif (theDutyPeriod.calculatedBlockTime <> theDutyPeriod.blockTime and theDutyPeriodBlockTimeList<>null) then {theDutyPeriodBlockTimeList.add(a DutyPeriodBlockTime initially {it.sequenceNumber = theDutyPeriod.sequenceNumber,it.blockTime = theDutyPeriod.calculatedBlockTime}).}// Only return changed duty durations// DE6474 - Changed Duty Sum to use Report-Release instead of FAA Duty DurationreportToRelease is an integer initially Duration.newInstance(theDutyPeriod.reportDateTime, theDutyPeriod.releaseDateTime).standardMinutes.if (reportToRelease <> theDutyPeriod.dutyDuration and theDutyPeriodDutyDurationList<>null) then {theDutyPeriodDutyDurationList.add(a DutyPeriodDutyDuration initially {it.sequenceNumber = theDutyPeriod.sequenceNumber,it.dutyDuration = reportToRelease}).}// Always return Rest valuesif (theDutyPeriodRestList<>null) then {theDutyPeriodRestList.add(a DutyPeriodRest initially {it.sequenceNumber = theDutyPeriod.sequenceNumber,it.rest = theDutyPeriod.faaRest}).}
```

## Historial de cambios

```
5/1/2015 - DE6474 - Melissa S - Changed Duty Sum to use Report-Release instead of FAA Duty Duration
```

