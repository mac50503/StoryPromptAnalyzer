# fcnGetLegPayFromPayLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetLegPayFromPayLeg`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |

## Lógica de negocio

```blaze
if (aPayLeg <> null) thenreturn aPayLeg.legPay.elsereturn null.
```

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

