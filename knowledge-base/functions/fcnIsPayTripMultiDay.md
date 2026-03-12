# fcnIsPayTripMultiDay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnIsPayTripMultiDay`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
if (aPayTrip <> null) then {if (fcnIsSameSwaDay(aPayTrip.beginDateTime, aPayTrip.endDateTime) = false) thenreturn true.}return false.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsSameSwaDay](fcnIsSameSwaDay.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

