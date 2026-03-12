# fcnGetLastDutyPeriodPayForFirstTripSpanningIntoSchedulePeriodPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DutyPeriodPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetLastDutyPeriodPayForFirstTripSpanningIntoSchedulePeriodPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
retVal is some DutyPeriodPay initially null.if (aSchedulePeriodPay <> null and aSchedulePeriodPay.tripPayList <> null and aSchedulePeriodPay.tripPayList.size() > 0) then{firstTripPay is some TripPay initially aSchedulePeriodPay.tripPayList.get(0).if (firstTripPay <> null and    firstTripPay.startsInSchedulePeriod <> aSchedulePeriodPay.schedulePeriodName and    firstTripPay.startSchedulePeriodPay <> aSchedulePeriodPay and     firstTripPay.dutyPeriodPayList <> null and     firstTripPay.dutyPeriodPayList.size() > 0) then{if (firstTripPay <> null) thenretVal = firstTripPay.dutyPeriodPayList.get(firstTripPay.dutyPeriodPayList.size() - 1).}}if retVal <> null thenfcnShow("===>>> SP = " aSchedulePeriodPay.schedulePeriodName " ...returning carry-in duty period " retVal.sequenceNumber " ... trip excess = " retVal.tripExcess).elsefcnShow("===>>> SP = " aSchedulePeriodPay.schedulePeriodName " ...returning NULL for carry-in duty period...").return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

