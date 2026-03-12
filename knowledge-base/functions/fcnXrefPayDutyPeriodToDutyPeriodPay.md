# fcnXrefPayDutyPeriodToDutyPeriodPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnXrefPayDutyPeriodToDutyPeriodPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |
| aDutyPeriodPay | DutyPeriodPay | |

## Lógica de negocio

```blaze
if (aPayDutyPeriod <> null and aDutyPeriodPay <> null) then{aPayDutyPeriod.dutyPeriodPay = aDutyPeriodPay.aDutyPeriodPay.payDutyPeriod = aPayDutyPeriod.aDutyPeriodPay.sequenceNumber = aPayDutyPeriod.sequenceNumber.aDutyPeriodPay.creditType = aPayDutyPeriod.creditType.aDutyPeriodPay.baseCreditType = aPayDutyPeriod.creditType.if (aPayDutyPeriod.payDutyPeriodInflight <> null) then{aDutyPeriodPay.originalScheduledReportDateTime = aPayDutyPeriod.payDutyPeriodInflight.originalScheduledReportDateTime.aDutyPeriodPay.originalScheduledReleaseDateTime = aPayDutyPeriod.payDutyPeriodInflight.originalScheduledReleaseDateTime.}aDutyPeriodPay.scheduledReportDateTime = aPayDutyPeriod.scheduledReportDateTime.aDutyPeriodPay.reportDateTime = aPayDutyPeriod.reportDateTime.aDutyPeriodPay.scheduledReleaseDateTime = aPayDutyPeriod.scheduledReleaseDateTime.aDutyPeriodPay.releaseDateTime = aPayDutyPeriod.releaseDateTime.aDutyPeriodPay.rapAssociation = aPayDutyPeriod.rapAssociation.aDutyPeriodPay.basePay = aPayDutyPeriod.basePay.}
```

## Llamado por

- [fcnCreateTripPay](fcnCreateTripPay.md)

