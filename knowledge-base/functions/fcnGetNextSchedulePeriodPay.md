# fcnGetNextSchedulePeriodPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: SchedulePeriodPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetNextSchedulePeriodPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| currentSchedulePeriodPay | SchedulePeriodPay | |
| schedulePeriodPayList | List<SchedulePeriodPay> | |

## Lógica de negocio

```blaze
count is an integer initially schedulePeriodPayList.size().if (currentSchedulePeriodPay <> null and schedulePeriodPayList <> null and count > 1) then{currentIndex is an integer initially schedulePeriodPayList.indexOf(currentSchedulePeriodPay).if (currentIndex < count -1) then{return schedulePeriodPayList.get(currentIndex + 1).}}return null.
```

