# fcnGetPayCrewMemberBySchedulePeriodName

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayCrewMember
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetPayCrewMemberBySchedulePeriodName`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayCrewMemberList | List<PayCrewMember> | |
| schedPeriodName | string | |

## Lógica de negocio

```blaze
if (aPayCrewMemberList <> null and aPayCrewMemberList.size() > 0) then {for each PayCrewMember in aPayCrewMemberList as an array of PayCrewMember do {if (it.schedulePeriodName =(ignoring case) schedPeriodName) thenreturn it.}}return null.
```

## Llamado por

- [fcnCalculateLongevityBucket](fcnCalculateLongevityBucket.md)
- [fcnCreateCrewPayResponse](fcnCreateCrewPayResponse.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

