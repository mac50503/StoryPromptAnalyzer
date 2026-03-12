# fcnAnyLegMatchesDeniedPRIQualification

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnAnyLegMatchesDeniedPRIQualification`

## Propósito
8/4/2015 - DE7172 - Melissa S - New function for DENIED PRI qual - Puerto Rico has a US country code, but the denied qual indicates PR.  So Blaze has to do a different match than the normal Denied Qual match

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | LegalityTrip | |

## Lógica de negocio

```blaze
puertoRicoAirportCodes is a string initially ";SJU;BQN;PSE;SIG;VQS;MAZ;ARE;NRR;CPX;FAJ;HUC;".dutyPeriodCounter is an integer initially 0.legCounter is an integer initially 0.if (theQualificationsList <> null) then {for each Qualification in theQualificationsList do {// Denied PRI Qual - Because Puerto Rico has a country code of US for Flight Attendants, it must be handled separatelyif (it.qualificationEffectiveDateTime <> null and it.qualificationEffectiveDateTime <> unknown and     it.containsQualificationType("DENIED") and it.containsDeniedCountry("PR")) then {if (// Qualification starts before or equal to the Trip start// AND// There is no qualification expiration or the qualification expiration is after or equal to the trip start((it.qualificationEffectiveDateTime.isBefore(theTrip.beginDateTime) or it.qualificationEffectiveDateTime.isEqual(theTrip.beginDateTime)) and ((it.qualificationExpirationDateTime = null or it.qualificationExpirationDateTime = unknown) or (it.qualificationExpirationDateTime <> null and it.qualificationExpirationDateTime <> unknown and (it.qualificationExpirationDateTime.isAfter(theTrip.beginDateTime) or it.qualificationExpirationDateTime.isEqual(theTrip.beginDateTime)))))or// Qualification starts before or equal to the Trip end// AND// There is no qualification expiration or the qualification expiration is after or equal to the trip end((it.qualificationEffectiveDateTime.isBefore(theTrip.endDateTime) or it.qualificationEffectiveDateTime.isEqual(theTrip.endDateTime)) and (it.qualificationEffectiveDateTime.isAfter(theTrip.beginDateTime)))) then {if (theTrip.dutyPeriodList <> null) then {dutyPeriodCounter = 0.while (dutyPeriodCounter < theTrip.dutyPeriodList.size()) do {if (theTrip.dutyPeriodList.get(dutyPeriodCounter).legList <> null) then {legCounter = 0.while (legCounter < theTrip.dutyPeriodList.get(dutyPeriodCounter).legList.size()) do {if (theTrip.dutyPeriodList.get(dutyPeriodCounter).legList.get(legCounter).countryCode = (ignoring case) "US" and    (puertoRicoAirportCodes contains match (ignoring case)";"theTrip.dutyPeriodList.get(dutyPeriodCounter).legList.get(legCounter).departureLocation";" or     puertoRicoAirportCodes contains match (ignoring case)";"theTrip.dutyPeriodList.get(dutyPeriodCounter).legList.get(legCounter).arrivalLocation";")) then {return true.}legCounter = legCounter + 1.}}dutyPeriodCounter = dutyPeriodCounter + 1.}}}}}}return false.
```

## Historial de cambios

```
8/4/2015 - DE7172 - Melissa S - New function for DENIED PRI qual - Puerto Rico has a US country code, but the denied qual indicates PR.  So Blaze has to do a different match than the normal Denied Qual match
8/11/2015 - Melissa S - DE7209 - Fixed to handle a null qualifications list
```

