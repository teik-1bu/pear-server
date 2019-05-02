from flask import Blueprint, jsonify

rest_node = Blueprint('rest_node', __name__, url_prefix='/v1')


@rest_node.route('/node', methods=['GET'])
def get_list_node():
    return jsonify(
        size=31739904,
        etag="\"5989826e-4ac3b8d\"",
        total_nodes_num=1,
        latest_nodes_num=1,
        nodes=[
            {
                "host": "localhost",
                "http_port": 8081,
                "https_port": 8081,
                "type": "node",
                "capacity": 6
            }
        ],
        torrents={
            "512": "http://localhost:8081/pearplayerdemo.000webhostapp.com/Pear-Demo-test.torrent"
        }
    )
