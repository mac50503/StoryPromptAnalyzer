# fcnReserveBlockTripConflictLegality

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Rulesets\grpReserveBlockConflict`

## Propósito
5/4/2015 US20172 Lohit B - This function creates conflict legality for each Reserve Block and Nonfly combination where there is a conflict, and where the conflict is not allowed.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theReserveBlock | LegalityDutyPeriod | |
| theRuleResult | RuleResult | |

## Lógica de negocio

```blaze
theOtherTrip is some LegalityTrip.theOtherTripName is a string initially "".conflictExists is a boolean initially false.// For FAR conflict nonflies that are NOT allowed to conflictfor each LegalityTrip in theTripList such that (it.isConflictNonFly=true and it.nonFlyCode <> (ignoring case) ("RNU") and it.nonFlyCode <> (ignoring case) ("RNUH") and it.nonFlyCode <> (ignoring case) ("LINK") and it.ghostedFlag = false) do {theOtherTrip = it.// For nonflies we need to use Nonfly code instead of trip Nameif (theOtherTrip.isNonFly =true) then theOtherTripName = theOtherTrip.nonFlyCode.elsetheOtherTripName = theOtherTrip.tripName.if (rsReserveBlockTripConflictExists(theReserveBlock, theOtherTrip)=true) then {// Reserve Block - Nonfly Conflict Legalityif (theReserveBlock.reportDateTime<=theOtherTrip.beginDateTime) then {theRuleResult.ruleMessageList.add(a RuleMessage initially { it.messageText = "(F) "theReserveBlock.legalityTrip.tripName" at "fcnFormatLegalityDateTime(theReserveBlock.reportDateTime)" conflicts with "theOtherTripName" at "fcnFormatLegalityDateTime(theOtherTrip.beginDateTime),it.ruleId = "F_DtyCon_005",it.ruleType = RuleType.FAR}).// Nonfly - Reserve Block Conflict Legality} else {theRuleResult.ruleMessageList.add(a RuleMessage initially { it.messageText = "(F) " theOtherTripName " at "fcnFormatLegalityDateTime(theOtherTrip.beginDateTime)" conflicts with "theReserveBlock.legalityTrip.tripName" at "fcnFormatLegalityDateTime(theReserveBlock.reportDateTime),it.ruleId = "F_DtyCon_005",it.ruleType = RuleType.FAR}).}}}// DE7287 - For Contractual Conflict nonflies that are NOT allowed to conflict//CREWT-4 Adding ETO which are NOT allowed to conflictfor each LegalityTrip in theTripList such that ((it.isContractualConflictNonFly=true and it.nonFlyCode <> (ignoring case) ("RNU") and it.nonFlyCode <> (ignoring case) ("RNUH") and it.nonFlyCode <> (ignoring case) ("LINK") and it.ghostedFlag = false) or it.isETONonFly = true) do {theOtherTrip = it.// For nonflies we need to use Nonfly code instead of trip Nameif (theOtherTrip.isNonFly =true) then theOtherTripName = theOtherTrip.nonFlyCode.elsetheOtherTripName = theOtherTrip.tripName.if (rsReserveBlockTripConflictExists(theReserveBlock, theOtherTrip)=true) then {// Reserve Block - Contractual Conflict Nonfly - Conflict Legalityif (theReserveBlock.reportDateTime<=theOtherTrip.beginDateTime) then {theRuleResult.ruleMessageList.add(a RuleMessage initially { it.messageText = "(C) "theReserveBlock.legalityTrip.tripName" at "fcnFormatLegalityDateTime(theReserveBlock.reportDateTime)" conflicts with "theOtherTripName" at "fcnFormatLegalityDateTime(theOtherTrip.beginDateTime),it.ruleId = "C_DtyCon_001",it.ruleType = RuleType.CC}).// Nonfly - Reserve Block Conflict Legality} else {theRuleResult.ruleMessageList.add(a RuleMessage initially { it.messageText = "(C) " theOtherTripName " at "fcnFormatLegalityDateTime(theOtherTrip.beginDateTime)" conflicts with "theReserveBlock.legalityTrip.tripName" at "fcnFormatLegalityDateTime(theReserveBlock.reportDateTime),it.ruleId = "C_DtyCon_001",it.ruleType = RuleType.CC}).}}}// US21075for each LegalityTrip in theTripList such that (it.isSickNonFly = true and it.ghostedFlag = false) do {theOtherTrip = it.conflictExists = rsReserveBlockTripConflictExists(theReserveBlock, theOtherTrip).if (rsReserveBlockSickNonFlyConflictAllowed(theReserveBlock, it, conflictExists) = false) then {if (theReserveBlock.reportDateTime <= it.beginDateTime) then {// Create Conflict legality message C_DtyCon_001 using the reserve block’s trip’s name and reserve block’s reportDateTime for the first trip in the message, and it’s tripName/beginDateTime as the second trip in the message and add to theRuleResulttheRuleResult.ruleMessageList.add(a RuleMessage initially { it.messageText = "(C) "theReserveBlock.legalityTrip.tripName" at "fcnFormatLegalityDateTime(theReserveBlock.reportDateTime)" conflicts with "theOtherTrip.nonFlyCode" at "fcnFormatLegalityDateTime(theOtherTrip.beginDateTime),it.ruleId = "C_DtyCon_001",it.ruleType = RuleType.CC}).} else {// Sick Nonfly - Reserve Block Conflict LegalitytheRuleResult.ruleMessageList.add(a RuleMessage initially {it.messageText = "(C) " theOtherTrip.nonFlyCode " at "fcnFormatLegalityDateTime(theOtherTrip.beginDateTime)" conflicts with "theReserveBlock.legalityTrip.tripName" at "fcnFormatLegalityDateTime(theReserveBlock.reportDateTime),it.ruleId = "C_DtyCon_001",it.ruleType = RuleType.CC}).}}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnFormatLegalityDate](fcnFormatLegalityDate.md)
- [fcnFormatLegalityDateTime](fcnFormatLegalityDateTime.md)

## Historial de cambios

```
5/4/2015 US20172 Lohit B - This function creates conflict legality for each Reserve Block and Nonfly combination where there is a conflict, and where the conflict is not allowed.
It calls the ruleset rsReserveBlockTripConflictExists to make that determination.
5/14/2015 - DE6607 - Melissa S - Added exception for RNU nonfly - allowed to conflict with reserve blocks
6/4/2015 Corey Gu - US21075
6/18/2015 - Melissa S - DE6875 - conflict with a ghosted trip is allowed
7/29/2015 - Melissa S - DE7076 / DE7105 - Added conflict legality for Reserve Blocks with Flying Trips that don't have an R label
9/3/2015 - Melissa S - DE7287 - Added conflict legality for Reserve Blocks with Nonflies in the Contractual Conflict nonfly column
11/24/2020 - Rachel S - CREWT-4 Adding conflict for ETO with reserves
5/13/2021 - Rachel S - CREWT-185 - Adding RNUH to behave like RNU
6/5/23 - Alex F - APIC-738 - Adding LINK to behave like CC
```

