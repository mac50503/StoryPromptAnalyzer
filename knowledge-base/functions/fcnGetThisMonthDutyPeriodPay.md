# fcnGetThisMonthDutyPeriodPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetThisMonthDutyPeriodPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
retVal is a real initially 0.0.if (aTripPay <> null and aSchedulePeriodPay <> null) then{for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do{if (fcnDoesDutyPeriodPayBeginInSchedulePeriodPay(it, aSchedulePeriodPay)) thenretVal += it.payValue.}}return fcnRoundUpAt2DecimalPlaces(retVal).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDoesDutyPeriodPayBeginInSchedulePeriodPay](fcnDoesDutyPeriodPayBeginInSchedulePeriodPay.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)

