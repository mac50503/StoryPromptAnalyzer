# rsBuildReserveBlockDayList

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Rulesets\rsBuildReserveBlockDayList`

## Propósito
MP-US16565-7/3/2014:This ruleset creates ReserveBlockDay objects from Reserve Blocks in (“K”, “T”, “B”) and adds them to theReservePayrollReport object

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayCrewMember | PayCrewMember | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |
| theSchedulePeriodPay | SchedulePeriodPay | |

## Historial de cambios

```
MP-US16565-7/3/2014:This ruleset creates ReserveBlockDay objects from Reserve Blocks in (“K”, “T”, “B”) and adds them to theReservePayrollReport object
MP-US17905-8/7/2014: Changes due to Reserve Block day class changes
MP-US1790 -8/21/2014: Changed to initialize duty period instead of reserve trips
USD-Crew689-5/3/2017: Created new rule to count B &amp; T label non-fly &amp; reserveblocks in sequence.(deleted old B &amp; T label reserveblock rule).
Blazer-60-7/10/2024: Chnages to rule "ruleSetOriginalMinimumGuarantee" to caluclate minimuguarantee inside Blaze instead of reading from CSS
Blazer-27-07/24/2024: New Reserve Types - Pay
```

