# fcnAssignAssignment

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegalityTrip
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnAssignAssignment`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theAssignments | List<LegalityTrip> | |
| counter | integer | |

## Lógica de negocio

```blaze
return theAssignments.get(counter).
```

