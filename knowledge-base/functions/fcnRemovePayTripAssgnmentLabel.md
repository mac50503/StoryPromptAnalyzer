# fcnRemovePayTripAssgnmentLabel

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnRemovePayTripAssgnmentLabel`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
if (aPayTrip <> null) then{aPayTrip.tempAssignmentLabel = aPayTrip.assignmentLabel.aPayTrip.assignmentLabel = "".}
```

