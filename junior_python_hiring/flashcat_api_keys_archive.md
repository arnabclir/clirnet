# FlashCat API Keys Archive

**Generated:** 2025-11-13
**Last Updated:** 2025-12-11
**Purpose:** Archive of hardcoded API keys found in candidate submissions

---

## Summary

Total unique API keys found: **8** (with hardcoded credentials)
Total candidates with exposed keys: **9** (Adarsh Anand & Arpan Dey share same key)
Total candidates with PROPER credential handling: **4** (using env vars)

### Hardcoded API Keys (CRITICAL SECURITY ISSUE)

| Candidate | Folder | API Key | File | Status |
|-----------|--------|---------|------|--------|
| Binita Ganguly | `Binita_Ganguly` | `ak_1KT9226nO3p75Dv3Vg2Ki4dj56L1W` | assignment.py | ❌ EXPOSED |
| Suvranil Sarkar | `Suvranil Sarkar - DSPy_Practical_Assignment` | `ak_1vd4a60HG1CO3pF17J7bk8YS1Wd3m` | DSPy_Assignment.ipynb | ❌ EXPOSED |
| Ashmita Chakrabarti | `DSPy_Assignment_Ashmita_Chakrabarti` | `ak_1cI2XZ9tq9OS2a12Tw01Y6a61y24E` | Assignment_DSPy.ipynb | ❌ EXPOSED |
| Krishna Soni | `Krishna Soni` | `ak_1Vo1sl9GT0sV3YM1df2AY9MU7KZ0u` | DSPy_Assignment_Krishna.ipynb | ❌ EXPOSED |
| Abhirup Dey | `Abhirup Dey` | `ak_1jN8Ei49i9Po5OR7Qs0Ta51Y3ls4s` | Assignment_DSPy_Practical_AbhirupDey.ipynb | ❌ EXPOSED |
| Adarsh Anand | `Adarsh Anand` | `ak_1Nm8PI6Zb0aR97X1wc9Zs32K8DZ06` | final_assignment.ipynb | ❌ EXPOSED |
| Arpan Dey | `Arpan Dey` | `ak_1Nm8PI6Zb0aR97X1wc9Zs32K8DZ06` | final_assignment.ipynb | ❌ EXPOSED |
| Sachin Kumar | `Sachin Kumar` | `ak_1Ru8DC84i9Fu4vm7Ip2os6gL7fw3H` | Sachin_Project.ipynb | ❌ EXPOSED |
| Suhana Parvin | `Suhana_Parvin` | `ak_15Y8kS6dp2Iy8Lt0Tl2Ip5Oz3ap6a` | structuring_unstructured_data_Suhana_Parvin.ipynb | ❌ EXPOSED |

### Candidates with Proper Credential Handling (Best Practices)

| Candidate | Folder | Approach | Status |
|-----------|--------|----------|--------|
| Aashish Gupta | `aashish_gupta_assignment` | `os.environ.get("LongCat_API_KEY")` | ✅ SAFE |
| Sayan Malik | `sayan malik` | `os.getenv("APIKEY")` | ✅ SAFE |
| Abhisek Paul | `Abhisek_paul_DSPy_Assignment` | `getpass('API_KEY (press Enter to skip): ')` | ✅ SAFE |
| Sujit | `Sujit` | Placeholder: `LLM_API_KEY_PLACEHOLDER` | ✅ SAFE |

---

## Detailed Findings

### November 2025 Batch

#### 1. Binita Ganguly

- **Folder Path:** `D:\writing\clirnet\junior_python_hiring\Already Evaluated\Binita_Ganguly`
- **File:** `assignment.py`
- **Line:** 28
- **API Key:** `ak_1KT9226nO3p75Dv3Vg2Ki4dj56L1W`
- **Context:** Hardcoded directly in Python file for DSPy LM configuration
- **Security Issue:** CRITICAL - Active API key exposed in source code

#### 2. Suvranil Sarkar

- **Folder Path:** `D:\writing\clirnet\junior_python_hiring\Already Evaluated\Suvranil Sarkar - DSPy_Practical_Assignment`
- **File:** `DSPy_Assignment.ipynb`
- **Cell:** 2, Line 79
- **API Key:** `ak_1vd4a60HG1CO3pF17J7bk8YS1Wd3m`
- **Context:** Hardcoded in Jupyter notebook cell for LongCat-Flash-Chat configuration
- **Security Issue:** CRITICAL - Active API key exposed in notebook

#### 3. Ashmita Chakrabarti

- **Folder Path:** `D:\writing\clirnet\junior_python_hiring\Already Evaluated\DSPy_Assignment_Ashmita_Chakrabarti`
- **File:** `Assignment_DSPy.ipynb`
- **Cell:** 5, Line 206
- **API Key:** `ak_1cI2XZ9tq9OS2a12Tw01Y6a61y24E`
- **Context:** Hardcoded in notebook with comment showing it was intended for .env file usage, but actual key exposed in code
- **Security Issue:** CRITICAL - Active API key exposed in notebook

#### 4. Krishna Soni (Previously Missed)

- **Folder Path:** `D:\writing\clirnet\junior_python_hiring\Already Evaluated\Krishna Soni`
- **File:** `DSPy_Assignment_Krishna.ipynb`
- **Cell:** 3, Line 142
- **API Key:** `ak_1Vo1sl9GT0sV3YM1df2AY9MU7KZ0u`
- **Context:** Hardcoded directly in notebook for LONGCAT_API_KEY variable
- **Security Issue:** CRITICAL - Active API key exposed in notebook

---

### December 2025 Batch

#### 5. Abhirup Dey

