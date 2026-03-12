# fcnGetMaxDutyAfterReducedRestByIndex

## Metadata
- **Tipo**: SRL Function
- **Retorna**: MaxDutyAfterReducedRest
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnGetMaxDutyAfterReducedRestByIndex`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theMaxDutyAfterReducedRestList | List<MaxDutyAfterReducedRest> | |
| index | integer | |

## Lógica de negocio

```blaze
if (theMaxDutyAfterReducedRestList.size() is greater than or equal to (index + 1)) thenreturn theMaxDutyAfterReducedRestList.get(index).elsereturn null.
```

