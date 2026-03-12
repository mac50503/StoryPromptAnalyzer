# fcnAddQualificationToResult

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Qualifications\Functions\fcnAddQualificationToResult`

## Propósito
11/4/2014 - MS - US18846

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theExistingQualification | Qualification | |
| theEffectiveDate | DateTime | |
| plusDays | integer | |
| theQualificationResult | QualificationResult | |

## Lógica de negocio

```blaze
newQualificationTime is some QualificationTime initially a QualificationTime.newQualificationTime.qualificationType = theExistingQualification.qualificationType.newQualificationTime.subQualification = theExistingQualification.subQualification.newQualificationTime.qualificationEffectiveDateTime = theEffectiveDate.withHourOfDay(0).withMinuteOfHour(0).withSecondOfMinute(0).if (plusDays >= 0) then {newQualificationTime.qualificationExpirationDateTime = newQualificationTime.qualificationEffectiveDateTime.plusDays(plusDays).withHourOfDay(23).withMinuteOfHour(59).}theQualificationResult.addQualificationTime(newQualificationTime).
```

## Llamado por

- [fcnFindNewPlt737QualificationDate](fcnFindNewPlt737QualificationDate.md)

## Historial de cambios

```
11/4/2014 - MS - US18846
6/15/2014 - DE6814 - Melissa S - Special Station Quals should include the effectiveDate as "Day 1", so we have to use expiresInDays-1 for the expiration date calculation.
Because of that, 0 will now be a valid case to return an expiration date time.
10/3/2016 - RS - CSCH-3918 - Setting SecondOfMinute to 0 for new qualification time.
```

