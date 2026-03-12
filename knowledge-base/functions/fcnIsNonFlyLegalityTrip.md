# fcnIsNonFlyLegalityTrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnIsNonFlyLegalityTrip`

## Propósito
5/23/2017 - Tim Albright - added this utility function

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aLegalityTrip | LegalityTrip | |

## Lógica de negocio

```blaze
if (aLegalityTrip <> null and aLegalityTrip.nonFlyCode <> null and aLegalityTrip.nonFlyCode.length() > 0) then {//fcnShow("===>>> EXAMINING TRIP " aLegalityTrip.tripName " with nonfly code " aLegalityTrip.nonFlyCode " returning IsNonFly = true...").return true.}else{//fcnShow("===>>> EXAMINING TRIP " aLegalityTrip.tripName " with nonfly code " aLegalityTrip.nonFlyCode " returning IsNonFly = false...").return false.}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Historial de cambios

```
5/23/2017 - Tim Albright - added this utility function
```

