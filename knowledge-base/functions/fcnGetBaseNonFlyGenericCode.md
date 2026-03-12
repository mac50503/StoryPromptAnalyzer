# fcnGetBaseNonFlyGenericCode

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnGetBaseNonFlyGenericCode`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| nonFlyCode | string | |

## Lógica de negocio

```blaze
baseNonFlyGenericCode is a string initially null.if((nonFlyCode <> null and nonFlyCode <> unknown and((nonFlyCode.startsWith("RT") and nonFlyCode <> "RTS") or nonFlyCode.endsWith("ST8")or nonFlyCode.endsWith("STW")))) then {if(nonFlyCode.endsWith("ST8")) then {baseNonFlyGenericCode = "ST8".} else if (nonFlyCode.endsWith("STW")) then {baseNonFlyGenericCode = "STW".} else {baseNonFlyGenericCode = "RT".}}return baseNonFlyGenericCode.
```

## Llamado por

- [fcnCalculateExperiencePayBucket](fcnCalculateExperiencePayBucket.md)
- [fcnCalculateTripDutyHours](fcnCalculateTripDutyHours.md)
- [fcnGetNonflyDefaultCredits](fcnGetNonflyDefaultCredits.md)
- [fcnIsPremiumNonFly](fcnIsPremiumNonFly.md)
- [fcnNonflyIsNonflyType](fcnNonflyIsNonflyType.md)

