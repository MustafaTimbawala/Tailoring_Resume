from typing import List, Dict, Any, Optional, TypedDict
from components import *
from langchain_core.documents import Document 
from langchain_core.tools import tool
from data.master.fomatting import formats, tasks 
from langgraph.graph import START, StateGraph
from components import vector_store_class,  google_llm, loader, text_splitter, generic_template, resume_template

vector_store = vector_store_class
llm  = google_llm
docs = loader.load()
all_splits = text_splitter.split_documents(docs)
document_ids = vector_store_class.add_documents(documents=all_splits) 



class State(TypedDict):
    question: str 
    job_description: str
    job_title: str
    company: str
    context:List[Document]
    answer: str

def retrieve(state: State):
    retrieved_docs = vector_store_class.similarity_search(state["job_description"], k=5)
    return {"context": retrieved_docs}

def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"]) 
    prompt = generic_template
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response} 

def gen_exp_sec(state: State): 
    docs_content = "\n\n".join(doc.page_content for doc in state["context"]) 
    task = tasks["experience_section"]
    formatting = formats["experience"] 
    word_limit =200; 
    tone = ""
    message = resume_template.invoke({"job_title": state["job_title"], "context": docs_content, "company": state["company"], "job_description": state["job_description"], "task": task, "formatting" : formatting, "word_limit": word_limit, "tone": tone }) 
    print(message)
    response = llm.invoke(message) 
    return {"answer" : response}
