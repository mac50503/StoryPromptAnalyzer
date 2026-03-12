# fcnIsTripForcedToZero

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnIsTripForcedToZero`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.if (aPayTrip <> null and aPayTrip.creditType <> null and aPayTrip.creditType = "F" and aPayTrip.basePay = 0.0) thenretVal = true.return retVal.
```

