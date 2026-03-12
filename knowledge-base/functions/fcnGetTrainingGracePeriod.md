# fcnGetTrainingGracePeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnGetTrainingGracePeriod`

## Propósito
02/16/2015 Corey Gu US16611 - Changed to return  the grace period end based on it’s qualification date.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theQualificationsList | List<Qualification> | |
| theCrewMemberLine | LegalityCrewMemberLine | |

## Lógica de negocio

```blaze
qualCounter is an integer initially 0.aQualification is some Qualification initially null.nextSPIndex is an integer initially 0.if (theQualificationsList <> null) then {while (qualCounter < theQualificationsList.size()) do {aQualification = theQualificationsList.get(qualCounter).if (aQualification.qualificationType = (ignoring case) "RT") then {if(theCrewMemberLine.crewMember <> null and theCrewMemberLine.crewMember.rtMonth <> null) then {return theCrewMemberLine.crewMember.rtMonth.}else {// US16611// Return the grace period end based on its qualification date.  nextSPIndex = theCrewMemberLine.getNextLegalitySchedulePeriodIndexForDate(aQualification.qualificationEffectiveDateTime).if (nextSPIndex > -1) then {return (theCrewMemberLine.schedulePeriodList.get(nextSPIndex).schedulePeriodEnd).} else {// DE6040 - If no next schedule period is found, use the qualification's effective date timereturn aQualification.qualificationEffectiveDateTime.}}}qualCounter+=1;}}return null.
```

## Historial de cambios

```
02/16/2015 Corey Gu US16611 - Changed to return  the grace period end based on it’s qualification date.
The grace period end will be the end of the next schedule period after the one the qualificationEffectiveDateTime falls under.
03/06/2015 - Melissa S - DE6040 - Fix for Training Qual to set the grace period end to the training qual effective date if no next schedule period can be found.
8/11/2015 - Melissa S - DE7209 - Fixed to handle a null qualifications list
4/2/2018 - Rachel S - CREW-6720 - Adding RT Month concept
```

