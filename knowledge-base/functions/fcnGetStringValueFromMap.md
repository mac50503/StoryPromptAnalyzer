# fcnGetStringValueFromMap

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnGetStringValueFromMap`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| map | Map<String, String> | |
| key | string | |

## Lógica de negocio

```blaze
returnValue is a string initially "".if (map.containsKey(key)) then {returnValue = map.get(key).}return returnValue.
```

