# fcnAssignLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegalityLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnAssignLeg`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLegs | List<LegalityLeg> | |
| counter | integer | |

## Lógica de negocio

```blaze
return theLegs.get(counter).
```

