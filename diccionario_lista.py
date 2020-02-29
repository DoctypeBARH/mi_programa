pizza={'corteza':'gruesa',
        'cobertura':['hongos','extra queso'],
        }
print(f"Ordenaste una pizza con cortesa-{pizza['corteza']}")

for cobertura in pizza ['cobertura']:
    print("\t"+ cobertura)

lenguajes_favoritos={
        'juan':['python','ruby','c+'],
        'sarah':['c','R','ruby'],
        'antonio':['rubyy','python','c#'],
        'norberto':['c#','R','ruby'],
        'braulio':['php','java','python'],
        'jose':['php'],
        'arturo':['python'],
        }
for nombre,lenguajes in lenguajes_favoritos.items():
    c=len(lenguajes)
    if c>1:
        print(f"\n los lenguajes favoritos de {nombre.title()} son:")
        for lenguaje in lenguajes:
            print(f"\t {lenguaje.title()}")
    else:
        print(f"\n El lenguaje favorito de {nombre.title()} son:")
        for lenguaje in lenguajes:
            print(f"\t {lenguaje.title()}")
    