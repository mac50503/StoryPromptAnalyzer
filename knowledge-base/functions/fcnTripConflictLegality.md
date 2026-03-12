# fcnTripConflictLegality

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Rulesets\grpTripConflict`

## Propósito
5/4/2015 US20172 Mitesh P - This function creates conflict legality for each set of Trips where there is a conflict, and where the conflict is not allowed.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | LegalityTrip | |
| theRuleResult | RuleResult | |

## Lógica de negocio

```blaze
tripListAsList is some List initially Arrays.asList(theTripList as a fixed array of LegalityTrip).theTripName is a string initially "".theOtherTripName is a string initially "".theOtherTrip is some LegalityTrip.conflictExists is a boolean initially false.// For nonflies we need to use Nonfly code in stead of trip Nameif theTrip.isNonFly =true then theTripName = theTrip.nonFlyCode.else theTripName = theTrip.tripName.for each LegalityTrip in theTripList as an array of LegalityTrip such that ((tripListAsList.indexOf(theTrip) < tripListAsList.indexOf(it) and theTrip.beginDateTime<=it.beginDateTime) and it <> theTrip andit.tripType <> (ignoring case) "R" and it.ghostedFlag = false) do {theOtherTrip = it.conflictExists = rsTripConflictExists(theTrip, theOtherTrip).// For nonflies we need to use Nonfly code instead of trip Nameif (theOtherTrip.isNonFly =true) then theOtherTripName = theOtherTrip.nonFlyCode.elsetheOtherTripName = theOtherTrip.tripName.// If a conflict exists and conflict is not allowedif (conflictExists = true and rsTripConflictAllowed(theTrip, theOtherTrip) = false) then {theRuleResult.ruleMessageList.add(a RuleMessage initially {it.messageText = "(F) "theTripName" at "fcnFormatLegalityDateTime(theTrip.beginDateTime)" conflicts with "theOtherTripName" at "fcnFormatLegalityDateTime(theOtherTrip.beginDateTime),it.ruleId = "F_DtyCon_005",it.ruleType = RuleType.FAR}).}// DE7287 - If a conflict exists and contractual conflict is not allowed (these get the Contractual rule id so they will only show in CWA and not CSS)if (conflictExists = true and rsContractualNonFlyConflictAllowed(theTrip, theOtherTrip) = false) then {theRuleResult.ruleMessageList.add(a RuleMessage initially {it.messageText = "(C) "theTripName" at "fcnFormatLegalityDateTime(theTrip.beginDateTime)" conflicts with "theOtherTripName" at "fcnFormatLegalityDateTime(theOtherTrip.beginDateTime),it.ruleId = "C_DtyCon_001",it.ruleType = RuleType.CC}).}// US21075// Sick conflict rules depend on the same SWA day, not a physical conflict, and they are also classified as Contract legalities, so they will have their own rulesetif (rsSickNonFlyConflictAllowed(theTrip, theOtherTrip, conflictExists) = false) then {theRuleResult.ruleMessageList.add(a RuleMessage initially {it.messageText = "(C) "theTripName" at "fcnFormatLegalityDateTime(theTrip.beginDateTime)" conflicts with "theOtherTripName" at "fcnFormatLegalityDateTime(theOtherTrip.beginDateTime),it.ruleId = "C_DtyCon_001",it.ruleType = RuleType.CC}).}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnFormatLegalityDate](fcnFormatLegalityDate.md)
- [fcnFormatLegalityDateTime](fcnFormatLegalityDateTime.md)

## Historial de cambios

```
5/4/2015 US20172 Mitesh P - This function creates conflict legality for each set of Trips where there is a conflict, and where the conflict is not allowed.
6/18/2015 - Melissa S - DE6875 - conflict with a ghosted trip is allowed
It will call the rulesets rsTripConflictExists and rsTripConflictAllowed to make that determination.
06/03/2015 Corey Gu US21075
7/8/2015 - Melissa S - DE7006/DE7007/DE6995 - Rework of sick nonfly conflict rules
9/3/2015 - Melissa S - DE7287 - Added conflict legality for nonflies in the Contractual Conflict nonfly column
```

