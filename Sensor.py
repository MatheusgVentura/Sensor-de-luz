import RPi.GPIO as GPIO
import time

# Definição dos pinos
LDR_PIN = 16
LED_YELLOW = 6
LED_RED = 5

# Configuração dos pinos
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_YELLOW, GPIO.OUT)
GPIO.setup(LED_RED, GPIO.OUT)

# Função para ler valor do LDR
def read_ldr(pin):
    count = 0
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)
    time.sleep(0.1)
    GPIO.setup(pin, GPIO.IN)

    while GPIO.input(pin) == 0:
        count += 1
        time.sleep(0.001)
        if count > 10000:  # Limite de segurança para não travar
            break
    return count

# Loop principal
try:
    while True:
        ldr_value = read_ldr(LDR_PIN)
        threshold = 1000

        if ldr_value > threshold:
            GPIO.output(LED_YELLOW, True)
            GPIO.output(LED_RED, False)
        else:
            GPIO.output(LED_YELLOW, False)
            GPIO.output(LED_RED, True)

        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
