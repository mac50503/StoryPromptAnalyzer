# fcnGetPayLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetPayLeg`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayLegList | List<PayLeg> | |
| theLegCounter | integer | |

## Lógica de negocio

```blaze
return thePayLegList.get(theLegCounter).
```

