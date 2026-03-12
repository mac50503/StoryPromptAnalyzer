# rsInitializeReseveBlocks

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Rulesets\rsInitializeReseveBlocks`

## Propósito
MP-US16565-7/3/2014:This ruleset augments the ReserveBlockDay objects to associate Reserve Trips (“R”) and Airport Standbys (“AS1”, “ASB”).

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theReservePayrollReport | ReservePayrollReport | |

## Historial de cambios

```
MP-US16565-7/3/2014:This ruleset augments the ReserveBlockDay objects to associate Reserve Trips (“R”) and Airport Standbys (“AS1”, “ASB”).
MP-US17905-8/7/2014: changed to add multiple trips.
MP-US1790 -8/21/2014: Changed to store duty period instead of reserve trips
10/22/2014 Corey Gu US18781 - In ruleAssociateDutyPeriodsForReserveBlock, replaced theTrip.assignmentLabel =(ignoring case) "R" with payTripInflight.isReserveTrip = true.
MP-US18906-11/3/2014 - added new rule ruleScheduleSplitMinimum
7/2/2015 - Melissa S - DE6957 - Updated ruleAssociateDutyPeriodsForReserveBlock for the last duty period, if the THR is higher than the base pay, starting with the THR value so the excess gets distributed.
07/07/2015 Corey Gu - DE6972 - Updated ruleAssociateDutyPeriodsForReserveBlock to add a new condition 'if anyTrip.tripPay.creditType = "T", use THR for minGuarantee'.
7/7/2015 - Melissa S - DE6972/DE6931/DE6964 - Added exclusions for RON duty periods, which don't pay THR or DHR
7/9/2015 - Melissa S - DE7018 - Reverted change from DE6957
TA -DE7711 - 11/03/2015: modified rule ruleAssociateDutyPeriodsForReserveBlock to initialize minGuarantee to zero if pre &gt; rigs at trip level
```

