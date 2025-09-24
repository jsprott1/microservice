# Microservice

A library to call Python class methods remotely, using HTTP requests

### Requirements

flask

### Usage:

Start a server by calling

`server = MicroserviceServer(target, restrict_network_partner, allowed_network_partners, route, ip, port)`
where
`target` is an instance of the class the server calls methods from,
`restrict_network_partner` is a boolean. If true, only allow requests from allowed_network_partners through.
`allowed_network_partners` is a list of strings, representing IPv4 addresses. 
`route`, `ip`, `port` are strings making up the server URI. 
