# fcnDoAllDutyPeriodsInSpHaveRapAssociations

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDoAllDutyPeriodsInSpHaveRapAssociations`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.if (aPayTrip <> null and aPayTrip.dutyPeriodList.size() > 0) then{retVal = true.    /// DEFAULT for trips with duty periods.... for each loop test validtes this premise....for each PayDutyPeriod in aPayTrip.dutyPeriodList as an array of PayDutyPeriod do{firstLeg is some PayLeg initially null.if (it.legList.size() > 0 and it.payDutyPeriodInflight <> null) then  //// IF context{firstLeg = it.legList.get(0).if (firstLeg <> null and      fcnIsDateTimeWithinDateTimeRange(firstLeg.scheduledDepartureDateTime, aSchedulePeriodPay.schedulePeriodStart, aSchedulePeriodPay.schedulePeriodEnd) and                                                  it.payDutyPeriodInflight.rapAssociationList.size() = 0) thenretVal = false.}else //// FO context{if (it.rapAssociation = null) thenretVal = false.}}}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeWithinDateTimeRange](fcnIsDateTimeWithinDateTimeRange.md)

## Llamado por

- [fcnCalculateTripContributionForProductivityPay](fcnCalculateTripContributionForProductivityPay.md)

