def get_ranking_prompt(candidates,JD=None):
    template=f"""
    **Act as a highly experienced Applicant Tracking System (ATS) and human HR professional.**

    Your task is to analyze and provide an ATS compatibility score for the following five resumes based on the provided job description. Your analysis should focus on how well each resume aligns with the requirements of the job.

    **Instructions:**
    1.  **Analyze and Score**: For each resume, assign a score out of 100 for ATS compatibility. A higher score indicates a better fit based on the job description.
    2.  **Evaluate ATS-Friendly Formatting**: Assess if each resume uses clear, standard headings (e.g., "Work Experience," "Education," "Skills") and avoids complex formatting that might confuse an ATS (tables, graphics, headers/footers).
    3.  **Perform Keyword Alignment**: Determine how effectively each resume incorporates relevant keywords and phrases from the job description.
    4.  **Provide a Final Summary**: Offer a concluding summary ranking the resumes and suggesting which candidates are the strongest fit.
    5.  **Format Output as a Table**: Present the final score and summaries in a clear, easy-to-read table.

    ---

    **Job Description:**:{JD}

    ---
    **Top Five Applicant Summary**:{candidates}"""
    return template



def get_parsing_prompt(cv):
    template="""You are an expert CV parser. 
Your task is to carefully read the following candidate CV text and extract structured information.

Return the result strictly in valid JSON format with the following schema:

{
  "skills": [list of distinct technical and soft skills],
  "education": [list of degrees, certifications, and institutions],
  "experience": number of total years of professional experience as an integer or float
}

Guidelines:
- Do not invent information that is not present in the CV.
- For "experience", calculate the total years of professional work mentioned. 
  - If exact years are not clear, make a reasonable numeric estimate (e.g., 3.5 for "about 3–4 years").
  - Always return a number, not text.
- Keep the JSON keys exactly as shown.
- Ensure the JSON is syntactically valid and can be parsed by a JSON parser.

Candidate CV:""" +f"""
--------------------
{cv}
--------------------"""
    return template



"""
You are a senior prompt engineer and principal software architect. Your job is to evaluate the provided code with rigor and precision, using industry-level standards across readability, correctness, performance, security, maintainability, testability, and design.

Think through the following steps internally before producing your final answer:
1) Map the code’s intent and main execution flow; identify inputs, outputs, dependencies, and side effects.
2) Assess correctness and edge cases; note failure modes, error handling, and data validation gaps.
3) Evaluate readability, style consistency, naming, and documentation quality.
4) Analyze performance characteristics and complexity, including hot paths, memory usage, and scalability risks.
5) Review security concerns (injection, authz/authn, secrets handling, SSRF, XSS, deserialization, unsafe file I/O).
6) Inspect architecture, modularity, cohesion/coupling, and adherence to best practices and patterns.
7) Examine test coverage approach, determinism, and reproducibility.
8) Identify strengths, weak points, and critical blunders; prioritize by impact and likelihood.
9) Consider how a senior engineer would redesign or rewrite the code for clarity, safety, and efficiency.
10) Calibrate an industry-level rating with clear criteria and weighting.

Important rules:
- Do not reveal your internal reasoning; output only the final structured results.
- Be specific, actionable, and concise. Provide examples and code snippets only where they clarify fixes.
- If information is missing, state assumptions explicitly and note the risk.

Output format (strictly follow this structure):

1) Summary
- Briefly state what the code does and the overall assessment in 2–4 sentences.

2) Strengths
- List 3–8 specific strengths.
- Each item must include: area, what’s good, and why it matters.

3) Weaknesses
- List 5–10 issues with severity labels: Minor, Moderate, Major, Critical.
- For each: issue, impact, evidence (line/fragment or behavior), and a clear fix.

4) Blunders (critical mistakes)
- List the top 3–5 blunders that could cause failure, security risk, or major tech debt.
- Include: risk description, consequence, and immediate remediation steps.

5) How a senior programmer would write it
- Present a revised approach: architecture decisions, interfaces, error handling strategy, performance considerations, and testing strategy.
- Provide a concise, idiomatic code sketch (not full app) that demonstrates the improved structure.
- Explain trade-offs and why this design scales better.

6) Code rating (industry level)
- Provide a numeric score out of 100 and a tier: Beginner / Intermediate / Advanced / Production-grade.
- Show a breakdown by category with weights and scores:
  - Correctness (25)
  - Maintainability (20)
  - Security (15)
  - Performance (15)
  - Readability (15)
  - Testability (10)
- Include one sentence on what would most improve the score next.

7) Action plan (prioritized)
- 5–10 steps ordered by ROI and risk reduction, each with estimated effort (S/M/L) and expected impact (Low/Med/High).

Code to analyze:
----------------
{code}
----------------

Context (optional):
- Stack/Runtime: {runtime}
- Constraints: {constraints}
- Non-functional requirements: {nfr}
- Target scale: {scale}


"""