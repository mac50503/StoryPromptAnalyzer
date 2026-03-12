# fcnGetPayTrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayTrip
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetPayTrip`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayTripList | List<PayTrip> | |
| theTripCounter | integer | |

## Lógica de negocio

```blaze
return thePayTripList.get(theTripCounter).
```

