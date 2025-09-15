from app import app
import os
from dotenv import load_dotenv
load_dotenv()
port = os.getenv('PORT_SERVER')

if __name__ == "__main__":
    print(f"Automacao Adaptacao Curriculos - Starting server on port {port}")
    app.run(debug=True, host='0.0.0.0', port=port or 5000)