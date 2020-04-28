"""
Knapsack problem:
https://www.kancloud.cn/kancloud/pack/70125

"""

L01: each article can only be used once

N articles, c[i] - cost, w[i] - value
V: volume

how to maximize value??

f[i][v]=max{f[i-1][v],f[i-1][v-c[i]]+w[i]}


for i=1..N
    for v=V..0
        f[v]=max{f[v],f[v-c[i]]+w[i]};


procedure ZeroOnePack(cost,weight)
    for v=V..cost
        f[v]=max{f[v],f[v-cost]+weight}

for i=1..N
    ZeroOnePack(c[i],w[i]);




"""
L02, complete 
"""
L02: each article may be used multiple times

f[i][v]=max{f[i][v],f[i][v-c[i]]+w[i]}

for i=1..N
    for v=0..V
        f[v]=max{f[v],f[v-c[i]]+w[i]};


procedure ZeroOnePack(cost,weight)
    for v=cost..V
        f[v]=max{f[v],f[v-cost]+weight}

for i=1..N
    ZeroOnePack(c[i],w[i]);

