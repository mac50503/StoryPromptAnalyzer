# fcnGetNextDutyPeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegalityDutyPeriod
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnGetNextDutyPeriod`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriodList | List<LegalityDutyPeriod> | |
| theDutyPeriodIndex | integer | |

## Lógica de negocio

```blaze
if (theDutyPeriodIndex < theDutyPeriodList.size() - 1) then {return theDutyPeriodList.get(theDutyPeriodIndex + 1).} else return null.
```

