# fcnGetSumOfLegPremiumForTrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetSumOfLegPremiumForTrip`

## Propósito
7/9/2015 - Melissa S - DE7016 - New function to add the total of the leg premiums for the trip, regardless of which schedule period the duty period falls in.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
retVal is a real initially 0.0.if (aTripPay <> null and aTripPay.tripPayInflight <> null) then{for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do retVal += fcnGetSumOfLegPremium(it).aTripPay.tripPayInflight.legPremium = retVal.}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetSumOfLegPremium](fcnGetSumOfLegPremium.md)

## Llamado por

- [fcnSetLegPremiumThisMonth](fcnSetLegPremiumThisMonth.md)
- [fcnSetRigsGreaterThanPremiumForTrip](fcnSetRigsGreaterThanPremiumForTrip.md)

## Historial de cambios

```
7/9/2015 - Melissa S - DE7016 - New function to add the total of the leg premiums for the trip, regardless of which schedule period the duty period falls in.
```

