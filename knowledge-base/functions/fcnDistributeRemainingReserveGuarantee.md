# fcnDistributeRemainingReserveGuarantee

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnDistributeRemainingReserveGuarantee`

## Propósito
Ben Lang - US18452 - 10/09/2014 - This function adds up the remaining reserve guarantee and than put that into the remaining reserve guarantee property on the SchedulePeriodPay object&gt; Then add that value to the REG bucket.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
fcnShow("===>>> ENTERING fcnDistributeRemainingReserveGuarantee").fcnShow("===>>> unutilizedReserveTfpCreditedTotal = " aSchedulePeriodPay.schedulePeriodPayInflight.totalUnutilizedReserveTfpCredited).fcnShow("===>>> monthlyGuaranteeCreditedTotal = " aSchedulePeriodPay.schedulePeriodPayInflight.totalMonthlyGuaranteeCredited).fcnShow("===>>> singleDayGuaranteeCreditedTotal = " aSchedulePeriodPay.schedulePeriodPayInflight.totalSingleDayGuaranteeCredited).count is an integer initially 0.aReserveMultiDaySection is some ReserveMultiDaySection initially null.aDutyPeriodPay is some DutyPeriodPay initially null.for each ReserveMultiDaySection in aSchedulePeriodPay.schedulePeriodPayInflight.reserveMultiDaySectionList as an array of ReserveMultiDaySection do{count += 1.fcnShow("===>>>  ReserveMutiDaySection " count ", MultiDayGuarantee = "  it.multiDayGuarantee ",  MultiDayTfpCredited = " it.multiDayTfpCredited ", MultiDayGuaranteeCredited = "  it.multiDayGuaranteeCredited). }aSchedulePeriodPay.remainingReserveGuaranty += aSchedulePeriodPay.schedulePeriodPayInflight.totalUnutilizedReserveTfpCredited.aSchedulePeriodPay.remainingReserveGuaranty += aSchedulePeriodPay.schedulePeriodPayInflight.totalSingleDayGuaranteeCredited.aSchedulePeriodPay.remainingReserveGuaranty += aSchedulePeriodPay.schedulePeriodPayInflight.totalMonthlyGuaranteeCredited.for each ReserveMultiDaySection in aSchedulePeriodPay.schedulePeriodPayInflight.reserveMultiDaySectionList as an array of ReserveMultiDaySection do{aSchedulePeriodPay.remainingReserveGuaranty += it.multiDayGuaranteeCredited.}aSchedulePeriodPay.remainingReserveGuaranty = math().max(0.0, aSchedulePeriodPay.remainingReserveGuaranty). if (aSchedulePeriodPay.remainingReserveGuaranty > 0.0) then{fcnShow("===>>> before adding remaining reserve guarantee of  " aSchedulePeriodPay.remainingReserveGuaranty " to REGBUCKET... value now = " aSchedulePeriodPay.getPayBucket("REGBUCKET").payValue).aSchedulePeriodPay.addToBucketPayValue("REGBUCKET", aSchedulePeriodPay.remainingReserveGuaranty).fcnShow("===>>> after adding remaining reserve guarantee of  " aSchedulePeriodPay.remainingReserveGuaranty " to REGBUCKET... value now = " aSchedulePeriodPay.getPayBucket("REGBUCKET").payValue).}//////// DATA ANALYTICS ... evenly allocate remaining reserve guarantee to all reserve block duties in the SP... allocate multiday section totals evenly across reserve day duties in the muti-day section////if (aSchedulePeriodPay <> null and     aSchedulePeriodPay.schedulePeriodPayInflight <> null) then{distributedAmount  is a real initially 0.0.if (aSchedulePeriodPay.remainingReserveGuaranty > 0.0) then{aSpDutyList is some List<DutyPeriodPay> initially fcnGetReserveBlockDutiesReportingInSchedulePeriodPay(aSchedulePeriodPay).if (aSpDutyList <> null and aSpDutyList.size() > 0) then{amountForEachDuty  is a real initially aSchedulePeriodPay.remainingReserveGuaranty / aSpDutyList.size().amountForEachDuty  = fcnRoundUpAt2DecimalPlaces(amountForEachDuty).for each DutyPeriodPay in aSpDutyList as an array of DutyPeriodPay do{aDutyPeriodPay = it.if(aDutyPeriodPay.dutyPeriodPayInflightAnalytics <> null) then{aDutyPeriodPay.dutyPeriodPayInflightAnalytics.dutyReserveGuaranteedPaidPayTfp = amountForEachDuty.distributedAmount += amountForEachDuty.}}//// NOW ADJUST FOR ROUNDING VARIANCES ON THE LAST DUTY PERIOD...if(aDutyPeriodPay.dutyPeriodPayInflightAnalytics <> null) then{aDutyPeriodPay.dutyPeriodPayInflightAnalytics.dutyReserveGuaranteedPaidPayTfp += (aSchedulePeriodPay.remainingReserveGuaranty - distributedAmount).aDutyPeriodPay.dutyPeriodPayInflightAnalytics.dutyReserveGuaranteedPaidPayTfp  = fcnRoundUpAt2DecimalPlaces(aDutyPeriodPay.dutyPeriodPayInflightAnalytics.dutyReserveGuaranteedPaidPayTfp).}}}if (aSchedulePeriodPay.schedulePeriodPayInflight.reserveMultiDaySectionList.size() > 0) then{//fcnShow("===>>> fcnDistributeRemainingReserveGuarantee ... reserveMultiDaySectionList.size() for SP " aSchedulePeriodPay.schedulePeriodName " = " aSchedulePeriodPay.schedulePeriodPayInflight.reserveMultiDaySectionList.size()).multiDayAmount is a real initially 0.0.for each ReserveMultiDaySection in aSchedulePeriodPay.schedulePeriodPayInflight.reserveMultiDaySectionList as an array of ReserveMultiDaySection do{distributedAmount  = 0.0.aReserveMultiDaySection = it.multiDayAmount = aReserveMultiDaySection.multiDayGuaranteeCredited / it.reserveMultiDayList.size().multiDayAmount = fcnRoundUpAt2DecimalPlaces(multiDayAmount).//fcnShow("===>>> multiDayAmount =  aReserveMultiDaySection.multiDayGuaranteeCredited / it.reserveMultiDayList.size() = " //aReserveMultiDaySection.multiDayGuaranteeCredited " / " it.reserveMultiDayList.size() " = " multiDayAmount). if (aReserveMultiDaySection.reserveBlock <> null) then{for each DutyPeriodPay in aReserveMultiDaySection.reserveBlock.tripPay.dutyPeriodPayList as an array of DutyPeriodPay do{aDutyPeriodPay = it.if(aDutyPeriodPay.dutyPeriodPayInflightAnalytics <> null) then{aDutyPeriodPay.dutyPeriodPayInflightAnalytics.dutyMultiDayReserveGuaranteedPaidPayTfp = multiDayAmount.//fcnShow("===>>> assigning dutyMultiDayReserveGuaranteedPaidPayTfp for "  fcnGetDutyIdentificationString(aDutyPeriodPay) " to " //aDutyPeriodPay.dutyPeriodPayInflightAnalytics.dutyMultiDayReserveGuaranteedPaidPayTfp). distributedAmount += multiDayAmount.}}//// NOW ADJUST FOR ROUNDING VARIANCES ON THE LAST DUTY PERIOD...if(aDutyPeriodPay.dutyPeriodPayInflightAnalytics <> null) then{aDutyPeriodPay.dutyPeriodPayInflightAnalytics.dutyMultiDayReserveGuaranteedPaidPayTfp += (aReserveMultiDaySection.multiDayGuaranteeCredited - distributedAmount).aDutyPeriodPay.dutyPeriodPayInflightAnalytics.dutyMultiDayReserveGuaranteedPaidPayTfp = fcnRoundUpAt2DecimalPlaces(aDutyPeriodPay.dutyPeriodPayInflightAnalytics.dutyMultiDayReserveGuaranteedPaidPayTfp).}}}}}fcnShow("===>>> EXITING fcnDistributeRemainingReserveGuarantee ... The remaining reserve guarantee = " aSchedulePeriodPay.remainingReserveGuaranty).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetDutyIdentificationString](fcnGetDutyIdentificationString.md)
- [fcnGetReserveBlockDutiesReportingInSchedulePeriodPay](fcnGetReserveBlockDutiesReportingInSchedulePeriodPay.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`
- [main](main.md)

## Historial de cambios

```
Ben Lang - US18452 - 10/09/2014 - This function adds up the remaining reserve guarantee and than put that into the remaining reserve guarantee property on the SchedulePeriodPay object&gt; Then add that value to the REG bucket.
```

