import re
import unicodedata
from typing import List, Tuple, Optional

class DPDPScrubber:
    """
    A lightweight, high-performance PII scrubber tailored for India's 
    DPDP (Digital Personal Data Protection) Act patterns.
    """

    # Hard PII — identifiers that are sensitive regardless of context
    HARD_PII_PATTERNS = {
        "aadhaar": r"\b\d{4}[\s\-]?\d{4}[\s\-]?\d{4}\b",
        "pan": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
        "card": r"\b(?:\d{4}[\s\-]?){3}\d{4}\b",
        "ifsc": r"\b[A-Z]{4}0[A-Z0-9]{6}\b",
        "upi": r"\b[\w.\-]+@(?:oksbi|okaxis|okicici|okhdfcbank|ybl|ibl|axl|upi)\b",
        "passport": r"\b[A-PR-WY][1-9]\d{6}\b",
        "voter_id": r"\b[A-Z]{3}\d{7}\b",
    }

    # Soft PII — identifiers that might be technical examples (phone, email)
    SOFT_PII_PATTERNS = {
        "phone": r"\b(?:\+91|0)?[6-9]\d{9}\b",
        "email": r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b",
    }

    def __init__(self, mask_char: str = "*", preserve_length: bool = True):
        self.mask_char = mask_char
        self.preserve_length = preserve_length
        self._patterns = {**self.HARD_PII_PATTERNS, **self.SOFT_PII_PATTERNS}
        self._regexes = {k: re.compile(v, re.IGNORECASE) for k, v in self._patterns.items()}

    def scrub(self, text: str, categories: Optional[List[str]] = None) -> str:
        """
        Redacts PII from the given text.
        :param text: Input string to scan.
        :param categories: List of categories to scrub (e.g. ['aadhaar', 'pan']). 
                           If None, scrubs all.
        """
        if not text:
            return ""

        text = unicodedata.normalize("NFKC", text)
        targets = categories if categories else self._regexes.keys()

        for cat in targets:
            if cat in self._regexes:
                text = self._regexes[cat].sub(self._get_mask, text)
        
        return text

    def _get_mask(self, match: re.Match) -> str:
        val = match.group(0)
        if self.preserve_length:
            return self.mask_char * len(val)
        return f"<{match.lastgroup or 'REDACTED'}>"

    def detect(self, text: str) -> List[Tuple[str, str]]:
        """
        Detects PII and returns a list of (category, value) tuples.
        """
        findings = []
        for cat, regex in self._regexes.items():
            matches = regex.findall(text)
            for m in matches:
                findings.append((cat, m))
        return findings

if __name__ == "__main__":
    scrubber = DPDPScrubber()
    sample = "My Aadhaar is 1234 5678 9012 and my email is test@example.com."
    print(f"Original: {sample}")
    print(f"Scrubbed: {scrubber.scrub(sample)}")
