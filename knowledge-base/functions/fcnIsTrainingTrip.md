# fcnIsTrainingTrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnIsTrainingTrip`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
if (aPayTrip <> null and    ((aPayTrip.tripType = "T" or aPayTrip.assignmentLabel = "T") or     (aPayTrip.tripType = "N" or aPayTrip.assignmentLabel = "N") or     (aPayTrip.tripType = "I" or aPayTrip.assignmentLabel = "I"))) thenreturn true.elsereturn false.
```

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

