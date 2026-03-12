# fcnGetPayTripByIndex

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayTrip
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetPayTripByIndex`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayTripList | List<PayTrip> | |
| index | integer | |

## Lógica de negocio

```blaze
if (thePayTripList is not equal to null) then {if (thePayTripList.size() is greater than or equal to (index +1)) then return thePayTripList.get(index).}return null.
```

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

