from langchain_ollama import OllamaLLM
from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.text import TextLoader 
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


# llm = OllamaLLM(model="gpt-oss:20b")

ollama_llm = OllamaLLM(model="mistral:latest") 

google_llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vector_store_class = InMemoryVectorStore(embeddings)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, chunk_overlap=20)

loader = TextLoader("./data/master/master_resume.txt")



cover_letter_template = PromptTemplate(
    template="""
            You are a professional cover letter writer. Create a tailored cover letter based on the information below.
            
            Applicant Information:
            {resume}
            
            Job Title: {job_title}
            Company: {company}
            
            Job Analysis:
            Required Skills: {required_skills}
            Key Responsibilities: {key_responsibilities}
            
            Instructions:
            1. Write a compelling introduction that mentions the job title and company
            2. Highlight 2-3 most relevant experiences that match the job requirements
            3. Explain how the applicant's skills align with the job needs
            4. Include a call to action in the conclusion
            5. Keep the letter professional and concise (3-4 paragraphs)
            
            Return the cover letter in plain text format.
            """,
    input_variables=[
        "personal_info",
        "job_title",
        "company",
        "required_skills",
        "key_responsibilities",
    ],
)


resume_template = PromptTemplate(
    input_variables=[
        "task",
        "job_title",
        "company",
        "job_description",
        "context",            
        "tone",               
        "word_limit", 
        "formatting"  
    ],
    template="""
You are an expert technical resume editor for software engineering, data, and technology internships.
Your job: perform the SPECIFIC TASK below to tailor the user's resume for the given job posting.

--- INSTRUCTIONS (follow carefully) ---
1) Task to perform (do exactly this): {task}
   - If `resume_section_id` is provided, edit **only that section** and leave other sections unchanged.
   - If no `resume_section_id` is provided, consider the whole resume.

2) Job context:
   Job Title: {job_title}
   Company: {company}
   Job Description:
   {job_description}

3) User materials:
   Retrieved context relevant information from the resume:
   {context}

4) Tone & length:
   - Tone: {tone} (if blank, default to "professional, concise, achievement-oriented")
   - Aim for roughly {word_limit} words or fewer when rewriting (if provided). Keep resume to ~1 page.

5) Safety & factuality:
   - DO NOT invent facts, dates, awards, or metrics.
   - If you need a metric, insert a placeholder like: <ADD_METRIC: e.g., "reduced latency by X%">.
   - Only rephrase/strengthen claims that are already present in the resume_text or context.

6) Output format (MUST follow EXACTLY):
Return Latex formated like: 
{formatting}


7) Additional guidance for bullets:
   - Prefer active verbs, quantify impact where possible, and put tech stack and outcomes near the start of bullets.
   - Convert passive or vague lines into achievement-oriented bullets (example: "Built X that did Y —> Built X, reduced Y by Z% by doing A").


--- END INSTRUCTIONS ---
"""
)


generic_template = PromptTemplate(
    input_variables=["question", "context"],
    template="""
You are an intelligent and reliable AI assistant. Your job is to carefully complete the following task:

**Task:**
{question}

**Context:**
{context}

Follow these instructions carefully:
- Be accurate, logical, and relevant to the task.
- Maintain a professional and consistent tone.
- If appropriate, provide concise examples or reasoning.
- Structure the answer clearly and make it easy to understand. 
- The ouput should be in overleaf latex making sure not to add any extra comments in the latex



Now generate your response below:
"""
)
