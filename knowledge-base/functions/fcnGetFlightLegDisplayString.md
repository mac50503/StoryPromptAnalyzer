# fcnGetFlightLegDisplayString

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetFlightLegDisplayString`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |

## Lógica de negocio

```blaze
retVal is a string initially "".if (aPayLeg <> null) thenretVal = aPayLeg.flightNumber " departing from " aPayLeg.departureLocation " at " DateTimeUtilities.getShortDateTimeString(aPayLeg.determineBestDepartureDateTimeNoEstimated()).return retVal.
```

## Llamado por

- [fcnDetermineMileage](fcnDetermineMileage.md)
- [fcnDetermineOverfly](fcnDetermineOverfly.md)
- [fcnDetermineOverschedule](fcnDetermineOverschedule.md)
- [fcnGetRegularPayForLegInForcedDutyPeriod](fcnGetRegularPayForLegInForcedDutyPeriod.md)

