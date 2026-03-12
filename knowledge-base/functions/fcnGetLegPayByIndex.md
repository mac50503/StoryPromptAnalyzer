# fcnGetLegPayByIndex

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetLegPayByIndex`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLegPayList | List<LegPay> | |
| index | integer | |

## Lógica de negocio

```blaze
if (theLegPayList.size() is greater than or equal to (index +1)) then return theLegPayList.get(index).elsereturn null.
```

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

