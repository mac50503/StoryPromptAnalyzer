# fcnAnyLegCountryMatchesAnyDeniedQualification

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnAnyLegCountryMatchesAnyDeniedQualification`

## Propósito
8/23/2013 - US13715 - Melissa S - Performance enhancements

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | LegalityTrip | |

## Lógica de negocio

```blaze
dutyPeriodCounter is an integer initially 0.legCounter is an integer initially 0.if (theQualificationsList <> null) then {for each Qualification in theQualificationsList do {if (it.qualificationEffectiveDateTime <> null and it.qualificationEffectiveDateTime <> unknown and it.containsQualificationType("DENIED")) then {if (// Qualification starts before or equal to the Trip start// AND// There is no qualification expiration or the qualification expiration is after or equal to the trip start((it.qualificationEffectiveDateTime.isBefore(theTrip.beginDateTime) or it.qualificationEffectiveDateTime.isEqual(theTrip.beginDateTime)) and ((it.qualificationExpirationDateTime = null or it.qualificationExpirationDateTime = unknown) or (it.qualificationExpirationDateTime <> null and it.qualificationExpirationDateTime <> unknown and (it.qualificationExpirationDateTime.isAfter(theTrip.beginDateTime) or it.qualificationExpirationDateTime.isEqual(theTrip.beginDateTime)))))or// Qualification starts before or equal to the Trip end// AND// There is no qualification expiration or the qualification expiration is after or equal to the trip end((it.qualificationEffectiveDateTime.isBefore(theTrip.endDateTime) or it.qualificationEffectiveDateTime.isEqual(theTrip.endDateTime)) and (it.qualificationEffectiveDateTime.isAfter(theTrip.beginDateTime)))) then {if (theTrip.dutyPeriodList <> null) then {dutyPeriodCounter = 0.while (dutyPeriodCounter < theTrip.dutyPeriodList.size()) do {if (theTrip.dutyPeriodList.get(dutyPeriodCounter).legList <> null) then {legCounter = 0.while (legCounter < theTrip.dutyPeriodList.get(dutyPeriodCounter).legList.size()) do {if (it.containsDeniedCountry(theTrip.dutyPeriodList.get(dutyPeriodCounter).legList.get(legCounter).countryCode)) then {return true.}legCounter = legCounter + 1.}}dutyPeriodCounter = dutyPeriodCounter + 1.}}}}}}return false.
```

## Historial de cambios

```
8/23/2013 - US13715 - Melissa S - Performance enhancements
4/10/2014 - DE3503/DE3508 - Blaze not reading Denied Entry's disqualification time
8/11/2015 - Melissa S - DE7209 - Fixed to handle a null qualifications list
fcnShow("Leg Country code = " theTrip.dutyPeriodList.get(dutyPeriodCounter).legList.get(legCounter).countryCode).
fcnShow("Denied code = " it.deniedCountry).
fcnShow("Country code exists = " it.containsDeniedCountry(theTrip.dutyPeriodList.get(dutyPeriodCounter).legList.get(legCounter).countryCode)).
fcnShow("QualificationType exists = " it.containsQualificationType("DENIED")).
if(it.qualificationEffectiveDateTime &lt;&gt; null) then fcnShow("qualificationEffectiveDateTime = " it.qualificationEffectiveDateTime.toString()).
if(it.qualificationExpirationDateTime &lt;&gt; null) then fcnShow("qualificationExpirationDateTime = " it.qualificationExpirationDateTime.toString()).
fcnShow("dutyPeriodCounter = " dutyPeriodCounter).
fcnShow("legCounter = " legCounter).
```

