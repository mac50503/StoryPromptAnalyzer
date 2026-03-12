# fcnAssignLegalitySchedulePeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegalitySchedulePeriod
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnAssignLegalitySchedulePeriod`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSchedulePeriodList | List<LegalitySchedulePeriod> | |
| schedulePeriodCounter | integer | |

## Lógica de negocio

```blaze
return theSchedulePeriodList.get(schedulePeriodCounter);
```

