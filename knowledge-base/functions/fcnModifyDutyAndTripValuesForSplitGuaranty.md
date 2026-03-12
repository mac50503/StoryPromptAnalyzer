# fcnModifyDutyAndTripValuesForSplitGuaranty

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnModifyDutyAndTripValuesForSplitGuaranty`

## Propósito
MP-US18906-11/14/2014 - This month change for a duty period calls for various recalculations for ex. trip RIG, Trip Excess, Trip credit etc. this is called by rsDetermineRemainingSplitGuaranty ruleset

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | PayDutyPeriod | |
| theSchedulePeriod | SchedulePeriod | |
| theSchedulePeriodPay | SchedulePeriodPay | |
| nextSchedulePeriodPay | SchedulePeriodPay | |
| previousSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
theTripPay is some TripPay initially theDutyPeriod.payTrip.tripPay.// Modify thisMonthPay last month pay, next month pay & prorated pay for theDutyPeriodrsDetermineCarryOverDutyPeriodCredits(theSchedulePeriodPay.schedulePeriodStart, theSchedulePeriodPay.schedulePeriodEnd, theDutyPeriod, theDutyPeriod.dutyPeriodPay).//Modify dutyPeriodSum & tripRIGtheTripPay.tripPayInflight.dutyPeriodSum = 0.theTripPay.tripPayInflight.thrValue = 0.theTripPay.tripPayInflight.tripRIG = 0.//Reset prorated pay for last duty periodlastDutyPeriodPay is some DutyPeriodPay initially null.if theTripPay.dutyPeriodPayList.size() > 0 thenlastDutyPeriodPay =  theTripPay.dutyPeriodPayList.get(theTripPay.dutyPeriodPayList.size() - 1).if (lastDutyPeriodPay <> null) thenlastDutyPeriodPay.proratedPay = fcnRoundUpAt2DecimalPlaces(lastDutyPeriodPay.thisMonthPay).//Recalculate trip RIGS as duty sum is changed//US18896 - The way we calculate Trip RIGS has changedtheDutyPeriod.payTrip = CssIfTripPaySubFlow(theDutyPeriod.payTrip).//Recalculate trip credit as duty sum is changedif ((theDutyPeriod.payTrip.creditType = "P"  and theDutyPeriod.payTrip.tripPay.tripPayInflight.thrValue > theDutyPeriod.payTrip.tripPay.basePay) is false) thenrsDetermineTripCreditsAndCreditType(theDutyPeriod.payTrip).// recalculate trip excess as duty sum/trip pay is changedfcnDetermineDutyTripExcess(theDutyPeriod.payTrip.tripPay, theSchedulePeriod, theSchedulePeriodPay).// recalculate trip carry over as duty sum/ trip pay is changedfcnDetermineCarryOverTripCredits(theDutyPeriod.payTrip.tripPay, theSchedulePeriodPay, nextSchedulePeriodPay, previousSchedulePeriodPay).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDetermineCarryOverTripCredits](fcnDetermineCarryOverTripCredits.md)
- [fcnDetermineDutyTripExcess](fcnDetermineDutyTripExcess.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- [rsDetermineCarryOverDutyPeriodCredits](rsDetermineCarryOverDutyPeriodCredits.md)
- [rsDetermineTripCreditsAndCreditType](rsDetermineTripCreditsAndCreditType.md)

## Historial de cambios

```
MP-US18906-11/14/2014 - This month change for a duty period calls for various recalculations for ex. trip RIG, Trip Excess, Trip credit etc. this is called by rsDetermineRemainingSplitGuaranty ruleset
BL-US18896-11/18/2014 - Call the ruleflow that calculates trip RIGs in this function.
```

