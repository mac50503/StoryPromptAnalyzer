# fcnGetPayTripBySequenceNumber

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayTrip
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetPayTripBySequenceNumber`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| seqNum | integer | |
| payTripList | List<PayTrip> | |

## Lógica de negocio

```blaze
for each PayTrip in payTripList as an array of PayTrip do {if (it.sequenceNumber is equal to seqNum) thenreturn it.}return null.
```

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

