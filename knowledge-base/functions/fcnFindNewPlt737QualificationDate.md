# fcnFindNewPlt737QualificationDate

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Qualifications\Functions\fcnFindNewPlt737QualificationDate`

## Propósito
7/20/2015 - Melissa S - US21136 - Moved functionality here from the plt737Rule so it can be used by multiple rules

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLegalityLegs | List<LegalityLeg> | |
| anyQualification | Qualification | |
| theQualificationResult | QualificationResult | |

## Lógica de negocio

```blaze
qualifiedLegs is an integer initially 0.resultEffectiveDateTime is some DateTime.legIndex is an integer initially theLegalityLegs.size() - 1.while (legIndex >= 0) do {if (theLegalityLegs.get(legIndex).actualInDateTime <> null and    theLegalityLegs.get(legIndex).isDeadhead = false and    theLegalityLegs.get(legIndex).nonFlyCode = ("" or (null as a string)) and    theLegalityLegs.get(legIndex).onReserveBlock = false and    (theLegalityLegs.get(legIndex).legWorkCodeList = null or       (theLegalityLegs.get(legIndex).legWorkCodeList <> null and theLegalityLegs.get(legIndex).legWorkCodeList.contains("GR") = false)    )) then {qualifiedLegs +=1.if (qualifiedLegs = 3) then {resultEffectiveDateTime = theLegalityLegs.get(legIndex).actualInDateTime.if (resultEffectiveDateTime.withHourOfDay(0).withMinuteOfHour(0).isAfter(anyQualification.qualificationEffectiveDateTime)) then {fcnAddQualificationToResult(anyQualification, resultEffectiveDateTime, 89, theQualificationResult).}// Exit Loop after the first group of 3 legs meeting the PLT737 conditions is foundlegIndex = 0.}}legIndex -= 1.}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnAddQualificationToResult](fcnAddQualificationToResult.md)

## Historial de cambios

```
7/20/2015 - Melissa S - US21136 - Moved functionality here from the plt737Rule so it can be used by multiple rules
```

