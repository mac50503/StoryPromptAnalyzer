# fcnGetPlnPayTripByIndex

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PlnPayTrip
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\PlanningPay\Functions\fcnGetPlnPayTripByIndex`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayTripList | List<PlnPayTrip> | |
| index | integer | |

## Lógica de negocio

```blaze
if (thePayTripList is not equal to null) then {if (thePayTripList.size() is greater than or equal to (index +1)) then return thePayTripList.get(index).}return null.
```

