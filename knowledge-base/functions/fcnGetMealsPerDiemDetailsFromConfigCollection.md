# fcnGetMealsPerDiemDetailsFromConfigCollection

## Metadata
- **Tipo**: SRL Function
- **Retorna**: CrewPerDiemMeal
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetMealsPerDiemDetailsFromConfigCollection`

## Propósito
5/06/2024 - Namratha- APIC-1102- FunctionTo Return Matching CrewMealPerdim Wrt EffectiveDate

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDateTime | DateTime | |

## Lógica de negocio

```blaze
theConfigCollection is some ConfigCollection initially inFlightGlobalVar.configCollection.if(theConfigCollection <> null and theConfigCollection <> unknown and theDateTime <> null and theDateTime <> unknown and theConfigCollection.crewPerDiemMeals <> null and theConfigCollection.crewPerDiemMeals <> unknown and  theConfigCollection.crewPerDiemMeals.crewPerdiemMealList <> null) then {for each CrewPerDiemMeal in theConfigCollection.crewPerDiemMeals.crewPerdiemMealList as an array of CrewPerDiemMeal do{if((theDateTime.isAfter(it.effectiveDateTime) or theDateTime.isEqual(it.effectiveDateTime)) and (theDateTime.isBefore(it.endDateTime) or theDateTime.isEqual(it.endDateTime))) then {return it.}}}return null;
```

## Llamado por

- [fcnCalculateCrewMealPerdiem](fcnCalculateCrewMealPerdiem.md)

## Historial de cambios

```
5/06/2024 - Namratha- APIC-1102- FunctionTo Return Matching CrewMealPerdim Wrt EffectiveDate
```

