# fcnGetLegCountFromDutiesWithNoLegalRest

## Metadata
- **Tipo**: SRL Function
- **Retorna**: integer
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnGetLegCountFromDutiesWithNoLegalRest`

## Propósito
Ben Lang - US16607 - 2/17/2015 - Initial Development

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| dutyCounter | integer | |
| theTrip | LegalityTrip | |
| restLimit | integer | |

## Lógica de negocio

```blaze
legCount is an integer initially 0.loopCounter is an integer initially dutyCounter.theDutyPeriod is some LegalityDutyPeriod.prevDutyPeriod is some LegalityDutyPeriod.while (loopCounter >= 0)  do {theDutyPeriod = theTrip.dutyPeriodList.get(loopCounter).legCount += theDutyPeriod.legList.size().if loopCounter > 0 then {prevDutyPeriod = theTrip.dutyPeriodList.get(loopCounter - 1).//if the duration from thePrevious duty’s best available arrival time to theDutyPeriod’s best available departure time (block to block rest) >= restLimit thenif Minutes.minutesBetween(prevDutyPeriod.lastLeg.determineArrivalDateTime(), theDutyPeriod.firstLeg.determineDepartureDateTime()).minutes >= restLimit thenloopCounter = 0.//exit loop once a legal rest is found}loopCounter -= 1.}return legCount.
```

## Historial de cambios

```
Ben Lang - US16607 - 2/17/2015 - Initial Development
```

