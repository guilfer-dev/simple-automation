from flask import Flask, render_template
import RPi.GPIO as GPIO

automacao = Flask(__name__)

#pinos conectados aos reles
quarto = 23
garagem = 24

#inicializar status dos comodos

statusquarto = 0
statusgaragem = 0

#configuracoes dos pinos
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(quarto, GPIO.OUT)
GPIO.setup(garagem, GPIO.OUT)

#pagina inicial
@automacao.route("/")
def principal():

    # ler status dos pinos e atribuir ao comando para facilitar o botao virtual
	statusquarto = GPIO.input(quarto)
        statusgaragem = GPIO.input(garagem)

    #dicionario para os dados dos pinos
	bv = {
		'title'   : 'GPIO output Status!',
		'quarto'  : statusquarto,
		'garagem' : statusgaragem,
	}
	return render_template('automacao.html', **bv)

@automacao.route("/<comodo>/<acao>")
def acao(comodo, acao):

    #atribuir string html do interruptor equivalente no interruptor do comodo correto para assim determinar o endereco
	if comodo == 'quarto':
		interruptor = quarto
	if comodo == 'garagem':
		interruptor = garagem

    #atribuir string html da posicao do interruptor equivalente ao comodo correto para assim determinar o endereco
	if acao == "ligado":
		GPIO.output(interruptor, GPIO.HIGH)
	if acao == "desligado":
		GPIO.output(interruptor, GPIO.LOW)
	statusquarto = GPIO.input(quarto)
	statusgaragem = GPIO.input(garagem)

	bv = {
              'quarto'  : statusquarto,
              'garagem' : statusgaragem,
	}
	return render_template('automacao.html', **bv)


if __name__ == "__main__":
	automacao.run()
