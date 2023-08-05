from camelcase  import CamelCase

instaciaCC = CamelCase("al","mundo")

texto = "Bienvenidos al mundo backend"

print(instaciaCC.hump(texto))