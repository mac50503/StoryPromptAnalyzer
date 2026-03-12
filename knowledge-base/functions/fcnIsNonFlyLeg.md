# fcnIsNonFlyLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnIsNonFlyLeg`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |

## Lógica de negocio

```blaze
if (aPayLeg <> null and aPayLeg.nonFlyCode <> null and aPayLeg.nonFlyCode.length() > 0) then return true.elsereturn false.
```

## Llamado por

- [fcnCalculateTripHourlyRatio](fcnCalculateTripHourlyRatio.md)

