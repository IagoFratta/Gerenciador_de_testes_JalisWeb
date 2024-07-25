from datetime import datetime

# Definindo os timestamps como strings
data_chamada_senha = "2024-07-24 14:10:28.000"
data_retirada_senha = "2024-07-24 14:09:54.000"

# Convertendo as strings para objetos datetime
timestamp1 = datetime.strptime(data_chamada_senha, "%Y-%m-%d %H:%M:%S.%f")
timestamp2 = datetime.strptime(data_retirada_senha, "%Y-%m-%d %H:%M:%S.%f")

# Subtraindo os timestamps
difference = timestamp1 - timestamp2

# Printando o resultado
print(f"Difference: {difference}")

# Printando o resultado em termos de dias, horas, minutos e segundos
days = difference.days
seconds = difference.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

print(f"Days: {days}, Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")
