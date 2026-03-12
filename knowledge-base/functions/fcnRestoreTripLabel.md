# fcnRestoreTripLabel

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnRestoreTripLabel`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
if (aPayTrip <> null) then{aPayTrip.assignmentLabel = aPayTrip.tempAssignmentLabel.if (aPayTrip.tripPay <> null) thenaPayTrip.tripPay.assignmentLabel = aPayTrip.assignmentLabel.}
```

