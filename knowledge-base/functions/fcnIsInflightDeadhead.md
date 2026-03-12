# fcnIsInflightDeadhead

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnIsInflightDeadhead`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.if (aPayLeg <> null and     (aPayLeg.deadHeadCode.contains("DH") or        aPayLeg.deadHeadCode.contains("DM") or       aPayLeg.deadHeadCode.contains("NM") or       aPayLeg.deadHeadCode.contains("DP") or      aPayLeg.deadHeadCode.contains("NP"))) thenretVal = true.return retVal.
```

## Llamado por

- [fcnCreateTripPayInflightAnalytics](fcnCreateTripPayInflightAnalytics.md)

