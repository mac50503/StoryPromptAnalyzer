# fcnBuildUnutilizedReserveList

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnBuildUnutilizedReserveList`

## Propósito
US16986 : SH : 08/20/2014: Unutilized Reserve Day Calculation

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSchedulePeriodPayInflight | SchedulePeriodPayInflight | |
| theReservePayrollReport | ReservePayrollReport | |
| theSchedulePeriodPay | SchedulePeriodPay | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |

## Lógica de negocio

```blaze
okToProcede is a boolean initially fcnReportDateRangeFiltersIncludeEntireSchedulePeriod(reportFilterStart, reportFilterEnd, theSchedulePeriodPay).if (okToProcede)  then{if (theSchedulePeriodPayInflight.reserveMonthlyGuaranteeSectionList <> null) then{if (theSchedulePeriodPayInflight.reserveMonthlyGuaranteeSectionList.size() > 0) then {totalTFPCredited is a real initially 0.// DE6013 - Changed from rawMinimumGuarantee to local monthlyReserveGuaranteemonthlyReserveGuarantee is a real initially theSchedulePeriodPayInflight.reserveMonthlyGuaranteeSectionList.get(0).monthlyGuarantee.fcnShow("====>> MonthlyGuarantee = " monthlyReserveGuarantee).for each ReserveBlockDay in theReservePayrollReport.reserveBlockDayList such that it.isForMonthlyGuarantee do {fcnShow("===>> Running fcnBuildUnutilizedReserveList... Duty Period that falls on " fcnGetShortDateTimeString(it.calendarDay) " pays " it.tfpCredited).fcnShow("===>> monthlyReserveGuarantee = " monthlyReserveGuarantee " ... totalTFPCredited = " totalTFPCredited).totalTFPCredited = totalTFPCredited + it.tfpCredited.if (totalTFPCredited >= monthlyReserveGuarantee and it.tfpCredited = 0) then {initialValueTotalUnutilizedReserveTfpCredited is a real initially theSchedulePeriodPayInflight.totalUnutilizedReserveTfpCredited.anUnutilizedReserve is some UnutilizedReserve initially a UnutilizedReserve.anUnutilizedReserve.unutilizedReserveDateTime = it.calendarDay.anUnutilizedReserve.unutilizedReserveTfpCredited = 3.00.theSchedulePeriodPayInflight.addUnutilizedReserve(anUnutilizedReserve).theSchedulePeriodPayInflight.unutilizedReserveSectionList.get(0).unutilizedReserveTfpCredited += anUnutilizedReserve.unutilizedReserveTfpCredited.theSchedulePeriodPayInflight.totalUnutilizedReserveTfpCredited += anUnutilizedReserve.unutilizedReserveTfpCredited.//distributing to trip bucket APIC-1475valueToDistributeTripBucket is a real initially theSchedulePeriodPayInflight.totalUnutilizedReserveTfpCredited - initialValueTotalUnutilizedReserveTfpCredited.if(valueToDistributeTripBucket <>0 and it.reserveBlock.tripPay <> null and it.reserveBlock.tripPay <> unknown) then{it.reserveBlock.tripPay.addTripPayBuckets("REGBUCKET", fcnRoundUpAt2DecimalPlaces(valueToDistributeTripBucket), 1.0).fcnShow("===>>addTripPayBuckets REGBUCKET value " valueToDistributeTripBucket).}fcnShow("===>> Adding 3.0 to totalUnutilizedReserveTfpCredited...from reserve block day " fcnGetShortDateTimeString(it.calendarDay)).}}}}}fcnShow("====>> EXITING function fcnBuildUnutilizedReserveList ...SP " theSchedulePeriodPay.schedulePeriodName " Unutilized reserve compensation total = " theSchedulePeriodPayInflight.totalUnutilizedReserveTfpCredited).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetShortDateTimeString](fcnGetShortDateTimeString.md)
- [fcnReportDateRangeFiltersIncludeEntireSchedulePeriod](fcnReportDateRangeFiltersIncludeEntireSchedulePeriod.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

## Historial de cambios

```
US16986 : SH : 08/20/2014: Unutilized Reserve Day Calculation
US18452 : BL : 10/16/2014: Changed comparison from totalMinimumGuarentee to rawMinimumGuarentee
US18452 : BL : 03/18/2014: Changed comparison from rawMinimumGuarentee to monthlyGuarantee. Also now updating theSchedulePeriodPayInflight.unutilizedReserveSectionList.get(0).unutilizedReserveTfpCredited
```

