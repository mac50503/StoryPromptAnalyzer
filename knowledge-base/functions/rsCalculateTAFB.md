# rsCalculateTAFB

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Rulesets\rsCalculateTAFB`

## Propósito
06/24/2014 Corey Gu US16985 - Initial development

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | PayTrip | |

## Historial de cambios

```
06/24/2014 Corey Gu US16985 - Initial development
09/19/2015 Mitesh P US18397 - Added rule to calculate and populate trip RIG.
11/13/2014 Ben Lang US18896 - Adding Credit Type Exceptions
12/17/2014 Pedro Loaiza DE5702 - Added the hasRONDutyType variable and modified conditions to add dutyPeriodSum
02/17/2015 Tim A. added ruleAdjustTimeAwayFromBase - DE5866 - adjust TAFB for last leg arrivial not equal to scheduled arrival
02/26/2015 Tim A. added ruleCalculateThrToStartOfRonRig - DE7306
```

