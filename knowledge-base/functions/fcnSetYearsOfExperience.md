# fcnSetYearsOfExperience

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnSetYearsOfExperience`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayCrewMember | PayCrewMember | |
| theSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
if (thePayCrewMember <> null and thePayCrewMember.payCrewMemberInflight <> null and theSchedulePeriodPay <> null) then{thePayCrewMember.payCrewMemberInflight.yearsOfExperience = Years.yearsBetween(thePayCrewMember.payCrewMemberInflight.seniorityDateTime, theSchedulePeriodPay.schedulePeriod.schedulePeriodStart.plusDays(15).withDayOfMonth(15)).years.fcnShow("===>>> SP = "  theSchedulePeriodPay.schedulePeriodName " ...crew member = " thePayCrewMember.crewId " ...setting years of experience to " thePayCrewMember.payCrewMemberInflight.yearsOfExperience ).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

