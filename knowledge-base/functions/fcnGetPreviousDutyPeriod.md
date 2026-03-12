# fcnGetPreviousDutyPeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegalityDutyPeriod
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnGetPreviousDutyPeriod`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriodList | List<LegalityDutyPeriod> | |
| theDutyPeriodCounter | integer | |

## Lógica de negocio

```blaze
tempDutyPeriod is some LegalityDutyPeriod initially null.if (theDutyPeriodCounter > 0 and theDutyPeriodList <> null and theDutyPeriodList.size() > 0) then tempDutyPeriod = theDutyPeriodList.get(theDutyPeriodCounter-1).return tempDutyPeriod
```

