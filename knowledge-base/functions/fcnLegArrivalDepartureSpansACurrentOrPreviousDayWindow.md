# fcnLegArrivalDepartureSpansACurrentOrPreviousDayWindow

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\isLegNonStop`

## Propósito
01/27/2016 CSCH-375 Matt C - Initial development -  Utility function for determining if a legdeparture and arrival spans a current/previous day window

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aLocalStartTime | LocalTime | |
| aLocalEndTime | LocalTime | |
| aLegDepartureTime | DateTime | |
| aLegArrivalTime | DateTime | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.if (aLocalStartTime > aLocalEndTime) then {  //previous day startif (aLegDepartureTime.toLocalDate() <aLegArrivalTime.toLocalDate() and aLegArrivalTime.toLocalTime() >= aLocalEndTime and aLegDepartureTime.toLocalTime() < aLocalStartTime) then {//fcnShow("VIOLATION! Span - previous day start: " aLegDepartureTime.toLocalTime() " " aLegArrivalTime.toLocalTime() as a string).retVal = true.    } } else if (aLocalStartTime < aLocalEndTime) then {if (aLegDepartureTime.toLocalTime() <= aLocalStartTime and aLegArrivalTime.toLocalTime() > aLocalEndTime) then {//fcnShow("VIOLATION! Span - current day start: " aLegDepartureTime.toLocalTime() " " aLegArrivalTime.toLocalTime() as a string).retVal = true.               }} return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Llamado por

- [fcnDutyHasNightFlightLeg](fcnDutyHasNightFlightLeg.md)

## Historial de cambios

```
01/27/2016 CSCH-375 Matt C - Initial development -  Utility function for determining if a legdeparture and arrival spans a current/previous day window
```

