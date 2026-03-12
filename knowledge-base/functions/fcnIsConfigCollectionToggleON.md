# fcnIsConfigCollectionToggleON

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnIsConfigCollectionToggleON`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theToggleKey | string | |

## Lógica de negocio

```blaze
isConfigCollectionToggleON is a boolean initially false.theConfigCollection is some ConfigCollection initially inFlightGlobalVar.configCollection.if(theConfigCollection <> null and theConfigCollection <> unknown and theConfigCollection.toggleMap <> null and theConfigCollection.toggleMap <> unknown and theConfigCollection.toggleMap.containsKey(theToggleKey)) then {  isConfigCollectionToggleON  = theConfigCollection.toggleMap.get(theToggleKey);}return isConfigCollectionToggleON.
```

## Llamado por

- [fcnCreateTripPay](fcnCreateTripPay.md)
- [fcnDetermineDutyPeriodTransientTerms](fcnDetermineDutyPeriodTransientTerms.md)

