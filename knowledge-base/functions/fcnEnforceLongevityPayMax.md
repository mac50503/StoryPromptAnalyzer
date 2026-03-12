# fcnEnforceLongevityPayMax

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnEnforceLongevityPayMax`

## Propósito
10/06/2014 Corey Gu US18522 - Initiall development

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSchedulePeriodPay | SchedulePeriodPay | |
| thePayCrewMember | PayCrewMember | |

## Lógica de negocio

```blaze
if (thePayCrewMember.payCrewMemberInflight <> null and theSchedulePeriodPay.schedulePeriodPayInflight <> null and thePayCrewMember.payCrewMemberInflight.longevityFlag) then{theLPMax is a real initially math().max(theSchedulePeriodPay.schedulePeriod.originalLineCredits, theSchedulePeriodPay.schedulePeriodPayInflight.totalMonthlyGuaranteeTfpCredited). fcnShow("Reserve guarantee = " theSchedulePeriodPay.reserveGuaranty "...Reserve remaining guarantee = " theSchedulePeriodPay.remainingReserveGuaranty "...theLPMax " theLPMax "...originalLineCredits "  theSchedulePeriodPay.schedulePeriod.originalLineCredits "...totalMonthlyGuaranteeTfpCredited " theSchedulePeriodPay.schedulePeriodPayInflight.totalMonthlyGuaranteeTfpCredited);if (theSchedulePeriodPay.getPayBucket("LPBUCKET") <> null and theSchedulePeriodPay.getPayBucket("LPBUCKET").payValue > theLPMax) then {fcnShow("===> LP Bucket payValue before enforcing pay max = " theSchedulePeriodPay.getPayBucket("LPBUCKET").payValue).theSchedulePeriodPay.getPayBucket("LPBUCKET").payValue = theLPMax.theSchedulePeriodPay.getPayBucket("LPBUCKET").baseValue = theLPMax.fcnLogRuleFireEvent("ruleLongevity", "fcnEnforceLongevityPayMax", "...LP Bucket payValue = " theSchedulePeriodPay.getPayBucket("LPBUCKET").payValue).}fcnShow("===> function fcnEnforceLongevityBucket …theLPMax = " theLPMax "...LP Bucket payValue = " theSchedulePeriodPay.getPayBucket("LPBUCKET").payValue "...Line Credts = " theSchedulePeriodPay.schedulePeriod.originalLineCredits "...Monthly Gurantee Tfp Credite Total = " theSchedulePeriodPay.schedulePeriodPayInflight.totalMonthlyGuaranteeTfpCredited).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnLogRuleFireEvent](fcnLogRuleFireEvent.md)
- `fcnShow()`
- [main](main.md)

## Llamado por

- [fcnCalculateLongevityBucket](fcnCalculateLongevityBucket.md)

## Historial de cambios

```
10/06/2014 Corey Gu US18522 - Initiall development
```

