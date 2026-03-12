# fcnGetValueFromMap

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnGetValueFromMap`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| map | Map<String, Double> | |
| key | string | |

## Lógica de negocio

```blaze
returnValue is a real initially 0.0.if (map.containsKey(key)) then {returnValue = map.get(key).}return returnValue.
```

