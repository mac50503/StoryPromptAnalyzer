# fcnGetNonRONDutyPeriodBasePay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetNonRONDutyPeriodBasePay`

## Propósito
Ben Lang DE6680 06/10/2015 - Returns the sum of non RON duty periods

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
retVal is a real initially 0.0.if (aTripPay <> null and aTripPay.dutyPeriodPayList.size() > 0) then{aSchedulePeriodPay is some SchedulePeriodPay initially fcnGetSchedulePeriodPayInScope(aTripPay). if (aSchedulePeriodPay <> null) then{for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do{if (it.payDutyPeriod.dutyType <> "RON") then retVal += it.basePay.}}}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetSchedulePeriodPayInScope](fcnGetSchedulePeriodPayInScope.md)

## Historial de cambios

```
Ben Lang DE6680 06/10/2015 - Returns the sum of non RON duty periods
7/7/2015 - Melissa S - DE6931 - Removed check for being in the same schedule period
```

