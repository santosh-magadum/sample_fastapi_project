from fastapi import FastAPI, Depends


app = FastAPI()

@app.get("/test")
async def testing_app():
    return "Successfully tested the app in the api folder"

@app.post("/sample_test/{num}")
def sample_test(num: int):
    return f"Successfully tested the sample test, num: {num}"

