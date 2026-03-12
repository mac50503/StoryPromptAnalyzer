# fcnInitializeNonflyPayDays

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnInitializeNonflyPayDays`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
if (aTripPay <> null and aTripPay.payTrip <> null and      ((aTripPay.tripPayInflightAnalytics <> null and aTripPay.tripPayInflightAnalytics.nonflyTripPay <> null) or      (aTripPay.tripPayFltOpsAnalytics <> null and aTripPay.tripPayFltOpsAnalytics.nonflyTripPay <> null))) then{days is an integer initially 0.if (aTripPay.tripPayInflightAnalytics <> null) then {aTripPay.tripPayInflightAnalytics.nonflyTripPay.nonflyDayPayList.clear().days = fcnGetCountOfSwaDays(aTripPay.beginDateTime, aTripPay.endDateTime).fcnShow("===>>> in function fcnInitializeNonflyPayDays for trip " aTripPay.tripName " count of intersecting SWA days = " days).}else if (aTripPay.tripPayFltOpsAnalytics <> null) then {aTripPay.tripPayFltOpsAnalytics.nonflyTripPay.nonflyDayPayList.clear().earlierDate is some DateTime initially  DateTime.newInstance(aTripPay.beginDateTime.year, aTripPay.beginDateTime.monthOfYear, aTripPay.beginDateTime.dayOfMonth, 0, 0, 0);        laterDate is some DateTime initially   DateTime.newInstance(aTripPay.endDateTime.year, aTripPay.endDateTime.monthOfYear, aTripPay.endDateTime.dayOfMonth, 0, 0, 0);                days = Days.daysBetween(earlierDate, laterDate).days + 1.fcnShow("===>>> in function fcnInitializeNonflyPayDays for trip " aTripPay.tripName " count of intersecting Calendar days = " days).}dayBasePay is a real initially aTripPay.basePay / days.dayBasePay = fcnRoundUpAt2DecimalPlaces(dayBasePay).dayPay is a real initially aTripPay.payValue / days.dayPay = fcnRoundUpAt2DecimalPlaces(dayPay).dayPremiumPay is a real initially 0.0.if (aTripPay.tripPayInflightAnalytics <> null) thendayPremiumPay = aTripPay.tripPayInflightAnalytics.nonflyTripPay.premiumPayValue / days.else if (aTripPay.tripPayFltOpsAnalytics <> null) thendayPremiumPay = aTripPay.tripPayFltOpsAnalytics.nonflyTripPay.premiumPayValue / days.dayPremiumPay = fcnRoundUpAt2DecimalPlaces(dayPremiumPay).runningDayBasePay is a real initially 0.0.runningDayPay is a real initially 0.0.runningDayPremiumPay is a real initially 0.0.aNonflyDayPay is some NonflyDayPay initially null.start is some DateTime initially aTripPay.beginDateTime.if (aTripPay.tripPayInflightAnalytics <> null and aTripPay.beginDateTime.hourOfDay < 3) then {start = start.minusDays(1).}while (days > 0) do{aNonflyDayPay = a NonflyDayPay.aNonflyDayPay.nonflyCode = aTripPay.nonFlyCode.aNonflyDayPay.position = aTripPay.payTrip.assignmentCrewPosition.aNonflyDayPay.startDateTime = start.aNonflyDayPay.basePayValue = dayBasePay.runningDayBasePay += dayBasePay.aNonflyDayPay.payValue = dayPay.runningDayPay += dayPay.aNonflyDayPay.premiumPayValue = dayPremiumPay.runningDayPremiumPay += dayPremiumPay.if (aTripPay.tripPayInflightAnalytics <> null) thenaTripPay.tripPayInflightAnalytics.nonflyTripPay.nonflyDayPayList.add(aNonflyDayPay).else if (aTripPay.tripPayFltOpsAnalytics <> null) thenaTripPay.tripPayFltOpsAnalytics.nonflyTripPay.nonflyDayPayList.add(aNonflyDayPay).start = start.plusDays(1).start = start.withTime(0, 1, 0, 0).days -= 1.fcnShow("===>>> creating new NonflyDayPay object with start = " fcnGetShortDateTimeString(aNonflyDayPay.startDateTime) " ...base pay = " aNonflyDayPay.basePayValue " ...pay value = " aNonflyDayPay.basePayValue " ...premium value = " aNonflyDayPay.premiumPayValue).}//// NOW ADJUST THE LAST DAY TO MAKE SURE TOTALS SQUARE WITH THE TOTAL TRIP NUMBERS...if (runningDayBasePay > aTripPay.basePay) then{aNonflyDayPay.basePayValue -=  (runningDayBasePay - aTripPay.basePay).aNonflyDayPay.basePayValue =  fcnRoundUpAt2DecimalPlaces(aNonflyDayPay.basePayValue).}if (runningDayPay > aTripPay.payValue) then{aNonflyDayPay.payValue -=  (runningDayPay - aTripPay.payValue).aNonflyDayPay.payValue =  fcnRoundUpAt2DecimalPlaces(aNonflyDayPay.payValue).}if (aTripPay.tripPayInflightAnalytics <> null and runningDayPremiumPay > aTripPay.tripPayInflightAnalytics.nonflyTripPay.premiumPayValue) then{aNonflyDayPay.premiumPayValue -=  (runningDayPremiumPay - aTripPay.tripPayInflightAnalytics.nonflyTripPay.premiumPayValue).aNonflyDayPay.premiumPayValue =  fcnRoundUpAt2DecimalPlaces(aNonflyDayPay.premiumPayValue).}else if (aTripPay.tripPayFltOpsAnalytics <> null) then{aNonflyDayPay.premiumPayValue -=  (runningDayPremiumPay - aTripPay.tripPayFltOpsAnalytics.nonflyTripPay.premiumPayValue).aNonflyDayPay.premiumPayValue =  fcnRoundUpAt2DecimalPlaces(aNonflyDayPay.premiumPayValue).}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetCountOfSwaDays](fcnGetCountOfSwaDays.md)
- [fcnGetShortDateTimeString](fcnGetShortDateTimeString.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

