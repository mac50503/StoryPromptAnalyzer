# fcnShowRuleMessages

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnShowRuleMessages`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aRuleResult | RuleResult | |

## Lógica de negocio

```blaze
origDebugMode is a boolean initially debugMode.debugMode = true.if (aRuleResult <> null and aRuleResult.ruleMessageList <> null) thenif (aRuleResult.ruleMessageList.size() > 0) then{if (aRuleResult.ruleMessageList.size() = 1) thenfcnShow("===>>> Rule result contains " aRuleResult.ruleMessageList.size() " Rule Message...").elsefcnShow("===>>> Rule result contains " aRuleResult.ruleMessageList.size() " Rule Messages...").for each RuleMessage in aRuleResult.ruleMessageList as an array of RuleMessage do{fcnShow("===>>> Rule Message: " it.messageText " ....RuleId: " it.ruleId " ...legalityValueInMinutes = " it.legalityValueInMinutes).}}elsefcnShow("===>>> Rule result contains no rule messages...").debugMode = origDebugMode.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

