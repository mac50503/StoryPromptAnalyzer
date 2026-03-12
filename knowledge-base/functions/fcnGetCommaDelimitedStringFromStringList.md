# fcnGetCommaDelimitedStringFromStringList

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnGetCommaDelimitedStringFromStringList`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| stringList | List<String> | |

## Lógica de negocio

```blaze
returnString is a string initially "";index is an integer initially 0.while (index < stringList.size()) do {if (index > 0) then {returnString = returnString ", ";}returnString = returnString "" stringList.get(index);index = index + 1.}return returnString.
```

