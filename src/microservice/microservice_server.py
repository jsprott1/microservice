from flask import Flask, request, abort
import threading

class MicroserviceServer:
    def __init__(self, target, restrict_network_partner, allowed_network_partners, route="/", flask_listen_ip="0.0.0.0", server_port=5000):
        self.target = target
        self.flask_app = Flask(__name__)
        @self.flask_app.route(route, methods=['POST'])
        def flask_receive_data():
            addr = request.remote_addr
            if restrict_network_partner and not addr in allowed_network_partners:
                abort(403)
            r_json = request.json
            result = getattr(target, r_json["function"])(*r_json["args"],**r_json["kwargs"])
            return result
        self.flask_thread = threading.Thread(target=self.flask_app.run, 
                                            kwargs={"host":flask_listen_ip, "port":server_port})
        self.flask_thread.start()
        print("Microservice started")
    def join(self):
        self.flask_thread.join()
