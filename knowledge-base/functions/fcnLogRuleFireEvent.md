# fcnLogRuleFireEvent

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\Logging\fcnLogRuleFireEvent`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aRuleName | string | |
| aMetaphorName | string | |
| extraInfo | string | |

## Lógica de negocio

```blaze
if (debugMode) then {if (extraInfo.length() > 0) thenfcnShow("===>>> FIRING RULE " aRuleName " FROM " aMetaphorName ", " extraInfo).elsefcnShow("===>>> FIRING RULE " aRuleName " FROM " aMetaphorName).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Llamado por

- [fcnEnforceLongevityPayMax](fcnEnforceLongevityPayMax.md)
- [fcnSetLegPremiumThisMonth](fcnSetLegPremiumThisMonth.md)

