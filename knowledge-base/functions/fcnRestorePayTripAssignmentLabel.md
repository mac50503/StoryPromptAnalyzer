# fcnRestorePayTripAssignmentLabel

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnRestorePayTripAssignmentLabel`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
if (aPayTrip <> null) thenaPayTrip.assignmentLabel = aPayTrip.tempAssignmentLabel.
```

## Llamado por

- [fcnRestoreAllPayTripAssignmentLabels](fcnRestoreAllPayTripAssignmentLabels.md)

