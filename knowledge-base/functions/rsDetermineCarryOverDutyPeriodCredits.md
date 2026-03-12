# rsDetermineCarryOverDutyPeriodCredits

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Rulesets\rsDetermineCarryOverDutyPeriodCredits`

## Propósito
03/06/2015 TIm A. DE6035 - added rule ruleAddToTripDutyPremium

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSchedulePeriodStart | DateTime | |
| theSchedulePeriodEnd | DateTime | |
| theDutyPeriod | PayDutyPeriod | |
| theDutyPeriodPay | DutyPeriodPay | |

## Llamado por

- [fcnModifyDutyAndTripValuesForSplitGuaranty](fcnModifyDutyAndTripValuesForSplitGuaranty.md)
- [fcnSetLegPremiumThisMonth](fcnSetLegPremiumThisMonth.md)

## Historial de cambios

```
03/06/2015 TIm A. DE6035 - added rule ruleAddToTripDutyPremium
04/09/2015 Akshay M DE6318 Modified ruleCarryOutPayCalcs and ruleDefaultPayCalcs to ensure a duty starting right at the end of a schedule period pays in that schedule period
6/16/2015 - Ben Lang - DE6669 - Added logic to use the first leg's scheduleDepartureDateTime for Inflight
```

