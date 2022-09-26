import fastapi
import uvicorn

print("Hello fastapi")
api = fastapi.FastAPI()


# use Alt-Enter for context help
# api = FastAPI()
@api.get("/api/endpoint")
def endpoint():
    return {"msg": "Hello from FastAPI",
            "another msg": ["Hello", "World"]}


uvicorn.run(api, port=8001)
