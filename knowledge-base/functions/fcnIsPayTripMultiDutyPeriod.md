# fcnIsPayTripMultiDutyPeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnIsPayTripMultiDutyPeriod`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
if (aPayTrip <> null and     aPayTrip.dutyPeriodList <> null and     aPayTrip.dutyPeriodList.size() > 1) then {return true.} else {return false.}
```

## Llamado por

- [fcnCreateInflightTripSets](fcnCreateInflightTripSets.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

