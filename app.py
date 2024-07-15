import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from textsummarizer.pipeline.prediction import PredictionPipeline

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) Middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Templates directory for HTML rendering
templates = Jinja2Templates(directory="templates")

# Route to render index.html on the root path
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route to handle POST requests for text summarization
@app.post("/predict")
async def predict_route(request: Request):
    try:
        data = await request.json()
        text = data['text']
        obj = PredictionPipeline()
        summarized_text = obj.predict(text)
        return summarized_text
    except Exception as e:
        return {"error": str(e)}

# Run the FastAPI application using Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
