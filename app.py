from flask import Flask, request, jsonify

app = Flask(__name__)
b = 0
seed = 0

@app.route('/api', methods=['GET'])
def get_coordinates():
    i = 0
    puntos = {'Coordenadas': []}
    lat = float(request.args.get('lat'))
    lon = float(request.args.get('lon'))
    while i < 4:
        latdelta = normal(0, 0.0001)
        londelta = normal(0, 0.0001)
        latitud = lat + latdelta
        longitud = lon + londelta
        puntos['Coordenadas'].append({'Lat': latitud, 'Lon': longitud})
        i+=1
    return jsonify(puntos)

def normal(mu, sigma):
    i = 1
    sumu = 0
    while i <= 12:
        u = generate_u()
        sumu = sumu + u
        i += 1
    valor = sigma * (sumu - 6) + mu
    return valor

def generate_u():
    global b
    global seed
    a = 19
    c = 155
    mod = 1000
    if b == 0:
        seed = 4
        b = 1
    seed = (a * seed + c) % mod
    u = seed / 1000
    return u

if __name__ == '__main__':
    app.run(debug=True)