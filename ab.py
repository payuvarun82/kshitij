# mock_post_server.py

import socket
import os

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # For Render, bind to 0.0.0.0 and use PORT from environment
    port = int(os.environ.get('PORT', 8443))
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print(f"POST mock server running on port {port}")

    while True:
        conn, addr = server.accept()
        request = conn.recv(4096).decode('utf-8', errors='ignore')

        if request.startswith("POST"):
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Transfer-Encoding: chunked\r\n"
                "Content-Type: application/json\r\n"
                "\r\n"
                "INVALID_HEX\r\n"
                '{"data": "test"}\r\n'
                "0\r\n\r\n"
            )
            conn.sendall(response.encode())

        conn.close()

if __name__ == '__main__':
    start()
