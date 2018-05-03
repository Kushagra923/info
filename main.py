from flask import Flask, jsonify, request

from modules import m_dns, m_port, m_admin_finder, m_site
from util import u_domain

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/dns', methods=['POST'])
def dns_query():
    data = {}
    try:
        domain = u_domain.domain_resolve(request.form['domain'])
    
        data = m_dns.dns_records(domain)
    except:
        data = {}

    return jsonify(data)

@app.route('/port', methods=['POST'])
def port_query():
    domain = u_domain.domain_resolve(request.form['domain'])
    port = request.form["port"]

    data = m_port.check_port(domain, port)

    return jsonify(data)
    
@app.route('/find_admin', methods=['POST'])
def admin_query():
    domain = u_domain.domain_resolve(request.form['domain'])

    data = m_admin_finder.find_admin(domain)

    return jsonify(data)

@app.route('/site_info', methods=['POST'])
def site_info():
    domain = u_domain.domain_resolve(request.form['domain'])

    data = m_site.info(domain)

    return jsonify(data)

if __name__ == '__main__':
    app.run()