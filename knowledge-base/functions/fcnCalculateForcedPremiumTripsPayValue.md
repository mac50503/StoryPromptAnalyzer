# fcnCalculateForcedPremiumTripsPayValue

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateForcedPremiumTripsPayValue`

## Propósito
04/21/2015 AM: This function will add the extra leg premium, over and above the Trip's Premium of 1.5, to the Trip's pay value

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripPay | TripPay | |

## Lógica de negocio

```blaze
tripPayValue is a real initially 0.0.resTrip is a boolean initially fcnIsReserveTrip(theTripPay.payTrip).fcnShow("====> ENTERING fcnCalculateForcedPremiumTripsPayValue for trip " theTripPay.tripNameAndDate " ...basePay = " theTripPay.basePay " is reserve trip? = " resTrip).if (resTrip = true) then{//tripBaseOverDutyBase is a real initially theTripPay.basePay - theTripPay.tripPayInflight.baseDutyPeriodSum.//tripBaseOverDutyBase = math().max(0.0, tripBaseOverDutyBase).//tripBaseOverDutyBase = fcnRoundUpAt2DecimalPlaces(tripBaseOverDutyBase).//tripPayValue = theTripPay.tripPayInflight.dutyPeriodSum + tripBaseOverDutyBase.//fcnShow("===>>> setting pay value of forced premium label reserve trip " theTripPay.tripNameAndDate " to sum of duty credits + tripBaseOverDutyBase = "//theTripPay.tripPayInflight.dutyPeriodSum " + "  tripBaseOverDutyBase " = " tripPayValue).tripPayValue = theTripPay.basePay + theTripPay.tripPayInflight.legPremium.fcnShow("===>>> setting pay value of forced premium label reserve trip " theTripPay.tripNameAndDate " basePay + the leg premium = "theTripPay.basePay " + "  theTripPay.tripPayInflight.legPremium " = " tripPayValue).}else{// Set forced PaytripPayValue = 1.5 * theTripPay.basePay.sumOfLegs is a real initially 0.0.// Add remaining leg premiumif (theTripPay.dutyPeriodPayList<>null and theTripPay.dutyPeriodPayList.size()>0) then{for each DutyPeriodPay in theTripPay.dutyPeriodPayList as an array of DutyPeriodPay do{sumOfLegs = 0.for each LegPay in it.legPayList as an array of LegPay do{if (it.basePay > 0) then{// Add leg premium over the Trip's premium of 1.5 to the Trip Pay valuesumOfLegs += it.payValue.tripPayValue += (math().max(1.5,it.payValue/it.basePay) - 1.5)*it.basePay.}}if (it.payValue > sumOfLegs) thentripPayValue += it.payValue - sumOfLegs.}}}return tripPayValue.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsReserveTrip](fcnIsReserveTrip.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`
- [main](main.md)

## Historial de cambios

```
04/21/2015 AM: This function will add the extra leg premium, over and above the Trip's Premium of 1.5, to the Trip's pay value
05/11/2015 - Pedro L DE6530 for each leg there is a formula that does payValue/basePay.  If basePay is 0 then there is no result for that operation since that is not an allowed operation, so the tripPay payValue was not updated and therefore thisMonthPay would not get updated either.  The solution was to only allow the formula if the LegPay basePay is greater than 0.
```

