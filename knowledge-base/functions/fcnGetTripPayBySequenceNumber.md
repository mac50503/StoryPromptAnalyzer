# fcnGetTripPayBySequenceNumber

## Metadata
- **Tipo**: SRL Function
- **Retorna**: TripPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetTripPayBySequenceNumber`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| seqNum | integer | |
| tripPayList | List<TripPay> | |

## Lógica de negocio

```blaze
index is an integer initially 0.if (tripPayList<>null) then {while (index < tripPayList.size()) do {    if (tripPayList.get(index).sequenceNumber is equal to seqNum) then {return tripPayList.get(index).}index += 1.}}return null.
```

## Llamado por

- [fcnDistributeToPerDiemBuckets](fcnDistributeToPerDiemBuckets.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

