# rsInflightDutyPeriodDataAnalytics

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Rulesets\rsInflightDutyPeriodDataAnalytics`

## Propósito
11/62017 - Mark B - CREW-3740 - Add ruleSumLodo for IF Pay analytics.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriodPay | DutyPeriodPay | |
| theGlobalDataCache | GlobalDataCache | |
| aSwaHolidayList | List<SwaHoliday> | |

## Historial de cambios

```
11/62017 - Mark B - CREW-3740 - Add ruleSumLodo for IF Pay analytics.
11/29/2017 - Tim A. - added rules for DPM RIG, DHR RIG, Prorated RIG and Holiday RIG
11/30/2017 - Tim A. - added rule for setting duty level RON Pay and deadheadRON pay
12/05/2017 - Tim A. - added rules ruleSumOfLegSeniorityPay and ruleSumOfDhLegSeniorityPay
02/09/2018 - Tim A. - added rules for filtering
```

