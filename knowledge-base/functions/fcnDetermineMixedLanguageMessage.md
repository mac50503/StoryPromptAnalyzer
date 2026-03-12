# fcnDetermineMixedLanguageMessage

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnDetermineMixedLanguageMessage`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | LegalityTrip | |

## Lógica de negocio

```blaze
count is an integer initially 0;result is a string initially "";while (count < theTrip.languageMap.size()) do {if (count>0) then {result = result", ";}key is a string initially theTrip.languageMap.keySet().toArray()[count] as a string;legalityLeg is some LegalityLeg initially theTrip.languageMap.get(key);result = result"Language "key" on flight "legalityLeg.flightNumber" at "fcnFormatLegalityDateTime(legalityLeg.scheduledDepartureDateTime);count = count+1;}return result;
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnFormatLegalityDate](fcnFormatLegalityDate.md)
- [fcnFormatLegalityDateTime](fcnFormatLegalityDateTime.md)

