# fcnGetPayLegByIndex

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetPayLegByIndex`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayLegList | List<PayLeg> | |
| index | integer | |

## Lógica de negocio

```blaze
if (thePayLegList.size() is greater than or equal to (index +1)) thenreturn thePayLegList.get(index).elsereturn null.
```

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

