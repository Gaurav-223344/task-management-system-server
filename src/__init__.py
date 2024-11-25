import uvicorn

def start_server():
    uvicorn.run("src.fastapi_interface.main:app", host="127.0.0.1", port=8000, reload=True)
    
    
# if __name__ == '__main__':
#     start_server()