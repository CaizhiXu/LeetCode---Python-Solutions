



##L1
def ZeroOnePack(cost,weight):
    for v=V..cost
        f[v]=max{f[v],f[v-cost]+weight}

##L2
def CompletePack(cost,weight):
    for v=cost..V
        f[v]=max{f[v],f[v-c[i]]+w[i]}

## L3
def MultiplePack(cost,weight,amount):
    if cost*amount>=V
        CompletePack(cost,weight)
        return
    integer k=1
    while k<amount
        ZeroOnePack(k*cost,k*weight)
        amount=amount-k
        k=k*2
    ZeroOnePack(amount*cost,amount*weight)