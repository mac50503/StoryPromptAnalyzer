# fcnAssignSchedulePeriodPayDaysOfService

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnAssignSchedulePeriodPayDaysOfService`

## Propósito
01-21-2016 Tim A - CSCH-1701 - changed methodolgy for determining how many days are contained in each schedule period

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
if (aSchedulePeriodPay <> null and daysOfServiceBlockArray <> null and daysOfServiceBlockArray.count > 0) then{//// determine dayOfMonthCount by ignoring time of day for schedule period start and end dates...dayOfMonthCount is a integer initially Days.daysBetween(aSchedulePeriodPay.schedulePeriodStart.toLocalDate().toDateTimeAtStartOfDay(), aSchedulePeriodPay.schedulePeriodEnd.toLocalDate().toDateTimeAtStartOfDay()).days. //fcnShow("===>>> ENTERING fcnAssignSchedulePeriodPayDaysOfService ...SP = " aSchedulePeriodPay.schedulePeriodName " ...daysOfServiceBlockArray contains " daysOfServiceBlockArray.count " daysOfserviceBlocks").//fcnShow("===>>> calculating days between " aSchedulePeriodPay.schedulePeriodStart " and " aSchedulePeriodPay.schedulePeriodEnd " ...dayOfMonthCount  = " dayOfMonthCount).count is an integer initially 0.aSchedulePeriodPay.daysOfService = 0.  /// default....dayCount is an integer initially 0.aDay is some DateTime initially null.dayOfService is a boolean initially false.dayCounts is a boolean initially false.while (dayCount < dayOfMonthCount) do {dayCounts = false. //defaultdayCount  += 1.aDay = aSchedulePeriodPay.schedulePeriodStart.withDayOfMonth(dayCount).//fcnShow("===>>> examining day " DateTimeUtilities.getShortDateTimeString(aDay)).for each DaysOfServiceBlock in daysOfServiceBlockArray do{//fcnShow("===>>> processing DaysOfserviceblock with start = " DateTimeUtilities.getShortDateTimeString(it.startDateTime) " ... end = " DateTimeUtilities.getShortDateTimeString(it.endDateTime)).dayOfService = false.  // default...if (aDay.isBefore(it.startDateTime) = false and     aDay.isAfter(it.endDateTime) = false) then{dayOfService = true.dayCounts = true.count = count + 1.//fcnShow("===>>> SP = " aSchedulePeriodPay.schedulePeriodName " ...adding 1 to daysOfService for day " fcnGetShortDateTimeString(aDay) " ..count of daysOfService now = " count).}//else//fcnShow("===>>> NOT adding 1 to daysOfService count ...value now = " count).//fcnShow("===>>> Is " DateTimeUtilities.getShortDateTimeString(aDay) " ... before " DateTimeUtilities.getShortDateTimeString(it.startDateTime) " ? ===>>> " aDay.isBefore(it.startDateTime)).//fcnShow("===>>> Is " DateTimeUtilities.getShortDateTimeString(aDay) " ... after " DateTimeUtilities.getShortDateTimeString(it.endDateTime) " ? ===>>> " aDay.isAfter(it.endDateTime)).//fcnShow("===>>> Is " DateTimeUtilities.getShortDateTimeString(aDay) " ... within start of " DateTimeUtilities.getShortDateTimeString(it.startDateTime) " ... and end of " DateTimeUtilities.getShortDateTimeString(it.endDateTime) " ? ===>>> " dayOfService).}//fcnShow("===>>> SP = " aSchedulePeriodPay.schedulePeriodName " ... Current Day = " DateTimeUtilities.getShortDateTimeString(aDay) " ... is day of service? = " dayCounts).dayOfService = false.}aSchedulePeriodPay.daysOfService = count.//fcnShow("===>>> EXITING fcnAssignSchedulePeriodPayDaysOfService for SP: " aSchedulePeriodPay.schedulePeriodName " ... daysOf Service = " aSchedulePeriodPay.daysOfService).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetShortDateTimeString](fcnGetShortDateTimeString.md)
- `fcnShow()`

## Historial de cambios

```
01-21-2016 Tim A - CSCH-1701 - changed methodolgy for determining how many days are contained in each schedule period
```

