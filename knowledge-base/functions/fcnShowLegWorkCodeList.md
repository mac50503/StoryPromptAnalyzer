# fcnShowLegWorkCodeList

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnShowLegWorkCodeList`

## Propósito
US18085 - Melissa S - 7/29/2014 - Refactored for performance  - Added check for debugMode to avoid looping if not in debugMode

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |

## Lógica de negocio

```blaze
if (debugMode) then {if (aPayLeg <> null) then {if (aPayLeg.legWorkCodeList = null or aPayLeg.legWorkCodeList.size() = 0) thenfcnShow("PayLeg " aPayLeg.sequenceNumber " contains no leg work codes:").else {fcnShow("PayLeg " aPayLeg.sequenceNumber " contains leg work codes:"). for each string in aPayLeg.legWorkCodeList as an array of String do{fcnShow("..........work code: " it). }}}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Llamado por

- [fcnRemovePremiumLegWorkCodes](fcnRemovePremiumLegWorkCodes.md)
- [fcnRestorePremiumLegWorkCodes](fcnRestorePremiumLegWorkCodes.md)

## Historial de cambios

```
US18085 - Melissa S - 7/29/2014 - Refactored for performance  - Added check for debugMode to avoid looping if not in debugMode
```

