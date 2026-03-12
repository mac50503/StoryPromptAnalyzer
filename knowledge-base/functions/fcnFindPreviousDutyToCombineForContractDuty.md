# fcnFindPreviousDutyToCombineForContractDuty

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnFindPreviousDutyToCombineForContractDuty`

## Propósito
12/30/2014 US19132 Mitesh P - This function loops back through the previous duty periods within a trip in order to determine where Rest For Duty is &gt;= 8 hours and

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripList | List<LegalityTrip> | |
| tripCounter | integer | |
| dutyPeriodCounter | integer | |
| combineForDuty | CombineForDuty | |

## Lógica de negocio

```blaze
theTrip is some LegalityTrip initially theTripList.get(tripCounter).previousDutyPeriod is some LegalityDutyPeriod.prevDutyCounter is an integer initially dutyPeriodCounter.while (prevDutyCounter >=0)do {previousDutyPeriod = theTrip.dutyPeriodList.get(prevDutyCounter).if previousDutyPeriod.restForDuty >= 480 then {for each LegalityLeg in previousDutyPeriod.legList as an array of LegalityLeg do combineForDuty.dutyLegs.add(it).combineForDuty.dutyStartDateTime = previousDutyPeriod.contDutyStartDateTime.prevDutyCounter = 0.}prevDutyCounter -=1.} // If the end of the while loop (start of the duty list) has been reached and no new duty start date time has been returned, keep looking back through previous trips.if (combineForDuty.dutyStartDateTime is unknown or combineForDuty.dutyStartDateTime is null) thenfcnFindPreviousTripToCombineForContractDuty(theTripList, tripCounter-1, combineForDuty).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnFindPreviousTripToCombineForContractDuty](fcnFindPreviousTripToCombineForContractDuty.md)

## Llamado por

- [fcnDetermineCombinedDutyDurationForDutyPeriod](fcnDetermineCombinedDutyDurationForDutyPeriod.md)
- [fcnFindPreviousTripToCombineForContractDuty](fcnFindPreviousTripToCombineForContractDuty.md)

## Historial de cambios

```
12/30/2014 US19132 Mitesh P - This function loops back through the previous duty periods within a trip in order to determine where Rest For Duty is &gt;= 8 hours and
return the Contract Duty start date time of that Duty Period. If all duty periods are checked and no new duty start is found, then the fcnFindPreviousTripToCombineForContractDuty will be called to
continue looping outside the trip.
1/28/2015 US19445 Mitesh P - Updated to use class CombineForDuty instead
```

