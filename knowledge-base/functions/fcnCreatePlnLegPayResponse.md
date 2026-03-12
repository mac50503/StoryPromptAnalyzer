# fcnCreatePlnLegPayResponse

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PlnLegPayResponse
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\PlanningPay\Functions\fcnCreatePlnLegPayResponse`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPlnLegPayRequest | PlnLegPayRequest | |

## Lógica de negocio

```blaze
retVal is some PlnLegPayResponse initially null.if (aPlnLegPayRequest <> null)  then{//////// CREATE AN EMPTY RESPONSE OBJECT...////retVal = a PlnLegPayResponse.//////// CREATE RESPONSE LEG OBJECT AND XREF REQUEST LEG TO RESPONSE LEG...////aPlnLegPay is a PlnLegPay.aPlnLegPayRequest.plnPayLeg.plnLegPay = aPlnLegPay.aPlnLegPay.payLeg = aPlnLegPayRequest.plnPayLeg.aPlnLegPay.sequenceNumber = aPlnLegPayRequest.plnPayLeg.sequenceNumber.aPlnLegPay.basePay = aPlnLegPayRequest.plnPayLeg.basePay.aPlnLegPay.creditType = aPlnLegPayRequest.plnPayLeg.creditType.//////// XREF RESPONSE LEG TO REQUEST RESPONSE OBJECT...////retVal.plnLegPay = aPlnLegPay.}return retVal.
```

