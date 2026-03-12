# fcnGetPreviousSchedulePeriodPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: SchedulePeriodPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetPreviousSchedulePeriodPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| currentSchedulePeriodPay | SchedulePeriodPay | |
| schedulePeriodPayList | List<SchedulePeriodPay> | |

## Lógica de negocio

```blaze
if (currentSchedulePeriodPay <> null and schedulePeriodPayList <> null and schedulePeriodPayList.size() > 1) then{currentIndex is an integer initially schedulePeriodPayList.indexOf(currentSchedulePeriodPay).if (currentIndex > 0) then{return schedulePeriodPayList.get(currentIndex - 1).}}return null.
```

