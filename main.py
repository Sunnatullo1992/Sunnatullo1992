#def ism(i):
#     return lambda n:(i+' ')*n
# k=input(" ismni kititing = ")
# na_ta_ism=ism(k)
# print(na_ta_ism(6))
import camelcase
c=camelcase.CamelCase()
txt ="Salom dunyo"
print(c.hump(txt))