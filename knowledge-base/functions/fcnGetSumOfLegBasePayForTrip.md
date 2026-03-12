# fcnGetSumOfLegBasePayForTrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetSumOfLegBasePayForTrip`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
retVal is a real initially 0.0.if (aPayTrip <> null and aPayTrip.dutyPeriodList <> null and aPayTrip.dutyPeriodList.size() > 0) then{for each PayDutyPeriod in aPayTrip.dutyPeriodList as an array of PayDutyPeriod do{for each PayLeg in it.legList as an array of PayLeg do{retVal += it.basePay.}}}return fcnRoundUpAt2DecimalPlaces(retVal).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)

## Llamado por

- [fcnCalculateTripContributionForProductivityPay](fcnCalculateTripContributionForProductivityPay.md)
- [fcnShowTripPaySummary](fcnShowTripPaySummary.md)

