import http.server
import socketserver
import threading
import time
import logging

PORT = 8000
semaphore = threading.Semaphore(1)

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        logger.info(f"{self.client_address} intenta conectarse")
        semaphore.acquire()
        try:
            logger.info("El semáforo ha sido adquirido")
            # Simular tiempo de procesamiento
            time.sleep(2)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, World!")
            logger.info(f"{self.client_address} se ha conectado satisfactoriamente")
        finally:
            logger.info("El semáforo ha sido liberado")
            semaphore.release()

logger.info("Iniciando servidor...")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    logger.info("Servidor iniciado en el puerto %d", PORT)
    httpd.serve_forever()

