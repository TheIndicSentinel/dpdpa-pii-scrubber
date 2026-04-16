# 🧼 dpdpa-pii-scrubber

**A lightweight, zero-dependency Python utility to detect and redact India-native PII patterns, aligned with the DPDP Act 2023.**

[![License](https://img.shields.io/badge/License-Apache_2.0-7C3AED?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-06B6D4?style=flat-square)](https://www.python.org/)
[![Focus](https://img.shields.io/badge/Focus-Bharat_Digital_Laws-F59E0B?style=flat-square)](#)

## 🛡️ Why This Exists
Most PII scrubbers are built for Western data patterns (SSN, Zip Codes). **dpdpa-pii-scrubber** is built specifically for **Bharat**. It identifies identifiers that are critical under India's **Digital Personal Data Protection (DPDP) Act**, ensuring your AI logs and datasets remain compliant.

## ✨ Features
- 🔍 **Aadhaar Detection:** Supports 12-digit formats with varied spacing.
- 💳 **Financial Identifiers:** PAN cards, IFSC codes, and UPI IDs.
- 🛂 **Identity Docs:** Indian Passports and Voter IDs.
- 📱 **Soft PII:** Mobile numbers (+91) and email addresses.
- ⚡ **Zero Dependency:** Built entirely on Python's standard library.

## 🚀 Installation
```bash
# Clone and use directly in your project
git clone https://github.com/TheIndicSentinel/dpdpa-pii-scrubber.git
```

## 🛠️ Usage

```python
from scrubber import DPDPScrubber

scrubber = DPDPScrubber(mask_char="X", preserve_length=True)

text = "Payment received from user@upi for Aadhaar 1234-5678-9012"
scrubbed = scrubber.scrub(text)

print(scrubbed)
# Output: Payment received from XXXXXXXX for Aadhaar XXXXXXXXXXXXXX
```

## 🏛️ Patterns Supported
| Entity | Pattern Description |
|:---|:---|
| **Aadhaar** | 12-digit UIDAI standard |
| **PAN** | Permanent Account Number (Income Tax Dept) |
| **UPI** | Unified Payments Interface IDs (@oksbi, @ybl, etc.) |
| **IFSC** | Bank branch identifiers |
| **Passport** | Indian Passport numbering |
| **Voter ID** | EPIC numbers |

## ⚡ Use Cases
- **Logging Sanitization:** Scrub PII before sending logs to CloudWatch/Datadog.
- **Dataset Preparation:** Clean raw customer data before fine-tuning local models.
- **Live Middleware:** Redact sensitive info in real-time within Chatbot interfaces.

## ⚖️ Social Proof & Compliance Alignment
Building on the principles of the **Digital Personal Data Protection (DPDP) Act 2023**, this utility helps organizations fulfill:
*   **Data Minimisation:** Collecting/storing only the data necessary for the purpose.
*   **Security Safeguards:** Implementing technical measures to protect personal data.

[![Used By](https://img.shields.io/badge/Used_By-KavachX_Governance-7C3AED?style=flat-square)](https://github.com/TheIndicSentinel/kavachxv2)
[![Compliance](https://img.shields.io/badge/Compliance-DPDP_Ready-10B981?style=flat-square)](#)

## ⚖️ License
Licensed under the [Apache 2.0 License](LICENSE).

---
*Built with conviction by **TheIndicSentinel** — Governance for Bharat.*
