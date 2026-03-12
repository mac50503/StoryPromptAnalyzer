# fcnAssignLegNoPremium

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnAssignLegNoPremium`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aLegPay | LegPay | |

## Lógica de negocio

```blaze
if (aLegPay <> null) thenaLegPay.payValueNoPremium = aLegPay.payValue.
```

