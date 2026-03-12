# fcnMaxPremiumPayCode

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnMaxPremiumPayCode`

## Propósito
US16813 - MP - 06/17/2014. This function is used to determine the maximum premium pay code value.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theCurrentPremiumPayCode | string | |
| theProposedPremiumPayCode | string | |

## Lógica de negocio

```blaze
theCurrentPremiumPayMultiplier is a real initially dtDetermineLegPremiumMultiplier(theCurrentPremiumPayCode).theProposedPremiumPayMultiplier is a real initially dtDetermineLegPremiumMultiplier(theProposedPremiumPayCode).if (theProposedPremiumPayMultiplier > theCurrentPremiumPayMultiplier) thenreturn theProposedPremiumPayCode.else return theCurrentPremiumPayCode.
```

## Historial de cambios

```
US16813 - MP - 06/17/2014. This function is used to determine the maximum premium pay code value.
```

