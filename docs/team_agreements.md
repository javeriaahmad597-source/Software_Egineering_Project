# Team Agreements & Quality Gates (VeriLoop)

## Definition of Ready (DoR)
A user story is considered "Ready" for sprint backlog intake only when:
1. It is written in the standard User Story format (As a... I want to... So that...).
2. Story Points have been assigned using Fibonacci estimation.
3. At least 2 testable Acceptance Criteria (Given/When/Then format) are explicitly defined.
4. All external dependencies and blockers are cleared.
5. An individual team member is assigned ownership.

## Definition of Done (DoD)
A user story is considered "Done" only when:
1. Code is successfully merged into `main` via a reviewed Pull Request (PR) with at least 1 teammate approval.
2. Commit messages and PR titles explicitly reference the Jira Ticket ID (e.g., `SCRUM-25`).
3. Unit test coverage passes cleanly via `pytest`.
4. Acceptance Criteria have been formally verified and signed off by the Product Owner (Javeria).
5. Environment secrets (`.env`) are excluded from Git tracked files (with a `.env.example` provided).
6. Associated documentation and traceability records are updated.
7. Jira ticket status is transitioned to "Done".