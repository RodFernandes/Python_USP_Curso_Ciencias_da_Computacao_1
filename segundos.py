segundos = int(input('Por favor, entre com o número de segundos que deseja converter:'))
a = segundos // 86400
segundos_rest = segundos % 86400
b = segundos_rest // 3600
segundos_rest = segundos % 3600
c = segundos_rest  // 60
d = segundos_rest  % 60
print(a,'dias,',b,'horas,',c,'minutos e',d,'segundos.')