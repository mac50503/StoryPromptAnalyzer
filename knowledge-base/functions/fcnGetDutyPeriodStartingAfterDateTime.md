# fcnGetDutyPeriodStartingAfterDateTime

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayDutyPeriod
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetDutyPeriodStartingAfterDateTime`

## Propósito
US18085 - Melissa S - 7/29/2014 - Refactored for performance

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripSet | TripSet | |
| theDateTime | DateTime | |

## Lógica de negocio

```blaze
theTripCounter is an integer initially 0.theDutyCounter is an integer.aPayTrip is some PayTrip initially null.aDutyPeriod is some PayDutyPeriod initially null.while (theTripCounter < theTripSet.payTripList.size()) do {aPayTrip = theTripSet.payTripList.get(theTripCounter).theDutyCounter = 0.while (theDutyCounter < aPayTrip.dutyPeriodList.size()) do {aDutyPeriod = aPayTrip.dutyPeriodList.get(theDutyCounter).if (aDutyPeriod.reportDateTime.isAfter(theDateTime)) then return aDutyPeriod.theDutyCounter +=1.}theTripCounter +=1.}return theTripSet.payTripList.get(theTripCounter - 1).dutyPeriodList.get(theDutyCounter - 1).
```

## Llamado por

- [fcnSetTripSetConusAndOconusDays](fcnSetTripSetConusAndOconusDays.md)

## Historial de cambios

```
US18085 - Melissa S - 7/29/2014 - Refactored for performance
```

