# fcnFindPreviousDutyToCombineForFAADuty

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnFindPreviousDutyToCombineForFAADuty`

## Propósito
12/26/2014 US19126 Mitesh P - This function loops back through the previous duty periods within a trip in order to determine where Rest For Duty is &gt;= 8 hours and

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripList | List<LegalityTrip> | |
| tripCounter | integer | |
| dutyPeriodCounter | integer | |

## Lógica de negocio

```blaze
theTrip is some LegalityTrip initially theTripList.get(tripCounter).previousDutyPeriod is some LegalityDutyPeriod.prevDutyCounter is an integer initially dutyPeriodCounter.while prevDutyCounter >=0 do {previousDutyPeriod = theTrip.dutyPeriodList.get(prevDutyCounter).if (previousDutyPeriod.restForDuty >= 480 or previousDutyPeriod.restForDuty <0 )thenreturn previousDutyPeriod.reportDateTime.prevDutyCounter -=1.} // If the end of the while loop (start of the duty list) has been reached and no new duty start date time has been returned, keep looking back through previous trips.return fcnFindPreviousTripToCombineForFAADuty(theTripList, tripCounter-1).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnFindPreviousTripToCombineForFAADuty](fcnFindPreviousTripToCombineForFAADuty.md)

## Llamado por

- [fcnDetermineCombinedDutyDurationForDutyPeriod](fcnDetermineCombinedDutyDurationForDutyPeriod.md)
- [fcnFindPreviousTripToCombineForFAADuty](fcnFindPreviousTripToCombineForFAADuty.md)

## Historial de cambios

```
12/26/2014 US19126 Mitesh P - This function loops back through the previous duty periods within a trip in order to determine where Rest For Duty is &gt;= 8 hours and
return the FAA Duty start date time of that Duty Period. If all duty periods are checked and no new duty start is found, then the fcnFindPreviousTripToCombineForFAADuty will be called to
continue looping outside the trip.
```

