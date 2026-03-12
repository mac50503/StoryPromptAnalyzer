# fcnSetRigsGreaterThanPremiumForTrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnSetRigsGreaterThanPremiumForTrip`

## Propósito
10/04/2024 - Added S label check in the if condition

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
//// constuctor sets default to true so only need to override for false legPremium is a real initially fcnGetSumOfLegPremiumForTrip(aTripPay).if ((aTripPay.creditType = "F" and aTripPay.assignmentLabel = ("J" or "U" or "V" or "S")) or    (aTripPay <> null and     aTripPay.tripPayInflight <> null and     aSchedulePeriodPay <> null and    legPremium > 0 and    aTripPay.tripPayInflight.dutyPeriodSum >= aTripPay.tripPayInflight.highestTripRig)) then{aTripPay.tripPayInflight.rigsGreaterThanPremium = false.}fcnShow("===>>> EXITING fcnSetRigsGreaterThanPremiumForTrip for " aTripPay.tripNameAndDate " ...SP " aSchedulePeriodPay.schedulePeriodName " ...legPremium = " legPremium " ...dutyPeriodSum = " aTripPay.tripPayInflight.dutyPeriodSum  " ...highestTripRig = " aTripPay.tripPayInflight.highestTripRig " ...rigsGreaterThanPremium = "aTripPay.tripPayInflight.rigsGreaterThanPremium).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetSumOfLegPremium](fcnGetSumOfLegPremium.md)
- [fcnGetSumOfLegPremiumForTrip](fcnGetSumOfLegPremiumForTrip.md)
- `fcnShow()`

## Historial de cambios

```
10/04/2024 - Added S label check in the if condition
```

