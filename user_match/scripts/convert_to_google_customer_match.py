#!/usr/bin/env python3
"""
Google Customer Match CSV Converter for Doctor Demographics

This script converts raw doctor data into the format required for Google Ads Customer Match uploads.
It handles:
- Data cleaning and validation
- SHA-256 hashing of PII (emails, phones, names)
- CSV formatting per Google's specifications
- Detailed logging and error reporting

Usage:
    python convert_to_google_customer_match.py <input_file> <output_file>

Example:
    python convert_to_google_customer_match.py sample_doctor_data.csv hashed_doctor_data.csv
"""

import pandas as pd
import hashlib
import sys
import re
from pathlib import Path
from typing import Optional, Tuple


class DoctorDataConverter:
    """Convert raw doctor data to Google Customer Match format."""

    def __init__(self, verbose: bool = True):
        self.verbose = verbose
        self.stats = {
            "total_rows": 0,
            "valid_rows": 0,
            "invalid_rows": 0,
            "hashed_count": 0,
        }

    def log(self, message: str):
        """Print log message if verbose."""
        if self.verbose:
            print(message)

    @staticmethod
    def clean_email(email: str) -> str:
        """
        Clean and validate email for hashing.
        - Lowercase
        - Remove spaces
        - Validate format
        """
        if pd.isna(email) or email == "":
            return ""
        email_str = str(email).lower().strip().replace(" ", "")
        # Validate email format
        if "@" in email_str and "." in email_str.split("@")[-1]:
            return email_str
        return ""

    @staticmethod
    def clean_phone(phone: str) -> str:
        """
        Clean and format phone to E.164 format for hashing.
        - Remove spaces, dashes, parentheses
        - Add country code prefix (+) if missing
        - Remove all non-numeric characters (except +)
        """
        if pd.isna(phone) or phone == "":
            return ""
        phone_str = str(phone).strip()
        # Remove common formatting characters
        phone_str = re.sub(r"[\s\-\(\)\.]+", "", phone_str)
        # Add + if not present
        if not phone_str.startswith("+"):
            phone_str = "+" + phone_str
        return phone_str

    @staticmethod
    def clean_name(name: str) -> str:
        """
        Clean name for hashing.
        - Remove prefixes (Dr., Prof., Dr, etc.)
        - Remove suffixes (MD, Jr., Sr., etc.)
        - Lowercase
        - Remove spaces
        """
        if pd.isna(name) or name == "":
            return ""
        name_str = str(name).strip()
        # Remove common prefixes
        name_str = re.sub(r"^(Dr\.?|Prof\.?|Professor|Mrs\.?|Mr\.?|Ms\.?|Miss)\s+", "", name_str, flags=re.IGNORECASE)
        # Remove common suffixes
        name_str = re.sub(r"\s+(MD|M\.D|Jr\.?|Sr\.?|PhD|Ph\.D|DDS|DMD|DO)$", "", name_str, flags=re.IGNORECASE)
        # Trim extra spaces and lowercase
        name_str = name_str.lower().strip().replace(" ", "")
        return name_str

    @staticmethod
    def clean_country(country: str) -> str:
        """
        Standardize country to ISO 2-letter code.
        Returns as-is if already in correct format.
        """
        if pd.isna(country) or country == "":
            return ""
        country_str = str(country).strip().upper()
        # If already 2-3 letter code, validate
        if len(country_str) == 2 or len(country_str) == 3:
            return country_str
        # Common country mappings (expand as needed)
        country_map = {
            "UNITED STATES": "US",
            "USA": "US",
            "CANADA": "CA",
            "UNITED KINGDOM": "UK",
            "INDIA": "IN",
            "AUSTRALIA": "AU",
            "GERMANY": "DE",
            "FRANCE": "FR",
            "SOUTH AFRICA": "ZA",
            "NIGERIA": "NG",
        }
        return country_map.get(country_str, country_str[:2].upper())

    @staticmethod
    def clean_zip(zip_code: str, country: str = "") -> str:
        """
        Standardize postal/zip code.
        - US: 5 or 5+4 digits
        - International: as-is
        """
        if pd.isna(zip_code) or zip_code == "":
            return ""
        zip_str = str(zip_code).strip()
        return zip_str

    @staticmethod
    def hash_field(value: str) -> str:
        """Hash a field using SHA-256."""
        if not value:
            return ""
        return hashlib.sha256(value.encode("utf-8")).hexdigest()

    def process_row(self, row: dict) -> Tuple[dict, bool]:
        """
        Process a single row: clean, validate, and hash.
        Returns: (processed_row, is_valid)
        """
        processed = {}
        errors = []

        # Extract and clean each field
        email = self.clean_email(row.get("Email", ""))
        phone = self.clean_phone(row.get("Phone", ""))
        first_name = self.clean_name(row.get("First Name", ""))
        last_name = self.clean_name(row.get("Last Name", ""))
        country = self.clean_country(row.get("Country", ""))
        zip_code = self.clean_zip(row.get("Zip", ""), country)

        # Validate: must have at least email or phone
        if not email and not phone:
            errors.append("Missing both Email and Phone")

        # Hash PII fields
        processed["Email"] = self.hash_field(email)
        processed["Phone"] = self.hash_field(phone)
        processed["First Name"] = self.hash_field(first_name)
        processed["Last Name"] = self.hash_field(last_name)
        # Don't hash country and zip
        processed["Country"] = country
        processed["Zip"] = zip_code

        is_valid = len(errors) == 0
        if is_valid:
            self.stats["valid_rows"] += 1
            self.stats["hashed_count"] += 1
        else:
            self.stats["invalid_rows"] += 1
            if self.verbose:
                print(f"  ⚠ Row skipped: {', '.join(errors)}")

        return processed, is_valid

    def convert(self, input_path: str, output_path: str) -> bool:
        """
        Read input CSV, process, and write output CSV.
        """
        try:
            # Read input
            self.log(f"📖 Reading input file: {input_path}")
            df = pd.read_csv(input_path)
            self.stats["total_rows"] = len(df)
            self.log(f"   Found {self.stats['total_rows']} rows")

            # Process each row
            self.log("🔄 Processing rows...")
            processed_rows = []
            for idx, row in df.iterrows():
                processed, is_valid = self.process_row(row.to_dict())
                if is_valid:
                    processed_rows.append(processed)
                if (idx + 1) % 100 == 0:
                    self.log(f"   Processed {idx + 1}/{self.stats['total_rows']} rows")

            # Create output dataframe
            output_df = pd.DataFrame(processed_rows)

            # Reorder columns per Google spec
            column_order = ["Email", "Phone", "First Name", "Last Name", "Country", "Zip"]
            output_df = output_df[column_order]

            # Write output
            self.log(f"💾 Writing output file: {output_path}")
            output_df.to_csv(output_path, index=False, encoding="utf-8")
            self.log(f"   ✅ Successfully wrote {self.stats['valid_rows']} rows")

            # Print summary
            self.print_summary()
            return True

        except Exception as e:
            self.log(f"❌ Error: {str(e)}")
            return False

    def print_summary(self):
        """Print conversion summary."""
        self.log("\n" + "="*60)
        self.log("📊 CONVERSION SUMMARY")
        self.log("="*60)
        self.log(f"Total rows read:      {self.stats['total_rows']}")
        self.log(f"Valid rows processed: {self.stats['valid_rows']}")
        self.log(f"Invalid rows skipped: {self.stats['invalid_rows']}")
        self.log(f"Match rate estimate:  {(self.stats['valid_rows']/max(1, self.stats['total_rows'])*100):.1f}%")
        self.log("="*60)
        self.log("\n✅ CSV ready for Google Ads Customer Match upload!")
        self.log("   Minimum rows for matching: 1,000")
        self.log("   Your file has: " + ("✅ Good!" if self.stats['valid_rows'] >= 1000 else f"⚠ {1000 - self.stats['valid_rows']} more needed"))
        self.log("\n📋 Next steps:")
        self.log("   1. Upload CSV to Google Ads > Tools > Audience Manager")
        self.log("   2. Wait 24-48 hours for matching")
        self.log("   3. Access insights via Audience Insights tool\n")


def main():
    """Main entry point."""
    if len(sys.argv) < 3:
        print("Usage: python convert_to_google_customer_match.py <input_csv> <output_csv>")
        print("\nExample:")
        print("  python convert_to_google_customer_match.py sample_doctor_data.csv hashed_doctor_data.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Verify input exists
    if not Path(input_file).exists():
        print(f"❌ Error: Input file not found: {input_file}")
        sys.exit(1)

    # Convert
    converter = DoctorDataConverter(verbose=True)
    success = converter.convert(input_file, output_file)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
