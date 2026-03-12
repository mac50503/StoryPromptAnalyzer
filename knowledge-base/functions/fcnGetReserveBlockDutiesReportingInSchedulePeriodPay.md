# fcnGetReserveBlockDutiesReportingInSchedulePeriodPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: List<DutyPeriodPay>
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetReserveBlockDutiesReportingInSchedulePeriodPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
dutyPeriodPayList is an ArrayList.if (aSchedulePeriodPay <> null and aSchedulePeriodPay.tripPayList <> null and aSchedulePeriodPay.tripPayList.size() > 0) then{aTripPay is some TripPay initially null.aDutyPeriodPay is some DutyPeriodPay initially null.for each TripPay in aSchedulePeriodPay.tripPayList as an array of TripPay do{aTripPay = it.for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do{aDutyPeriodPay = it.if (aTripPay.tripType =(ignoring case) "R" and fcnDoesDutyPeriodPayBeginInSchedulePeriodPay(aDutyPeriodPay, aSchedulePeriodPay)) thendutyPeriodPayList.add(aDutyPeriodPay).}}}//fcnShow("===>>> RETURNING from function fcnGetReserveBlockDutiesReportingInSchedulePeriodPay ... " dutyPeriodPayList.size() " reserve duty periods in SP " aSchedulePeriodPay.schedulePeriodName).return dutyPeriodPayList.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDoesDutyPeriodPayBeginInSchedulePeriodPay](fcnDoesDutyPeriodPayBeginInSchedulePeriodPay.md)
- `fcnShow()`

## Llamado por

- [fcnDistributeRemainingReserveGuarantee](fcnDistributeRemainingReserveGuarantee.md)

