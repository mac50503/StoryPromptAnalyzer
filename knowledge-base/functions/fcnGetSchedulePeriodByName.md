# fcnGetSchedulePeriodByName

## Metadata
- **Tipo**: SRL Function
- **Retorna**: SchedulePeriod
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnGetSchedulePeriodByName`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aSchedulePeriodList | List<SchedulePeriod> | |
| name | string | |

## Lógica de negocio

```blaze
if (aSchedulePeriodList is not equal to null and aSchedulePeriodList.size() > 0) then{for each SchedulePeriod in aSchedulePeriodList  as an array of SchedulePeriod do {    if (it.schedulePeriodName is equal to name) then        return it.}}return null.
```

