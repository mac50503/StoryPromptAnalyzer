# fcnGetMaxDutyAfterReducedRestList

## Metadata
- **Tipo**: SRL Function
- **Retorna**: List<MaxDutyAfterReducedRest>
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnGetMaxDutyAfterReducedRestList`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theMaxDutyAfterReducedRestList | List<MaxDutyAfterReducedRest> | |

## Lógica de negocio

```blaze
aMaxDutyAfterReducedRestList is some List<MaxDutyAfterReducedRest> initially an ArrayList.if (theMaxDutyAfterReducedRestList is not equal to null) thenreturn theMaxDutyAfterReducedRestList.elsereturn aMaxDutyAfterReducedRestList.
```

