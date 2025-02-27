import uvicorn
import sys
import os

if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

    uvicorn.run(
        app="app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
