from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Allow all origins for simplicity, but you should limit this in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class TextRequest(BaseModel):
    text: str

# Load model and tokenizer once at startup
tokenizer = AutoTokenizer.from_pretrained("google/pegasus-cnn_dailymail")
model = AutoModelForSeq2SeqLM.from_pretrained("google/pegasus-cnn_dailymail")
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

@app.post("/summarize")
async def summarize(request: TextRequest):
    text = request.text
    gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}
    summary = summarizer(text, **gen_kwargs)[0]["summary_text"]
    print(summary)
    return {"summary": summary}

@app.get("/myitem")
def getitem():
    return {"hello world"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
