from flask import Flask
import random
app = Flask(__name__)
facts_list = [
    "El Sol es 400 veces más grande que la Luna, pero también está 400 veces más lejos de la Tierra, lo que hace que ambos parezcan tener el mismo tamaño en el cielo.",
    "Los pulpos tienen tres corazones y su sangre es de color azul debido a una proteína llamada hemocianina.",
    "Una sola cucharada de miel es el resultado del trabajo de aproximadamente 12 abejas durante toda su vida.",
    "El ADN de los humanos y los plátanos es aproximadamente un 60% similar.",
    "En el espacio, los astronautas no pueden llorar como en la Tierra, ya que las lágrimas no tienen gravedad para caer; se quedan flotando en sus ojos."
]
lanzar_moneda = ["Cara", "Cruz"]
@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"
    "<a href="/random_fact">¡Ver un dato aleatorio!</a>"
    "<a href="/moneda">Lanzar una Moneda</a>"

@app.route("/random_fact")
def random():
   return f'<p>{random.choice(facts_list)}</p>'

@app.route("/moneda"):
    return f"<p>{random.choice(lanzar_moneda)}</p>'"

if __name__ == '__main__':
 app.run()
