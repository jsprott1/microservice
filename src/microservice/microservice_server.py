from flask import Flask, request, abort
import threading

class MicroserviceServer:
    def __init__(self, target, config):
        self.target = target
        self.config = config
        filter_ip = config["restrict_network_partner"]
        self.flask_app = Flask(__name__)
        @self.flask_app.route(config["route"], methods=['POST'])
        def flask_receive_data():
            addr = request.remote_addr
            if filter_ip and not addr in config["allowed_network_partners"]:
                abort(403)
            r_json = request.json
            result = getattr(target, r_json["function"])(*r_json["args"],**r_json["kwargs"])
            return result
        self.flask_thread = threading.Thread(target=self.flask_app.run, 
                                            kwargs={"host":self.config["flask_listen_ip"], "port":self.config["server_port"]})
        self.flask_thread.start()
        print("Microservice started")
    def join(self):
        self.flask_thread.join()