- **Folder Path:** `D:\writing\clirnet\junior_python_hiring\Abhirup Dey`
- **File:** `Assignment_DSPy_Practical_AbhirupDey.ipynb`
- **Cell:** Line 168
- **API Key:** `ak_1jN8Ei49i9Po5OR7Qs0Ta51Y3ls4s`
- **Context:** Hardcoded as LONGCAT_API_KEY variable in Jupyter notebook
- **Security Issue:** CRITICAL - Active API key exposed in notebook
- **Note:** Otherwise a strong submission (67/100, only passing candidate in December batch)

#### 6. Adarsh Anand ⚠️ SHARED KEY

- **Folder Path:** `D:\writing\clirnet\junior_python_hiring\Adarsh Anand`
- **File:** `final_assignment.ipynb`
- **Cell:** Line 53
- **API Key:** `ak_1Nm8PI6Zb0aR97X1wc9Zs32K8DZ06`
- **Context:** Hardcoded as API_KEY variable
- **Security Issue:** CRITICAL - Active API key exposed; **SAME KEY AS ARPAN DEY** (indicates possible collaboration or shared account)

#### 7. Arpan Dey ⚠️ SHARED KEY

- **Folder Path:** `D:\writing\clirnet\junior_python_hiring\Arpan Dey`
- **File:** `final_assignment.ipynb`
- **Cell:** Line 53
- **API Key:** `ak_1Nm8PI6Zb0aR97X1wc9Zs32K8DZ06`
- **Context:** Hardcoded as API_KEY variable
- **Security Issue:** CRITICAL - Active API key exposed; **SAME KEY AS ADARSH ANAND** (indicates possible collaboration or shared account)
- **Investigation Note:** Both candidates have identical file names (`final_assignment.ipynb`) and same API key - possible code sharing detected

#### 8. Sachin Kumar

- **Folder Path:** `D:\writing\clirnet\junior_python_hiring\Sachin Kumar\Assesment`
- **File:** `Sachin_Project.ipynb`
- **Cell:** Line 435
- **API Key:** `ak_1Ru8DC84i9Fu4vm7Ip2os6gL7fw3H`
- **Context:** Hardcoded in notebook with inline comment `# <--- YOUR KEY IS HERE`
- **Security Issue:** CRITICAL - Active API key exposed with explicit marker comment

#### 9. Suhana Parvin

- **Folder Path:** `D:\writing\clirnet\junior_python_hiring\Suhana_Parvin`
- **File:** `structuring_unstructured_data_Suhana_Parvin.ipynb`
- **Cell:** Line 171
- **API Key:** `ak_15Y8kS6dp2Iy8Lt0Tl2Ip5Oz3ap6a`
- **Context:** Hardcoded with comment indicating it should be replaced
- **Security Issue:** CRITICAL - Active API key exposed in notebook

---

## Security Assessment

### Risk Level: **HIGH**

All 9 submissions contain hardcoded API keys that were exposed in their submission files:

- **Exposure Method:** Direct hardcoding in source code/notebooks
- **Token Format:** `ak_[alphanumeric]` (LongCat API token format)
- **Key Characteristics:** All appear to be valid, active tokens
- **Version Control Risk:** Keys likely committed to version control

### Key Sharing Detection

⚠️ **IMPORTANT:** Adarsh Anand and Arpan Dey submitted with identical API keys (`ak_1Nm8PI6Zb0aR97X1wc9Zs32K8DZ06`). This could indicate:
1. Collaboration on the assignment (against rules if not permitted)
2. Shared LongCat account
3. Code copying from one candidate to another

**Recommendation:** Flag for manual review and potential plagiarism investigation.

### Violations Identified

1. **Hardcoding Secrets** - Violates production readiness standards
2. **No Environment Variable Usage** - Should use `.env` files or env vars
3. **Credentials in Submission** - Exposed to evaluators and potentially publicly
4. **No `.gitignore` Protection** - No evidence of attempts to prevent exposure
5. **Potential Collaboration** - Two candidates sharing same API key (new finding)

---

## Actions Required

### Immediate
- [ ] **Revoke/Rotate** all 8 unique API keys in LongCat account
- [ ] Monitor accounts for unauthorized usage
- [ ] Notify affected candidates of the security issue
- [ ] Investigate Adarsh Anand & Arpan Dey key sharing

### For Evaluations
- [x] Flag as critical security failure in evaluation rubric (deduction of points for Production Readiness)
- [x] Document in candidate_tracking.md under "Critical Issues"
- [ ] Use as teaching moment in feedback

### Process Improvement
- [ ] Add pre-submission validation to check for common API key patterns
- [ ] Provide candidates with security best practices documentation
- [ ] Require `.env` file example with dummy keys instead of real ones
- [ ] Update submission guidelines with security checklist
- [ ] Add explicit prohibition on code/credential sharing in assignment instructions

---

## Statistics

| Metric | November Batch | December Batch | Total |
|--------|:--------------:|:--------------:|:-----:|
| Exposed Keys | 4 | 5 | 9 candidates |
| Unique Keys | 4 | 4 | 8 unique |
| Safe Handling | 4 | 0 | 4 candidates |
| Key Sharing | 0 | 2 candidates | 2 candidates |

### Exposure Rate by Batch

- **November 2025:** 50% (4/8 with code submissions had exposed keys)
- **December 2025:** 100% of candidates who used API had exposed keys (5/5)
- **Overall:** 69% exposure rate among candidates who attempted LLM integration

---

## Notes

- All keys appear to be valid LongCat API tokens based on format
- Keys were likely obtained from LongCat signup/onboarding process
- This is a common mistake for junior developers unfamiliar with secrets management
- Provides good opportunity for security education during onboarding
- December batch showed higher exposure rate (100%) suggesting clearer guidance needed in assignment instructions
- Key sharing between Adarsh Anand and Arpan Dey warrants plagiarism review
