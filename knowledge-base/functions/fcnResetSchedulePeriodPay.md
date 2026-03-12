# fcnResetSchedulePeriodPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnResetSchedulePeriodPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
if (aSchedulePeriodPay <> null) then{aSchedulePeriodPay.ojiBucket= 0.0.aSchedulePeriodPay.ojcBucket = 0.0.aSchedulePeriodPay.otrBucket = 0.0.aSchedulePeriodPay.otcBucket = 0.0.aSchedulePeriodPay.perBucket = 0.0.aSchedulePeriodPay.regBucket = 0.0.aSchedulePeriodPay.pecBucket = 0.0.aSchedulePeriodPay.rgcBucket = 0.0.aSchedulePeriodPay.sckBucket = 0.0.aSchedulePeriodPay.skcBucket = 0.0.aSchedulePeriodPay.trnBucket = 0.0.aSchedulePeriodPay.trcBucket = 0.0.aSchedulePeriodPay.ubBucket = 0.0.aSchedulePeriodPay.ubcBucket = 0.0.aSchedulePeriodPay.vacBucket = 0.0.aSchedulePeriodPay.jaBucket = 0.0.aSchedulePeriodPay.jacBucket = 0.0.aSchedulePeriodPay.pp1Bucket= 0.0.aSchedulePeriodPay.pp2Bucket = 0.0.aSchedulePeriodPay.pp3Bucket = 0.0.aSchedulePeriodPay.pi1Bucket = 0.0.aSchedulePeriodPay.pi2Bucket = 0.0.aSchedulePeriodPay.pi3Bucket = 0.0.aSchedulePeriodPay.reserveGuaranty = 0.0.aSchedulePeriodPay.remainingReserveGuaranty = 0.0.aSchedulePeriodPay.reserveProjectedTotal = 0.0.aSchedulePeriodPay.projectedCredit = 0.0.aSchedulePeriodPay.totalBucket = 0.0.aSchedulePeriodPay.totalPayTripsBucket= 0.0.aSchedulePeriodPay.monthToDateCredit = 0.0.aSchedulePeriodPay.accruedOji = 0.0.aSchedulePeriodPay.accruedSick = 0.0.aSchedulePeriodPay.earnedOji = 0.0.aSchedulePeriodPay.usedOji = 0.0.aSchedulePeriodPay.adjustmentOji= 0.0.aSchedulePeriodPay.remainingOji = 0.0.aSchedulePeriodPay.earnedSick = 0.0.aSchedulePeriodPay.usedSick = 0.0.aSchedulePeriodPay.adjustmentSick = 0.0.aSchedulePeriodPay.remainingSick = 0.0.aSchedulePeriodPay.reserveTotal = 0.0.aSchedulePeriodPay.jLabelCredits = 0.0.//---------------------------------------------------------------------------------------------------------------------------//for each TripSet in aSchedulePeriodPay.tripSetList as an array of TripSet do//{//it.currentConusLimit = 0;//it.currentOconusLimit = 0;//}//---------------------------------------------------------------------------------------------------------------------------//Replacing the above code with the following logic, since a SchedulePeriodPay might not contain a TripSet but still contain the trip which belongs to that TripSet, //and since setting of conus/oconus per diem limit  uses payTrip.tripSet, we need to reset the TripSet for each payTrip in a schedulePeriod.for each TripPay in aSchedulePeriodPay.tripPayList as an array of TripPay do{if(it.payTrip<>null and it.payTrip.tripSet<>null)then{it.payTrip.tripSet.currentConusLimit = 0;it.payTrip.tripSet.currentOconusLimit = 0;}}for each TripPay in aSchedulePeriodPay.tripPayList as an array of TripPay do {it.amReserveCredit = 0.0;if (it.dutyPeriodPayList <> null and it.dutyPeriodPayList.size() > 0) then{for each DutyPeriodPay in it.dutyPeriodPayList  as an array of DutyPeriodPay doit.tripExcess = 0.0.} }}
```

## Dependencias

Esta function llama a:

- [main](main.md)

