"""This module contains the LaTeX formatting templates for different sections of the resume.
These templates are used to generate the formatted resume output."""

formats = {
    "project": r"""  
            \resumeProjectHeading
        {\textbf{\href{https://github.com/MealadE/SharesSpace}{SharesSpace}} $|$ \emph{Python, Flask, Mongoose, PostgreSQL, GitHub}}{}
        \resumeItemListStart
            \resumeItem{Developed a database-backed social network application using \textbf{Python Flask} for the Web Server, with \textbf{HTML} and \textbf{CSS} for the front-end.} 
            \resumeItem{Utilized \textbf{PostgreSQL} for robust database management, handling complex queries and calculations for portfolio statistics, including Beta, covariance, and correlation matrices.} 
            \resumeItem{ Deployed the application on \textbf{Google Cloud virtual machines}, ensuring scalability and high availability.} 
            \resumeItem{Integrated social networking features, allowing users to manage friends, share stock lists, and write reviews, enhancing user interaction and collaboration}
        
        \resumeItemListEnd 
    """,
    "experience": r"""  
        \resumeSubheading
            {{Web Developer}}{Toronto, Canada}
        {African Student Association}{Oct. 2024 --  Jan. 2025}
        \resumeItemListStart
        \resumeItem{Collaborated with a cross-functional team using \textbf{Figma} to design and develop front-end UI/UX components for a website using a user-centered design approach, focusing on creating a visually appealing and functional interface. }

        \resumeItem{Built the back end using \textbf{Express}, \textbf{MongoDB}, and integrated \textbf{AWS S3} buckets for an efficient and scalable storage solution. 
        \resumeItem{Developed the front end using \textbf{React} and \textbf{Tailwind}, ensuring a modern but highly adapted user interface that successfully integrated African cultural design elements with contemporary interface design standards.}
        }
            \resumeItemListEnd  
    """,
    "skills": r""" 
    \section{Skills Summary}
    \begin{itemize}[leftmargin=0.15in, label={}]
        \small{\item{
        \textbf{Languages}{: Python, JavaScript, TypeScript, Dart, HTML/CSS, C, C++, Java, Kotlin, Assembly, Bash, SQL} \\
        \textbf{Frameworks and Libraries}{: ReactJS, NodeJs, Flutter, Express, FastAPI, Flask, Django, Bootstrap, React Native/Expo, Mongoose, JUnit, PyTorch, SciKit-Learn} \\
        \textbf{Databases}{: SQLlite, Firebase, MongoDB, AWS, Neo4js, PostgreSQL} \\
        \textbf{Tools}{: GIT, PyCharm, Jupyter, Android Studio, Eclipse, Figma, Agile, GitHub, Google Cloud Platform, Postman, Wireshark, Jira, Docker}
        }}
    \end{itemize}
    """,
} 

tasks = {
    "experience_section": """
Create a complete LaTeX-formatted 'Experience' section based on the user's provided context 
and the given job description. Focus on aligning the user's previous experiences with the 
skills and responsibilities mentioned in the job posting. Use bullet points that emphasize 
impact, technologies used, and measurable outcomes. Follow the example formatting closely
""",

    "projects_section": """
Generate a LaTeX-formatted 'Projects' section using the provided context and job description. 
Include 2–3 relevant projects that demonstrate technical proficiency, creativity, and problem-solving. 
Each project entry should include the project name, tech stack, and 2–3 achievement-focused bullet points 
following the formatting example closely
""",

    "skills_summary_section": """
Write a LaTeX-formatted 'Skills Summary' section based on the user's context and the job description. 
Group skills into logical categories such as 'Programming Languages', 'Frameworks & Tools', and 'Other Tools'. 
Highlight the most relevant technologies for the internship role. Follow the formatting example closely
"""
}
