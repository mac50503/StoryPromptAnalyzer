# fcnDetermineDutyTripExcess

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDetermineDutyTripExcess`

## Propósito
Ben Lang - US15815 - Reviewed Code - This code calculates the trip excess and adds that value to the last duty period tripExcess value.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |
| aSchedulePeriod | SchedulePeriod | |
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially false.if(aTripPay <> null) then {if2025NewDomicileDayPayEffectiveDateActiveFlag = fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(aTripPay.beginDateTime, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").}if(if2025NewDomicileDayPayEffectiveDateActiveFlag) then {if (aSchedulePeriodPay <> null and    aTripPay.dutyPeriodPayList is not equal to null and     aTripPay.dutyPeriodPayList.size() > 0) then{fcnShow("===>>> ENTERING FUNCTION: fcnDetermineDutyTripExcess for Trip: " aTripPay.tripName " ...aSchedulePeriodPay = " aSchedulePeriodPay.schedulePeriodName).aTripExcess is a real initially 0.0.aTripExcess = fcnGetTripExcess(aTripPay).fcnShow("===>>>TripExcess = " aTripExcess).// Create a proper variable that will be used after the APIC-1209 checklastDutyPeriodPay is some DutyPeriodPay initially a DutyPeriodPay;lastDutyPeriodPay = aTripPay.dutyPeriodPayList.get(aTripPay.dutyPeriodPayList.size() - 1).if (lastDutyPeriodPay <> null and aTripPay.dutyPeriodPayList.size() > 0) then // DE5706 - Allow negative tripExcess values if the trip credit is forced and is less than the trip pay{lastDutyPeriodPay.tripExcess = aTripExcess.fcnShow("===>> Assigning trip excess of " lastDutyPeriodPay.tripExcess " to DutyPeriodPay: " lastDutyPeriodPay.sequenceNumber).lastDutyPeriodPay.proratedPay += aTripExcess.fcnShow("===>> Adding trip excess of " lastDutyPeriodPay.tripExcess " to DutyPeriodPay: " lastDutyPeriodPay.sequenceNumber "'s proratedPay property ... value now = " lastDutyPeriodPay.proratedPay).// now need to add the excess to the proper month's pay value...// FIRST HANDLE THE TRIP EXCESS FOR MONTH TO DATE CALCS...theEffectiveReportDateTime is some LocalDateTime initially fcnGetEffectiveReportDateTime(lastDutyPeriodPay.payDutyPeriod).toLocalDateTime().if (aSchedulePeriodPay <> null and lastDutyPeriodPay.includeInMonthToDateCalc is equal to true and fcnDoesDutyPeriodPayBeginInSchedulePeriodPay(lastDutyPeriodPay, aSchedulePeriodPay)) then{aSchedulePeriodPay.monthToDateCredit += aTripExcess.fcnShow("............................===>>> Adding Trip Excess "  aTripExcess " to current schedule period MonthToDateCredit ...... value now = " aSchedulePeriodPay.monthToDateCredit).}// NEXT HANDLE CURRENT SCHEDULE PERIOD (Month)...if (theEffectiveReportDateTime.isBefore(aSchedulePeriodPay.schedulePeriodStart.toLocalDateTime()) = false andtheEffectiveReportDateTime.isAfter(aSchedulePeriodPay.schedulePeriodEnd.toLocalDateTime()) = false) then{aTripPay.thisMonthPay += aTripExcess.fcnShow("............................===>>> Adding Trip Excess "  aTripExcess " to thisMonthPay of trip " aTripPay.tripName " thisMonthPay now = " aTripPay.thisMonthPay).}// NEXT HANDLE PREVIOUS SCHEDULE PERIOD (Month)...else if (theEffectiveReportDateTime.isBefore(aSchedulePeriodPay.schedulePeriodStart.toLocalDateTime()) is equal to true) then{aTripPay.lastMonthPay += aTripExcess.fcnShow("............................===>>> Adding Trip Excess "  aTripExcess " to lastMonthPay of trip " aTripPay.tripName " lastMonthPay now = " aTripPay.lastMonthPay).}// NEXT HANDLE NEXT SCHEDULE PERIOD (Month)...else if (theEffectiveReportDateTime.isAfter(aSchedulePeriodPay.schedulePeriodEnd.toLocalDateTime()) is equal to true) then{aTripPay.nextMonthPay += aTripExcess.fcnShow("............................===>>> Adding Trip Excess "  aTripExcess " to nextMonthPay of trip " aTripPay.tripName " nextMonthPay now = " aTripPay.nextMonthPay).}}fcnShow("===>>> EXITING FUNCTION: fcnDetermineDutyTripExcess  for Trip: " aTripPay.tripName " ...aSchedulePeriodPay = " aSchedulePeriodPay.schedulePeriodName).}}else {if (aSchedulePeriodPay <> null andaTripPay.dutyPeriodPayList is not equal to null and aTripPay.dutyPeriodPayList.size() > 0) then{fcnShow("===>>> ENTERING FUNCTION: fcnDetermineDutyTripExcess for Trip: " aTripPay.tripName " ...aSchedulePeriodPay = " aSchedulePeriodPay.schedulePeriodName).aTripExcess is a real initially 0.0.aTripExcess = fcnGetTripExcess(aTripPay).fcnShow("===>>>TripExcess = " aTripExcess).// Create a proper variable that will be used after the APIC-1209 checklastDutyPeriodPay is some DutyPeriodPay initially a DutyPeriodPay;lastDutyPeriodPay = aTripPay.dutyPeriodPayList.get(aTripPay.dutyPeriodPayList.size() - 1).if (lastDutyPeriodPay <> null and aTripPay.dutyPeriodPayList.size() > 0) then // DE5706 - Allow negative tripExcess values if the trip credit is forced and is less than the trip pay{lastDutyPeriodPay.tripExcess = aTripExcess.fcnShow("===>> Assigning trip excess of " lastDutyPeriodPay.tripExcess " to DutyPeriodPay: " lastDutyPeriodPay.sequenceNumber).lastDutyPeriodPay.proratedPay += aTripExcess.fcnShow("===>> Adding trip excess of " lastDutyPeriodPay.tripExcess " to DutyPeriodPay: " lastDutyPeriodPay.sequenceNumber "'s proratedPay property ... value now = " lastDutyPeriodPay.proratedPay).// now need to add the excess to the proper month's pay value...// FIRST HANDLE THE TRIP EXCESS FOR MONTH TO DATE CALCS...theEffectiveReportDateTime is some DateTime initially fcnGetEffectiveReportDateTime(lastDutyPeriodPay.payDutyPeriod).if (aSchedulePeriodPay <> null and lastDutyPeriodPay.includeInMonthToDateCalc is equal to true and fcnDoesDutyPeriodPayBeginInSchedulePeriodPay(lastDutyPeriodPay, aSchedulePeriodPay)) then{aSchedulePeriodPay.monthToDateCredit += aTripExcess.fcnShow("............................===>>> Adding Trip Excess "  aTripExcess " to current schedule period MonthToDateCredit ...... value now = " aSchedulePeriodPay.monthToDateCredit).}// NEXT HANDLE CURRENT SCHEDULE PERIOD (Month)...if (theEffectiveReportDateTime.isBefore(aSchedulePeriodPay.schedulePeriodStart) = false andtheEffectiveReportDateTime.isAfter(aSchedulePeriodPay.schedulePeriodEnd) = false) then{aTripPay.thisMonthPay += aTripExcess.fcnShow("............................===>>> Adding Trip Excess "  aTripExcess " to thisMonthPay of trip " aTripPay.tripName " thisMonthPay now = " aTripPay.thisMonthPay).}// NEXT HANDLE PREVIOUS SCHEDULE PERIOD (Month)...else if (theEffectiveReportDateTime.isBefore(aSchedulePeriodPay.schedulePeriodStart) is equal to true) then{aTripPay.lastMonthPay += aTripExcess.fcnShow("............................===>>> Adding Trip Excess "  aTripExcess " to lastMonthPay of trip " aTripPay.tripName " lastMonthPay now = " aTripPay.lastMonthPay).}// NEXT HANDLE NEXT SCHEDULE PERIOD (Month)...else if (theEffectiveReportDateTime.isAfter(aSchedulePeriodPay.schedulePeriodEnd) is equal to true) then{aTripPay.nextMonthPay += aTripExcess.fcnShow("............................===>>> Adding Trip Excess "  aTripExcess " to nextMonthPay of trip " aTripPay.tripName " nextMonthPay now = " aTripPay.nextMonthPay).}}fcnShow("===>>> EXITING FUNCTION: fcnDetermineDutyTripExcess  for Trip: " aTripPay.tripName " ...aSchedulePeriodPay = " aSchedulePeriodPay.schedulePeriodName).}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDoesDutyPeriodPayBeginInSchedulePeriodPay](fcnDoesDutyPeriodPayBeginInSchedulePeriodPay.md)
- [fcnGetEffectiveReportDateTime](fcnGetEffectiveReportDateTime.md)
- [fcnGetTripExcess](fcnGetTripExcess.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- `fcnShow()`

## Llamado por

- [fcnModifyDutyAndTripValuesForSplitGuaranty](fcnModifyDutyAndTripValuesForSplitGuaranty.md)

## Historial de cambios

```
Ben Lang - US15815 - Reviewed Code - This code calculates the trip excess and adds that value to the last duty period tripExcess value.
DE5706 - Ben Lang - 12/16/2014 - Allow negative tripExcess values if the trip credit is forced and is less than the trip pay.
6/16/2015 - Ben Lang - DE6669 - Added logic to use the first leg's scheduleDepartureDateTime for Inflight
```

