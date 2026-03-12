# fcnIsNonFlyLegalityLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnIsNonFlyLegalityLeg`

## Propósito
5/23/2017 - Tim Albright - added this utility function

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aLegalityLeg | LegalityLeg | |

## Lógica de negocio

```blaze
if (aLegalityLeg <> null and aLegalityLeg.nonFlyCode <> null and aLegalityLeg.nonFlyCode.length() > 0) then return true.elsereturn false.
```

## Historial de cambios

```
5/23/2017 - Tim Albright - added this utility function
```

