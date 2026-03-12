# fcnGetTripPayByIndex

## Metadata
- **Tipo**: SRL Function
- **Retorna**: TripPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetTripPayByIndex`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripPayList | List<TripPay> | |
| index | integer | |

## Lógica de negocio

```blaze
if (theTripPayList is not equal to null and theTripPayList.size() is greater than or equal to (index +1)) then return theTripPayList.get(index).elsereturn null.
```

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

