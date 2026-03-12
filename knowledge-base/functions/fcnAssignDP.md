# fcnAssignDP

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegalityDutyPeriod
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnAssignDP`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDPs | List<LegalityDutyPeriod> | |
| counter | integer | |

## Lógica de negocio

```blaze
return theDPs.get(counter).
```

