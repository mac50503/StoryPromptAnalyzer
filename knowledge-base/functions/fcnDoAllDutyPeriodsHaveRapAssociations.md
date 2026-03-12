# fcnDoAllDutyPeriodsHaveRapAssociations

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDoAllDutyPeriodsHaveRapAssociations`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.if (aPayTrip <> null and aPayTrip.dutyPeriodList.size() > 0) then{retVal = true.    /// DEFAULT for trips with duty periods.... for each loop test validtes this premise....for each PayDutyPeriod in aPayTrip.dutyPeriodList as an array of PayDutyPeriod do{if (it.payDutyPeriodInflight <> null) then  //// IF context{if (it.payDutyPeriodInflight.rapAssociationList.size() = 0) thenretVal = false.}else //// FO context{if (it.rapAssociation = null) thenretVal = false.}}}return retVal.
```

## Llamado por

- [fcnCalculateTripContributionForProductivityPay](fcnCalculateTripContributionForProductivityPay.md)

