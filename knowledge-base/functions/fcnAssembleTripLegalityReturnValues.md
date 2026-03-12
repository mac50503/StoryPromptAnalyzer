# fcnAssembleTripLegalityReturnValues

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnAssembleTripLegalityReturnValues`

## Propósito
5/11/2016 - Mark B - CSCH-2107 - Add theFdpNumberOfLegsList as a parameter.  Add fdpNumberOfLegsList to theRuleResult.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLegBlockTimeList | List<LegBlockTime> | |
| theDutyPeriodBlockTimeList | List<DutyPeriodBlockTime> | |
| theDutyPeriodDutyDurationList | List<DutyPeriodDutyDuration> | |
| theDutyPeriodFDPDurationList | List<DutyPeriodFDPDuration> | |
| theTripCalculations | TripCalculations | |
| theRuleResult | RuleResult | |
| theLegalityLimitList | List<LegalityLimit> | |
| theDutyPeriodRestList | List<DutyPeriodRest> | |
| theFdpNumberOfLegsList | List<FdpNumberOfLegs> | |

## Lógica de negocio

```blaze
if (theLegBlockTimeList <> null and theLegBlockTimeList.size() > 0) then {theRuleResult.legBlockTimeList = theLegBlockTimeList.}if (theLastPointOfAcclimationArray <> null and theLastPointOfAcclimationArray.count > 0) then {theRuleResult.lastPointOfAcclimationList = Arrays.asList(theLastPointOfAcclimationArray as a fixed array of LastPointOfAcclimation).}if (theDutyPeriodBlockTimeList <> null and theDutyPeriodBlockTimeList.size() > 0) then {theRuleResult.dutyPeriodBlockTimeList = theDutyPeriodBlockTimeList.}if (theDutyPeriodDutyDurationList <> null and theDutyPeriodDutyDurationList.size() > 0) then {theRuleResult.dutyPeriodDutyDurationList = theDutyPeriodDutyDurationList.}if (theDutyPeriodFDPDurationList <> null and theDutyPeriodFDPDurationList.size() > 0) then {theRuleResult.dutyPeriodFDPDurationList = theDutyPeriodFDPDurationList.}if (theDutyPeriodRestList <> null and theDutyPeriodRestList.size() > 0) then {theRuleResult.dutyPeriodRestList = theDutyPeriodRestList.}if (theTripCalculations <> null) then {theRuleResult.tripCalculations = theTripCalculations.}if (theLegalityLimitList <> null and theLegalityLimitList.size() > 0) then{theRuleResult.legalityLimitList = theLegalityLimitList.}if (theFdpNumberOfLegsList <> null and theFdpNumberOfLegsList.size() > 0) then {theRuleResult.fdpNumberOfLegsList = theFdpNumberOfLegsList }
```

## Historial de cambios

```
5/11/2016 - Mark B - CSCH-2107 - Add theFdpNumberOfLegsList as a parameter.  Add fdpNumberOfLegsList to theRuleResult.
```

