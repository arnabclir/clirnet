# FlashCat API Keys Archive

**Generated:** 2025-11-13
**Purpose:** Archive of hardcoded API keys found in candidate submissions

---

## Summary

Total API keys found: **3** (with hardcoded credentials)
Total candidates with PROPER credential handling: **4** (using env vars)

### Hardcoded API Keys (CRITICAL SECURITY ISSUE)

| Candidate | Folder | API Key | File | Status |
|-----------|--------|---------|------|--------|
| Binita Ganguly | `Binita_Ganguly` | `ak_1KT9226nO3p75Dv3Vg2Ki4dj56L1W` | assignment.py | ❌ EXPOSED |
| Suvranil Sarkar | `Suvranil Sarkar - DSPy_Practical_Assignment` | `ak_1vd4a60HG1CO3pF17J7bk8YS1Wd3m` | DSPy_Assignment.ipynb | ❌ EXPOSED |
| Ashmita Chakrabarti | `DSPy_Assignment_Ashmita_Chakrabarti` | `ak_1cI2XZ9tq9OS2a12Tw01Y6a61y24E` | Assignment_DSPy.ipynb | ❌ EXPOSED |

### Candidates with Proper Credential Handling (Best Practices)

| Candidate | Folder | Approach | Status |
|-----------|--------|----------|--------|
| Aashish Gupta | `aashish_gupta_assignment` | `os.environ.get("LongCat_API_KEY")` | ✅ SAFE |
| Sayan Malik | `sayan malik` | `os.getenv("APIKEY")` | ✅ SAFE |
| Abhisek Paul | `Abhisek_paul_DSPy_Assignment` | `getpass('API_KEY (press Enter to skip): ')` | ✅ SAFE |
| Sujit | `Sujit` | Placeholder: `LLM_API_KEY_PLACEHOLDER` | ✅ SAFE |

---

## Detailed Findings

### 1. Binita Ganguly

- **Folder Path:** `D:\writing\clirnet\junior_python_hiring\Binita_Ganguly`
- **File:** `assignment.py`
- **Line:** 28
- **API Key:** `ak_1KT9226nO3p75Dv3Vg2Ki4dj56L1W`
- **Context:** Hardcoded directly in Python file for DSPy LM configuration
- **Security Issue:** CRITICAL - Active API key exposed in source code

### 2. Suvranil Sarkar

- **Folder Path:** `D:\writing\clirnet\junior_python_hiring\Suvranil Sarkar - DSPy_Practical_Assignment\Suvranil Sarkar - DSPy_Practical_Assignment`
- **File:** `DSPy_Assignment.ipynb`
- **Cell:** 2, Line 79
- **API Key:** `ak_1vd4a60HG1CO3pF17J7bk8YS1Wd3m`
- **Context:** Hardcoded in Jupyter notebook cell for LongCat-Flash-Chat configuration
- **Security Issue:** CRITICAL - Active API key exposed in notebook

### 3. Ashmita Chakrabarti

- **Folder Path:** `D:\writing\clirnet\junior_python_hiring\DSPy_Assignment_Ashmita_Chakrabarti`
- **File:** `Assignment_DSPy.ipynb`
- **Cell:** 5, Line 206
- **API Key:** `ak_1cI2XZ9tq9OS2a12Tw01Y6a61y24E`
- **Context:** Hardcoded in notebook with comment showing it was intended for .env file usage, but actual key exposed in code
- **Security Issue:** CRITICAL - Active API key exposed in notebook

---

## Security Assessment

### Risk Level: **HIGH**

All three submissions contain hardcoded API keys that were exposed in their submission files:

- **Exposure Method:** Direct hardcoding in source code/notebooks
- **Token Format:** `ak_[alphanumeric]` (LongCat API token format)
- **Key Characteristics:** All appear to be valid, active tokens
- **Version Control Risk:** Keys likely committed to version control

### Violations Identified

1. **Hardcoding Secrets** - Violates production readiness standards
2. **No Environment Variable Usage** - Should use `.env` files or env vars
3. **Credentials in Submission** - Exposed to evaluators and potentially publicly
4. **No `.gitignore` Protection** - No evidence of attempts to prevent exposure

---

## Actions Required

### Immediate
- [ ] **Revoke/Rotate** all three API keys in LongCat account
- [ ] Monitor accounts for unauthorized usage
- [ ] Notify affected candidates of the security issue

### For Evaluations
- [ ] Flag as critical security failure in evaluation rubric (deduction of points for Production Readiness)
- [ ] Document in candidate_tracking.md under "Critical Issues"
- [ ] Use as teaching moment in feedback

### Process Improvement
- [ ] Add pre-submission validation to check for common API key patterns
- [ ] Provide candidates with security best practices documentation
- [ ] Require `.env` file example with dummy keys instead of real ones
- [ ] Update submission guidelines with security checklist

---

## Notes

- All keys appear to be valid LongCat API tokens based on format
- Keys were likely obtained from LongCat signup/onboarding process
- This is a common mistake for junior developers unfamiliar with secrets management
- Provides good opportunity for security education during onboarding
