# Quick Reference: Few-Shot + Agentic Enhancements

This document summarizes the new features integrated into your relevance evaluation pipeline.

---

## 1. Semantic Versioning

- **Auto-incremented versions**: Each iteration increases version number automatically.  
- **Suffix based on features**:
  - `-fewshot` → Few-shot examples only
  - `-agentic` → Few-shot + agentic conflict resolver  
- **Example progression**:
  - `v2-fewshot` → First run with few-shot  
  - `v3-agentic` → Next run adds agentic layer  
  - `v4-agentic` → Subsequent run with agentic active  

---

## 2. Few-Shot Pool

- **Source**: Cleaned log (`prompt_evaluation_log_cleaned.json`)  
- **Selection Criteria**:
  - Hybrid confidence ≥80%
  - Balanced 50/50 relevant vs irrelevant
  - Shuffled for diversity
- **Usage**: Prepended to evaluation prompt automatically each iteration

---

## 3. Agentic Conflict Resolver

- **Trigger Condition**: When model vs rule confidence differs by >20%.  
- **Process**:
  1. Reanalyzes reasoning JSON and criteria.
  2. Chooses final decision using weighted logic.
  3. Logs reconciled decision + rationale under `agentic_resolution`.
- **Review**: Flagged outputs stored in `flagged_for_review.json`.

---

## 4. Enhanced Logging Fields

Each relevant document log entry now includes:

- `decision_source`: Always `"hybrid"` (model + rule combo)  
- `hybrid_confidence`: Average of model and rule confidence  
- `agentic_resolution`: Reconciled decision + rationale (if flagged)  
- `prompt_version`: Semantic version of pipeline for that iteration  

---

## 5. Usage Notes

- **Log File**: All runs append to `prompt_evaluation_log.json`.  
- **Clean Log**: Run cleaner when schema changes; otherwise continue with cleaned log.  
- **Visualization**: Drift, confidence trends, and flagged discrepancies visualized at end of each run.  
