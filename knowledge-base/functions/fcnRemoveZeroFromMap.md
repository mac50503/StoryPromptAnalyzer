# fcnRemoveZeroFromMap

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnRmZeroElementsFromMap`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| map | Map<String, Double> | |

## Lógica de negocio

```blaze
if (map is not null) then { for each string in map.keySet() as an array of string do { if (map.get(it) = Double.valueOf(0.0)) then {map.remove(it).}}}
```

