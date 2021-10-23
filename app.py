from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

relay_one = 23
relay_two = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(relay_one, GPIO.OUT)
GPIO.setup(relay_two, GPIO.OUT)


@app.route("/")
def principal():

    bv = {
        'relay_one': GPIO.input(relay_one),
        'relay_two': GPIO.input(relay_two),
    }

    return render_template('index.html', **bv)


@app.route("/<relay>/<relay_status>")
def action(relay, relay_status):

    if relay == 'relay_one':
        relay_id = relay_one
    else:
        relay_id = relay_two

    if relay_status == 'False':
        GPIO.output(relay_id, GPIO.HIGH)
    else:
        GPIO.output(relay_id, GPIO.LOW)

    bv = {
        'relay_one': GPIO.input(relay_one),
        'relay_two': GPIO.input(relay_two),
    }

    return render_template('index.html', **bv)


if __name__ == "__main__":
    app.run()
