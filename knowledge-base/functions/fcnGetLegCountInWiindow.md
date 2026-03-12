# fcnGetLegCountInWiindow

## Metadata
- **Tipo**: SRL Function
- **Retorna**: integer
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnGetLegCountInWiindow`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLeg | LegalityLeg | |
| numOfHours | integer | |

## Lógica de negocio

```blaze
legCount is an integer initially 0.// Count the number of legs within the windowif (theLeg <> null and theLeg <> unknown and theLegs <> null and theLegs <> unknown) then {for each LegalityLeg in theLegs as an array of LegalityLeg  do {if (it.legalityDutyPeriod <> null and it.legalityDutyPeriod <> unknown and it.legalityDutyPeriod.legalityTrip <> null and it.legalityDutyPeriod.legalityTrip <> unknown and            it.legalityDutyPeriod.legalityTrip.tripClass <> (ignoring case)  ("C" and "L") and         it.legalityDutyPeriod.legalityTrip.assignmentLabel <> (ignoring case)  ("A" and "C" and "D" and "L" and "Q" and "T" and "S" and "U" and "V" and "X") and            it.scheduledDepartureDateTime <> null and it.scheduledDepartureDateTime <> unknown and theLeg.scheduledDepartureDateTime <> null and theLeg.scheduledDepartureDateTime <> unknown and     it.scheduledDepartureDateTime.isBefore(theLeg.scheduledDepartureDateTime.minusHours(numOfHours)) = false and it.scheduledDepartureDateTime.isAfter(theLeg.scheduledDepartureDateTime) = false) then{legCount = legCount + 1.}}}return legCount.
```

