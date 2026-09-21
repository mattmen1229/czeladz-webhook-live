from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running!", 200

@app.route('/zapisz', methods=['GET', 'POST'])
def zapisz():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    if lat and lon:
        czas = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        wpis = f"[{czas}] Lat: {lat}, Lon: {lon} | Maps: https://maps.google.com/?q={lat},{lon}\n"
        print(f"ZLAPANO WSPOLRZEDNE: {wpis}")
        with open('wspolrzedne.txt', 'a', encoding='utf-8') as f:
            f.write(wpis)
        return jsonify({"status": "success", "lat": lat, "lon": lon}), 200
    return jsonify({"status": "error", "message": "Brak wspolrzednych"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
