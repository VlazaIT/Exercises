# Implement a Flask backend service that tells whether a number received as a parameter is a prime number or not.
# Use the prior prime number exercise as a starting point.
# For example, a GET request for number 31 is given as: http://127.0.0.1:5000/prime_number/31.
# The response must be in the format of {"Number":31, "isPrime":true}.

from flask import Flask

app = Flask(__name__)
@app.route('/prime_number/<number>')
def prime_number(number):
    number = int(number)
    if number == 1:
        answer = "false"
    else:
        for i in range(2, number):
            if (number % i == 0):
                answer = "false"
                break
        else:
            answer = "true"

    response = {
        "Number": number,
        "iSPrime:": answer
        }
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)