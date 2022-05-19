import random 

player = int(input('[1]Pedra [2]Papel [3]Tesoura '))
maquina = random.randint(1, 3)

if player == 1:
  player = 'Pedra'
elif player == 2:
  player = 'Papel'
else:
  player = 'Tesoura'

if maquina == 1:
  maquina = 'Pedra'
elif maquina == 2:
  maquina = 'Papel'
else:
  maquina = 'Tesoura'

print(f'Você escolheu {player}')
print(f'A máquina escolheu {maquina}')

if maquina == 'Tesoura' and  player == 'Papel':
  print('Você Perdeu :(')
elif maquina == 'Tesoura' and player == 'Pedra':
  print('Você Ganhou :)')
elif maquina == 'Pedra' and player == 'Papel':
  print('Você Ganhou :)')
elif maquina == 'Pedra' and player == 'Tesoura':
  print('Você Perdeu :(')
elif maquina == 'Papel' and player == 'Tesoura':
  print('Você Ganhou :)')
elif maquina == 'Papel' and player == 'Pedra':
  print('Você Perdeu :(')
else:
  print('EMPATE!!')