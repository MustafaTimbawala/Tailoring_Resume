from fastapi import FastAPI, HTTPException, Body 
from fastapi.middleware.cors import CORSMiddleware
from components import google_llm, loader, text_splitter, vector_store_class
from functions import retrieve, gen_exp_sec, State
from langgraph.graph import START, StateGraph 
from contextlib import asynccontextmanager 
from pydantic import BaseModel, Field


class TailoringRequest(BaseModel):
    question: str = Field(..., description="Query for retrieving relevant context")
    job_title: str = Field(..., description="Job title for the position")
    company: str = Field(..., description="Company name")
    job_description: str = Field(..., description="Full job description")

@asynccontextmanager
async def lifespan(app: FastAPI): 
    global vector_store, resume_graph 

    llm = google_llm
    docs = loader.load()
    all_splits = text_splitter.split_documents(docs)
    vector_store = vector_store_class  # Use your initialized vector store
    vector_store.add_documents(documents=all_splits)   

    exp_graph_builder = StateGraph(State).add_sequence([retrieve, gen_exp_sec])
    exp_graph_builder.add_edge(START, "retrieve")
    resume_graph = exp_graph_builder.compile() 

    yield

    vector_store = None
    resume_graph = None


app = FastAPI(
    title="AI Resume Tailor API",
    description="API for resume tailoring and generation",
    version="0.0.1",
    lifespan =lifespan
    ) 
# Allow requests from your front-end (React app)
origins = [
    "http://localhost:5173",  # React development server
    "http://127.0.0.1:5173",  # Also allow access from this URL
    # Add other frontend URLs as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows only specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
async def root():
    return {
        "message": "LangGraph RAG API",
        "endpoints": {
            "/generate-experience": "POST - Generate resume experience section"
        }
    } 

@app.post("/generate-experience")
async def generate_experience(request: TailoringRequest):
    """
    Generate a resume experience section based on job details and retrieved context.
    """
    try: 
        # How about I construct the type dictionary state and then pass that typed dictionary to the function that I built 
        current_state = State( 
            question= request.question, 
            job_title= request.job_title, 
            company=request.company, 
            job_description= request.job_description, 
            context=[], 
            answer="",
        )
        result = resume_graph.invoke(current_state)
        return result["answer"].content
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating experience section: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
