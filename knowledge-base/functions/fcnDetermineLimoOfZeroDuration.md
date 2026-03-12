# fcnDetermineLimoOfZeroDuration

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnDetermineLimoOfZeroDuration`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayLeg | PayLeg | |

## Lógica de negocio

```blaze
if (thePayLeg.limoFlag = false or    (thePayLeg.limoFlag = true and fcnGetTimeDiffInMinutes(thePayLeg.determineBestDepartureDateTimeNoEstimated(), thePayLeg.determineBestArrivalDateTimeNoEstimated()) > 0)) thenreturn false.elsereturn true.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)

## Llamado por

- [fcnDutyContainsAllLimosOfZeroDuration](fcnDutyContainsAllLimosOfZeroDuration.md)
- [fcnSetTripNonDeadheadBeginEndTime](fcnSetTripNonDeadheadBeginEndTime.md)

