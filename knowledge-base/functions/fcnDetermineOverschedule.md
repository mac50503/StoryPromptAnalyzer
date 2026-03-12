# fcnDetermineOverschedule

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDetermineOverschedule`

## Propósito
09/20/2017 Tim A. - added IF analytics data population code

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayLeg | PayLeg | |
| theOverscheduleStandardMinutes | integer | |
| theOverscheduleOverrideDivisor | real | |
| theOverscheduleOverrideMultiplier | real | |
| theOverscheduleStandardAdder | real | |

## Lógica de negocio

```blaze
fcnShow("===>>> in function fcnDetermineOverschedule with args thePayLeg = " fcnGetFlightLegDisplayString(thePayLeg) " ...theOverscheduleStandardMinutes = " theOverscheduleStandardMinutes ", theOverscheduleOverrideDivisor = " theOverscheduleOverrideDivisor ", theOverscheduleOverrideMultiplier = " theOverscheduleOverrideMultiplier ", theOverscheduleStandardAdder = " theOverscheduleStandardAdder).thePlannedBlockTime is an integer initially Duration.newInstance(thePayLeg.scheduledDepartureDateTime, thePayLeg.scheduledArrivalDateTime).standardMinutes.retVal is a real initially 0.0.fcnShow("===>>> thePlannedBlockTime = " thePlannedBlockTime " minutes ...skd dep time = " DateTimeUtilities.getShortDateTimeString(thePayLeg.scheduledDepartureDateTime) " ...skd arr time = " DateTimeUtilities.getShortDateTimeString(thePayLeg.scheduledArrivalDateTime)).if (thePlannedBlockTime <= theOverscheduleStandardMinutes) thenretVal = theOverscheduleStandardAdder.else{retVal = ((math().floor((thePlannedBlockTime - theOverscheduleStandardMinutes) / theOverscheduleOverrideDivisor) * theOverscheduleOverrideMultiplier) + theOverscheduleStandardAdder).fcnShow("===>>> overschedule = (((thePlannedBlockTime - theOverscheduleStandardMinutes) / theOverscheduleOverrideDivisor) * theOverscheduleOverrideMultiplier) + theOverscheduleStandardAdder").fcnShow("===>>> " retVal " = (((" thePlannedBlockTime " - " theOverscheduleStandardMinutes ") / " theOverscheduleOverrideDivisor" ) * "theOverscheduleOverrideMultiplier ") + " theOverscheduleStandardAdder).}retVal = fcnRoundUpAt2DecimalPlaces(retVal).fcnShow("===>>> returning overschedule of " retVal " for flight leg " fcnGetFlightLegDisplayString(thePayLeg)).//// IF  ANALYTICSif (thePayLeg.legPay <> null and thePayLeg.legPay.legPayInflightAnalytics <> null) then{if(thePayLeg.legWorkCodeList.contains("GR") = false and (thePayLeg.nonFlyCode = null or thePayLeg.nonFlyCode.length() = 0)) then {thePayLeg.legPay.legPayInflightAnalytics.overschedulePremiumTfp = fcnRoundUpAt2DecimalPlaces(math().max(0.0, retVal - legMileageTfp_var)).}}//// FO  ANALYTICSif (thePayLeg.legPay <> null and thePayLeg.legPay.legPayFltOpsAnalytics <> null) then{if(thePayLeg.legWorkCodeList.contains("GR") = false and (thePayLeg.nonFlyCode = null or thePayLeg.nonFlyCode.length() = 0)) then {thePayLeg.legPay.legPayFltOpsAnalytics.overschedulePremiumTfp = fcnRoundUpAt2DecimalPlaces(math().max(0.0, retVal - legMileageTfp_var)).}}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetFlightLegDisplayString](fcnGetFlightLegDisplayString.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

## Historial de cambios

```
09/20/2017 Tim A. - added IF analytics data population code
01/09/2018 Tim A. - added FO analytics data population code
```

