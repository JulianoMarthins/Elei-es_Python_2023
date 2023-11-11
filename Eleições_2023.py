from random import randint
from time import sleep

print('\n\n')
 
# 156454011 -> Número de votantes no brasil sengundo TSE
eleitores =  1564540 # retirei dois digito para o programa ficar mais agil

bolsonaro = 0
lula = 0
ciro = 0

contador = eleitores
votos_apurados = 0
contador_votos = 0

print('\033[1;34mELEIÇÔES 2023 EM PYTHON\033[m')

print('\033[1;32m\nCandidatos\n21 - Bolsonaro\n12 - Ciro Gomes\n13 - Lula\n\033[m')

while contador > 0:

    voto = randint(0, 2)
    contador_votos += 1

    votos_apurados = contador_votos * 100 / eleitores
    print(f'Votos apurados: {votos_apurados:.2f} %',end='\r')
   

    match voto:
        case 0:
            bolsonaro += 1
            contador -= 1
            continue
        case 1:
            ciro += 1
            contador -= 1
            continue
        case 2:
            lula += 1
            contador -= 1
            continue
        case _:
            print('Candidato inexistente')

    
            
print('\n')

print('\n\033[1;034mE o vencedor das eleições Python 2023 é......\033[m ')
sleep(2)

print('\n')

porcento_bolsonaro = bolsonaro * 100 / eleitores
porcento_lula = lula * 100 / eleitores
porcento_ciro = ciro * 100 / eleitores

if lula < bolsonaro > ciro: # Bolsonaro ganha
    print(f'\033[1;32m1° Lugar: Bolsonaro\033[m com {bolsonaro} votos e {porcento_bolsonaro:.2f} %')
    
    if lula > ciro:
        print(f'\033[1;33m2° Lugar: Lula\033[m com {lula} votos e {porcento_lula:.2f} %')
        print(f'\033[1;31m3° Lugar: Ciro Gomes\033[m com {ciro} votos e {porcento_ciro:.2f} %')

    elif ciro > lula:
        print(f'\033[1;33m2° Lugar: Ciro Gomes\033[m com {ciro} votos e {porcento_ciro:.2f} %')
        print(f'\033[1;31m3° Lugar: Lula\033[m com {lula} votos e {porcento_lula:.2f} %')
    

elif bolsonaro < ciro > lula:
    print(f'\033[1;32m1° Lugar: Ciro Gomes\033[m com {ciro} votos e {porcento_ciro:.2f} %')
    
    if lula > bolsonaro:
        print(f'\033[1;33m2° Lugar: Lula\033[m com {lula} votos e {porcento_lula:.2f} %')
        print(f'\033[1;31m3° Lugar: Bolsonaro\033[m com {bolsonaro} votos e {porcento_bolsonaro:.2f} %')

    elif bolsonaro > lula:
        print(f'\033[1;33m2° Lugar: Bolsonaro\033[m com {bolsonaro} votos e {porcento_bolsonaro:.2f} %')
        print(f'\033[1;31m3° Lugar: Lula\033[m com {lula} votos e {porcento_lula:.2f} %')
    

elif bolsonaro < lula > ciro:
    print(f'\033[1;32m1° Lugar: Lula\033[m com {lula} votos e {porcento_lula:.2f} %')
    
    if bolsonaro > ciro:
        print(f'\033[1;33m2° Lugar: Bolsonaro\033[m com {bolsonaro} votos e {porcento_bolsonaro:.2f} %')
        print(f'\033[1;31m3° Lugar: Ciro Gomes\033[m com {ciro} votos e {porcento_ciro:.2f} %')

    elif ciro > bolsonaro:
        print(f'\033[1;33m2° Lugar: Ciro Gomes\033[m com {ciro} votos e {porcento_ciro:.2f} %')
        print(f'\033[1;31m3° Lugar: Bolsonaro\033[m com {bolsonaro} votos e {porcento_bolsonaro:.2f} %')
    

elif bolsonaro == lula or lula == ciro or ciro == bolsonaro:
    print('Eleições empatadas ')

print('\n')
