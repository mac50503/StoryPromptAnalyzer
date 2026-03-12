# fcnGetNonRONpremium

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetNonRONpremium`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
retVal is a real initially 0.0.if (aTripPay <> null and aTripPay.dutyPeriodPayList.size() > 0) then{aSchedulePeriodPay is some SchedulePeriodPay initially fcnGetSchedulePeriodPayInScope(aTripPay). if (aSchedulePeriodPay <> null) then{for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do{if (it.payDutyPeriod.dutyType <> "RON" and fcnDoesDutyPeriodPayBeginInSchedulePeriodPay(it, aSchedulePeriodPay)) thenretVal += it.sumLegPremiumCredits.}}}return fcnRoundUpAt2DecimalPlaces(retVal).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDoesDutyPeriodPayBeginInSchedulePeriodPay](fcnDoesDutyPeriodPayBeginInSchedulePeriodPay.md)
- [fcnGetSchedulePeriodPayInScope](fcnGetSchedulePeriodPayInScope.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)

## Llamado por

- [fcnShowTripPaySummary](fcnShowTripPaySummary.md)

