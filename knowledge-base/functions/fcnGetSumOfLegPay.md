# fcnGetSumOfLegPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetSumOfLegPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriodPay | DutyPeriodPay | |
| legBasePay | boolean | |
| positionALegs | boolean | |

## Lógica de negocio

```blaze
retVal is a real initially 0.0.if (aDutyPeriodPay <> null and aDutyPeriodPay.legPayList.size() > 0) then{for each LegPay in aDutyPeriodPay.legPayList as an array of LegPay do{if ((positionALegs = true and it.positionA = true) or      (positionALegs = false and it.positionA = false)) thenif (legBasePay = true) thenretVal += it.basePay.elseretVal += it.payValue.}}return fcnRoundUpAt2DecimalPlaces(retVal).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)

## Llamado por

- [fcnCalculateDutyPeriodContributionForProductivityPay](fcnCalculateDutyPeriodContributionForProductivityPay.md)
- [fcnCalculateHolidayPayBucketFromReserve](fcnCalculateHolidayPayBucketFromReserve.md)
- [fcnCalculateTripContributionForProductivityPay](fcnCalculateTripContributionForProductivityPay.md)
- [fcnShowTripPaySummary](fcnShowTripPaySummary.md)

