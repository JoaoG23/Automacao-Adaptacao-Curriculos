from app import app
import os
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    port = os.getenv('PORT_SERVER')
    print(f"Automacao Adaptacao Curriculos - Starting server on port {port}")
    app.run( host='0.0.0.0', port=port or 5000, debug=True )