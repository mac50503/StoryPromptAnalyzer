# fcnIsPremiumCodeChangeNeeded

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnIsPremiumCodeChangeNeeded`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| anyPayLeg | PayLeg | |
| theTrip | PayTrip | |
| premiumMultiplierValue | real | |

## Lógica de negocio

```blaze
premiumCodeChangeNeeded is a boolean initially false;if ((anyPayLeg.legWorkCodeList.contains("CT") = false)     and (((theTrip.assignmentLabel = "E") and (premiumMultiplierValue > 2.0)) or ((theTrip.assignmentLabel = ("J" or "U" or "V" or "S")) and (premiumMultiplierValue > 1.5)))    and (fcnDetermineAnyRigsWinning(anyPayLeg))) then {premiumCodeChangeNeeded = true;}return premiumCodeChangeNeeded;
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDetermineAnyRigsWinning](fcnDetermineAnyRigsWinning.md)

