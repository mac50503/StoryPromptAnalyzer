# fcnFindRestForDutyStartBetweenDutiesInATrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnFindRestForDutyStartBetweenDutiesInATrip`

## Propósito
12/18/2014 US19195 Mitesh P  - This function will loop back through the previous duty periods within a trip in order to determine where rest should start

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripList | List<LegalityTrip> | |
| tripCounter | integer | |
| dutyPeriodCounter | integer | |

## Lógica de negocio

```blaze
theTrip is some LegalityTrip initially theTripList.get(tripCounter);prevDutyCounter is an integer initially dutyPeriodCounter.previousDutyPeriod is some LegalityDutyPeriod.while prevDutyCounter >= 0 do {previousDutyPeriod = theTrip.dutyPeriodList.get(prevDutyCounter).if (previousDutyPeriod.allRSDeadheads = false and previousDutyPeriod.legalityTrip.tripType <> (ignoring case) "R") then {return previousDutyPeriod.releaseDateTime.}prevDutyCounter -= 1.}// If the end of the while loop (start of the duty list) has been reached and no rest start date time has been returned, that means we need to keep looking back through previous trips.return fcnFindRestForDutyStartBeforeTrip(theTripList, tripCounter-1)
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnFindRestForDutyStartBeforeTrip](fcnFindRestForDutyStartBeforeTrip.md)

## Llamado por

- [fcnDetermineDutyPeriodRest](fcnDetermineDutyPeriodRest.md)
- [fcnFindRestForDutyStartBeforeTrip](fcnFindRestForDutyStartBeforeTrip.md)

## Historial de cambios

```
12/18/2014 US19195 Mitesh P  - This function will loop back through the previous duty periods within a trip in order to determine where rest should start
5/5/2015 - DE6520 - Melissa S - Changed from checking contractDutyDuration &gt; 0 to checking allRSDeadheads and tripType&lt;&gt;R because there are some cases where contractDuty is 0 but we want to combine
```

