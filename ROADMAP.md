# 🗺️ Cenegi Security Scripts – Roadmap

High-level plan for features and improvements to this repo.  
This is a living document and will change as the project evolves.

---

## ✅ Completed

- [x] Create initial repository and README
- [x] Add `pentest-automation.sh` Bash script
- [x] Add blue-themed colored output and basic UX messages
- [x] Support **normal** and **proxychains** modes
- [x] Add timestamped **results directory** per run (grouping all artifacts)
- [x] Implement basic tool checks for required binaries (`nmap`, `nc`)
- [x] Publish repo and link it from resume / GitHub profile
- [x]  Build initial **Python-based automation script** that mirrors the Bash workflow
- [x] Support `--proxy` style behavior (proxy / non-proxy modes)
- [x] Use the same results directory layout and filenames

---

## 🧪 In Progress / Next Up

- [ ] Improve error handling and input validation (e.g., bad targets, unreachable host)
- [ ] Add more graceful handling when optional tools (`nikto`, `sslscan`, `eyewitness`) are missing
- [ ] Light refactor of the Bash script into reusable functions (scan, web checks, summary generation)

---

## 🔮 Planned

- [ ] Add configuration options (profiles for light / full / stealth scans)
- [ ] Add log / evidence collection helpers for incident response (e.g., grabbing key logs, saving artifacts)
- [ ] Add simple report-helper scripts (collect outputs into a single folder, generate a basic markdown/text report starter)
- [ ] Add example usage scenarios (lab walkthroughs, sample commands)
- [ ] Add unit/integration tests for the Python version where practical
- [ ] Add CONTRIBUTING guidelines for future collaborators

---

## 📝 Notes

Goals for this repo:

- Stay **practical** and **readable** — scripts that a working security engineer would actually use.
- Demonstrate **automation skills** for:
  - Penetration testing labs  
  - Real-world authorized assessments  
  - Incident response and evidence gathering
- Keep the Bash and Python versions aligned so they feel like two interfaces to the same workflow.
