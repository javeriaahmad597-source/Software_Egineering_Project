# Sprint 1 Impediment Log (Blockers Tracker)

| # | Date | Blocker / Issue | Owner | Status | How We Solved It |

| 1 | 19 Oct | `iverilog` command not recognized in Windows terminal | Areesha | Resolved | Added `C:\iverilog\bin` to Windows Environment PATH. Tested in cmd and verified it compiles. |
| 2 | 19 Oct | Windows cmd gave syntax error on `mkdir -p` | Laraib | Resolved | Removed `-p` flag since Windows creates directories using standard `mkdir docs\sprint1`. |
| 3 | 20 Oct | Pytest import error: `No module named 'agents.verifier.harness'` | Laraib | Resolved | Fixed typo in filename (`harness,py` had a comma instead of a dot). Ran via `python -m pytest`. |
| 4 | 20 Oct | Pytest skipped 3 compiler tests | Laraib | Resolved | Detected missing local `iverilog` on test machine; installed Icarus binary so all 5 tests pass. |