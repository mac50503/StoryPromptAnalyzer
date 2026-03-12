# fcnGetPlnLegPayByIndex

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PlnLegPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\PlanningPay\Functions\fcnGetPlnLegPayByIndex`

## Propósito
1/19/2016 - Ben L.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLegPayList | List<PlnLegPay> | |
| index | integer | |

## Lógica de negocio

```blaze
if (theLegPayList.size() is greater than or equal to (index +1)) then return theLegPayList.get(index).elsereturn null.
```

## Historial de cambios

```
1/19/2016 - Ben L.
```

