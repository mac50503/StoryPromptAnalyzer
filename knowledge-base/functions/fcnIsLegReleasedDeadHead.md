# fcnIsLegReleasedDeadHead

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnIsLegReleasedDeadHead`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayLeg | PayLeg | |

## Lógica de negocio

```blaze
isLegReleasedDeadHead is a boolean initially false.if(thePayLeg <> nulland thePayLeg <> unknownand thePayLeg.deadHeadCode.empty = falseand thePayLeg.legWorkCodeList.contains("RS")) then {isLegReleasedDeadHead = true.}return isLegReleasedDeadHead.
```

## Llamado por

- [fcnGetLegGroundTimePay](fcnGetLegGroundTimePay.md)
- [fcnIsRedEyePayEligible](fcnIsRedEyePayEligible.md)

