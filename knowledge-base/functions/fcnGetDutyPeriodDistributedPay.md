# fcnGetDutyPeriodDistributedPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetDutyPeriodDistributedPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSchedulePeriodPay | SchedulePeriodPay | |
| theTripSequenceNumber | integer | |
| theDutyPeriodSequenceNumber | integer | |

## Lógica de negocio

```blaze
if (theSchedulePeriodPay <> null and theSchedulePeriodPay <> unknown) thenfor each TripPay in theSchedulePeriodPay.tripPayList as an array of TripPay doif it.sequenceNumber = theTripSequenceNumber thenfor each DutyPeriodPay in it.dutyPeriodPayList as an array of DutyPeriodPay doif it.sequenceNumber = theDutyPeriodSequenceNumber thenreturn it.distributedPay.return 0.0.
```

