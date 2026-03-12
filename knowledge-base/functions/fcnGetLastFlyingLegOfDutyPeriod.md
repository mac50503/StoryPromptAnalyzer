# fcnGetLastFlyingLegOfDutyPeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetLastFlyingLegOfDutyPeriod`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
legCounter is an integer initially 0;aPayLeg is some PayLeg initially null.if(aPayDutyPeriod.legList<>null and aPayDutyPeriod.legList.size()>0)then{legCounter = aPayDutyPeriod.legList.size()-1;while(legCounter >=0) do{if((aPayDutyPeriod.legList.get(legCounter).nonFlyCode = null as a string or                                                                         aPayDutyPeriod.legList.get(legCounter).nonFlyCode = "" or                                                                           aPayDutyPeriod.legList.get(legCounter).nonFlyCode is unknown))then return aPayDutyPeriod.legList.get(legCounter).legCounter-=1;}}return aPayLeg
```

## Llamado por

- [fcnCalculateCrewMealPerdiumInternational](fcnCalculateCrewMealPerdiumInternational.md)

