# Requirements & AI Constraints (VeriLoop - Sprint 1)

## 1. Functional Requirements (FR)
* **FR-01 (Natural Language Intake):** The system shall accept a plain-English natural-language hardware specification string via a CLI command.
* **FR-02 (RTL Generation):** The system shall call the Gemini API using a versioned system prompt to generate synthesizable Verilog RTL code.
* **FR-03 (File Persistence):** The system shall extract the code block from the LLM output and save it as a `.v` file inside the `output/` directory.
* **FR-04 (Verification Compilation):** The system shall invoke `iverilog` and execute `vvp` simulations via a subprocess harness to compile and test the generated module.
* **FR-05 (Status Reporting):** The system shall report a clear PASS/FAIL summary result to the terminal.

## 2. Non-Functional Requirements (NFR)
* **NFR-01 (Execution Safety):** The verification harness shall enforce a strict timeout limit to prevent infinite loops from hanging system execution.
* **NFR-02 (Error Handling):** Missing API keys or runtime failures shall display clean error messages without throwing unhandled stack traces.
* **NFR-03 (Traceability):** Every run shall log the model name, prompt version, and associated metadata.

## 3. AI Constraints & Guardrails
* **Constraint-01 (Deterministic Output):** The LLM temperature shall be kept low to maximize code syntax reproducibility.
* **Constraint-02 (Verilog Standard):** Generated code must strictly adhere to synthesizable Verilog-2001 standards (e.g., non-blocking assignments for sequential logic, active-low synchronous reset).
* **Constraint-03 (Retry Limit):** Future repair loops shall restrict automated correction attempts to a maximum of 3 retries.
* **Constraint-04 (External Fallback):** Unit tests must mock the LLM client to ensure testing can proceed without active API quotas or external network calls.