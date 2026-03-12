# fcnLegArrivesDepartsWithinACurrentOrPreviousDayWindow

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnIsLegWithinDutyWindow`

## Propósito
01/27/2016 CSCH-375 Matt C - Initial development -  Utility function for determining if a leg departs or arrives within a current/previous day window

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aLocalStartTime | LocalTime | |
| aLocalEndTime | LocalTime | |
| aLegTime | LocalTime | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.if (aLocalStartTime > aLocalEndTime) then { //previous day if (aLegTime >= aLocalStartTime or aLegTime <= aLocalEndTime) then {retVal = true.    } } else if (aLocalStartTime < aLocalEndTime) then {    //current day if (aLegTime >= aLocalStartTime and aLegTime <= aLocalEndTime) then {retVal = true.               }    } return retVal.
```

## Llamado por

- [fcnDutyHasNightFlightLeg](fcnDutyHasNightFlightLeg.md)

## Historial de cambios

```
01/27/2016 CSCH-375 Matt C - Initial development -  Utility function for determining if a leg departs or arrives within a current/previous day window
```

