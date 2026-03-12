# fcnRemoveInflightFilteredDataAnalytics

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnRemoveInflightFilteredDataAnalytics`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriodPay | DutyPeriodPay | |

## Lógica de negocio

```blaze
if(theDutyPeriodPay <> null and theDutyPeriodPay.dutyPeriodPayInflightAnalytics <> null) then{theDutyPeriodPay.dutyPeriodPayInflightAnalytics.filteredDataAnalytics = null.}
```

