--[[
Esse algoritmo surgiu de uma discussão em um grupo de Lua sobre como implementar o SWIFT CASE em Lua
]]
calendario={
            ["janeiro"]=31, 
            ["fevereiro"]=28, 
            ["março"]=31,
            ["abril"]=30,
            ["maio"]=31,
            ["junho"]=30,
            ["julho"]=31,
            ["agosto"]=31,
            ["setembro"]=30,
            ["outubro"]=31,
            ["novembro"]=30,
            ["dezembro"]=31
            }

print("Digite um mês")
x=io.read()
io.write(x, " possui ", calendario[x], " dias")
