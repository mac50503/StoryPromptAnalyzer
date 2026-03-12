# fcnGetFirstFlyLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegalityLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnGetFirstFlyLeg`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLegList | List<LegalityLeg> | |

## Lógica de negocio

```blaze
legCounter is an integer initially 0.while(legCounter < theLegList.size()) do{if(theLegList.get(legCounter).nonFlyCode = null or theLegList.get(legCounter).nonFlyCode = unknown or theLegList.get(legCounter).nonFlyCode ="") then {return theLegList.get(legCounter).}else legCounter = legCounter + 1.}return null.
```

## Llamado por

- [fcnGetFirstFlyingLegalityLeg](fcnGetFirstFlyingLegalityLeg.md)

