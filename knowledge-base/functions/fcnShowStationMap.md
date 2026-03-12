# fcnShowStationMap

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnShowStationMap`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aGlobalDataCache | GlobalDataCache | |

## Lógica de negocio

```blaze
if (aGlobalDataCache <> null) then{if (aGlobalDataCache.stationMap <> null) then{for each string in aGlobalDataCache.stationMap.keySet() as an array of string do{fcnShow("===> GDC station map contains station: " it).}}elsefcnShow("===>>> stationMap is null...").}elsefcnShow("===>>> aGlobalDataCache is null...").
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

