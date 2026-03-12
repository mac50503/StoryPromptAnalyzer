# fcnRestoreAllPayTripAssignmentLabels

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnRestoreAllPayTripAssignmentLabels`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripList | List<PayTrip> | |

## Lógica de negocio

```blaze
if (aTripList <> null and aTripList.size() > 0) then{for each PayTrip in aTripList as an array of PayTrip do fcnRestorePayTripAssignmentLabel(it).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnRestorePayTripAssignmentLabel](fcnRestorePayTripAssignmentLabel.md)

