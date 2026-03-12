# fcnPopulateSchedulePeriodPayList

## Metadata
- **Tipo**: SRL Function
- **Retorna**: List<SchedulePeriodPay>
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnPopulateSchedulePeriodPayList`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aSchedulePeriodList | List<SchedulePeriod> | |

## Lógica de negocio

```blaze
retVal is some List<SchedulePeriodPay> initially an ArrayList.aSchedulePeriodPay is some SchedulePeriodPay initially null.if (aSchedulePeriodList <> null and aSchedulePeriodList.size() > 0) then{for each SchedulePeriod in aSchedulePeriodList as an array of SchedulePeriod do{aSchedulePeriodPay = it.schedulePeriodPay.if (aSchedulePeriodPay <> null) thenretVal.add(aSchedulePeriodPay).}}return retVal.
```

