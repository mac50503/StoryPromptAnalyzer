# fcnGetTripPayFromPayTrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: TripPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetTripPayFromPayTrip`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
if (aPayTrip <> null) thenreturn aPayTrip.tripPay.elsereturn null.
```

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

