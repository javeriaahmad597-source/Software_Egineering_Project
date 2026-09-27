# VLSI Design Assistant

An agentic software system that uses LLM-assisted generation to produce Verilog RTL modules from natural-language hardware specifications, verified through deterministic simulation (Icarus Verilog / Verilator) before any output is accepted.

## Problem

Unlike most agentic AI applications, RTL design has a deterministic, non-LLM ground truth: a Verilog module either compiles and passes simulation, or it doesn't. This project uses that property to build a verification-first agent pipeline, where an LLM's generated output is always treated as a hypothesis to be tested — never as a final answer.

## Architecture — Six Agents

1. **Spec Intake Agent** — Converts a natural-language hardware requirement into a structured design spec (I/O ports, timing constraints, target FSM behavior).
2. **RTL Generation Agent** — Uses the Gemini API to generate a Verilog module from the structured spec.
3. **Testbench Agent** — Generates or selects a testbench for the module under test.
4. **Verifier Agent** — Runs Icarus Verilog / Verilator against the generated RTL and testbench, returning a structured pass/fail report.
5. **Repair Agent** — Takes the Verifier's structured failure report and produces a patched RTL version, looping back to the Verifier (bounded retries).
6. **Report & Commit Agent** — Produces a design rationale document for the verified module and prepares the final commit.
Spec Intake → RTL Generation → Testbench → Verifier ⇄ Repair (loop until pass) → Report & Commit

## Tech Stack

- Python
- Google GenAI SDK 2.0 (Gemini API, `gemini-3.8-flash` via the Interactions API)
- Icarus Verilog / Verilator (RTL simulation and verification)

## Project Structure
agents/
spec_intake/ rtl_gen/ testbench/ verifier/ repair/ report/
test_gemini_connection.py # Sprint 1: verifies the Gemini API connection
requirements.txt
.env # local only — holds GEMINI_API_KEY, never committed

## Setup

1. `pip install -r requirements.txt`
2. Create a `.env` file with `GEMINI_API_KEY=<your key>` (get one at https://aistudio.google.com/apikey)
3. Run `python test_gemini_connection.py` to verify the connection

## Status

**Sprint 1 (current):** repository scaffolding and a working Gemini API connection.
Later sprints implement each agent, the Verilog simulation loop, and the end-to-end pipeline.