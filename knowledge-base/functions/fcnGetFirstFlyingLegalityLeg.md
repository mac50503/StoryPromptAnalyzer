# fcnGetFirstFlyingLegalityLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegalityLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnGetFirstFlyingLegalityLeg`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aLegalityTrip | LegalityTrip | |

## Lógica de negocio

```blaze
retVal is some LegalityLeg initially null.if (aLegalityTrip.dutyPeriodList<>null and aLegalityTrip.dutyPeriodList.size()>0) thenretVal = fcnGetFirstFlyLeg(aLegalityTrip.dutyPeriodList.get(0).legList). return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetFirstFlyLeg](fcnGetFirstFlyLeg.md)

