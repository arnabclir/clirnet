#!/usr/bin/env python3
"""
Facebook Custom Audiences CSV Converter

Converts raw doctor data into the format required for Facebook Custom Audiences uploads.
Handles data cleaning, normalization, and optional SHA-256 hashing.

Facebook Format Requirements:
- Headers: email, phone, fn, ln, ct, st, zip, country, dob, gen
- Phone: E.164 format with + prefix
- All text: lowercase, trimmed
- Country: 2-letter ISO code (required)

Usage:
    python convert_to_facebook_custom_audience.py <input_file> <output_file>

Example:
    python convert_to_facebook_custom_audience.py sample_doctor_data.csv facebook_audience.csv
"""

import csv
import hashlib
import sys
import re
from pathlib import Path
from typing import Dict, Tuple


class FacebookAudienceConverter:
    """Convert raw data to Facebook Custom Audiences format."""

    def __init__(self, verbose: bool = True, hash_data: bool = False):
        self.verbose = verbose
        self.hash_data = hash_data
        self.stats = {
            "total_rows": 0,
            "valid_rows": 0,
            "invalid_rows": 0,
        }

    def log(self, message: str):
        """Print log message if verbose."""
        if self.verbose:
            print(message)

    @staticmethod
    def clean_email(email: str) -> str:
        """
        Clean and validate email for Facebook.
        - Lowercase
        - Remove spaces
        - Validate format
        - Remove dots in Gmail (optional but recommended)
        """
        if not email or email.strip() == "":
            return ""
        email_str = str(email).lower().strip().replace(" ", "")
        # Validate email format
        if "@" in email_str and "." in email_str.split("@")[-1]:
            # Optional: Remove dots in Gmail addresses
            if email_str.endswith("@gmail.com"):
                local = email_str.split("@")[0].replace(".", "")
                email_str = local + "@gmail.com"
            return email_str
        return ""

    @staticmethod
    def clean_phone(phone: str) -> str:
        """
        Clean and format phone to E.164 format for Facebook.
        - Must include + prefix
        - Format: +[country code][number]
        - Remove all spaces, dashes, parentheses
        """
        if not phone or phone.strip() == "":
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
        Clean name for Facebook.
        - Remove prefixes (Dr., Prof., etc.)
        - Remove suffixes (MD, Jr., etc.)
        - Lowercase
        - Remove extra spaces (but keep internal spaces initially, then remove for hashing)
        """
        if not name or name.strip() == "":
            return ""
        name_str = str(name).strip()
        # Remove common prefixes
        name_str = re.sub(
            r"^(Dr\.?|Prof\.?|Professor|Mrs\.?|Mr\.?|Ms\.?|Miss)\s+",
            "",
            name_str,
            flags=re.IGNORECASE,
        )
        # Remove common suffixes
        name_str = re.sub(
            r"\s+(MD|M\.D|Jr\.?|Sr\.?|PhD|Ph\.D|DDS|DMD|DO)$",
            "",
            name_str,
            flags=re.IGNORECASE,
        )
        # Lowercase and trim
        name_str = name_str.lower().strip()
        return name_str

    @staticmethod
    def clean_city(city: str) -> str:
        """
        Clean city name for Facebook.
        - Lowercase
        - Remove spaces (Facebook requirement)
        """
        if not city or city.strip() == "":
            return ""
        city_str = str(city).lower().strip().replace(" ", "")
        return city_str

    @staticmethod
    def clean_state(state: str) -> str:
        """
        Standardize state/province to 2-letter code.
        - US: CA, NY, TX, etc.
        - India: MH, DL, KA, etc.
        - Lowercase for Facebook
        """
        if not state or state.strip() == "":
            return ""
        state_str = str(state).strip().lower()
        # If already 2 letters, return as-is
        if len(state_str) == 2:
            return state_str
        # State name mappings (expand as needed)
        state_map = {
            "california": "ca",
            "new york": "ny",
            "texas": "tx",
            "maharashtra": "mh",
            "delhi": "dl",
            "karnataka": "ka",
            "tamil nadu": "tn",
        }
        return state_map.get(state_str, state_str[:2])

    @staticmethod
    def clean_country(country: str) -> str:
        """
        Standardize country to 2-letter ISO code (REQUIRED by Facebook).
        - US, GB, IN, CA, AU, etc.
        - Lowercase for Facebook
        """
        if not country or country.strip() == "":
            return ""
        country_str = str(country).strip().lower()
        # If already 2-3 letters, validate
        if len(country_str) == 2 or len(country_str) == 3:
            return country_str[:2]  # Always use 2-letter
        # Country name mappings
        country_map = {
            "united states": "us",
            "usa": "us",
            "india": "in",
            "canada": "ca",
            "united kingdom": "uk",
            "great britain": "gb",
            "australia": "au",
            "germany": "de",
            "france": "fr",
        }
        return country_map.get(country_str, country_str[:2])

    @staticmethod
    def clean_zip(zip_code: str) -> str:
        """
        Standardize postal/ZIP code.
        - US: 5 or 9 digits
        - International: as-is
        - NO hashing for zip (Facebook requirement)
        """
        if not zip_code or zip_code.strip() == "":
            return ""
        zip_str = str(zip_code).strip()
        return zip_str

    @staticmethod
    def clean_gender(gender: str) -> str:
        """
        Standardize gender to Facebook format.
        - "m" for male
        - "f" for female
        """
        if not gender or gender.strip() == "":
            return ""
        gender_str = str(gender).strip().lower()
        if gender_str in ["m", "male", "man"]:
            return "m"
        elif gender_str in ["f", "female", "woman"]:
            return "f"
        return ""

    @staticmethod
    def hash_field(value: str) -> str:
        """
        Hash a field using SHA-256 (lowercase hex).
        Facebook requires lowercase hexadecimal output.
        """
        if not value or value.strip() == "":
            return ""
        # Remove spaces for hashing
        value_no_spaces = value.replace(" ", "")
        return hashlib.sha256(value_no_spaces.encode("utf-8")).hexdigest().lower()

    def process_row(self, row: Dict[str, str]) -> Tuple[Dict[str, str], bool]:
        """
        Process a single row: clean, validate, and optionally hash.
        Returns: (processed_row, is_valid)
        """
        processed = {}
        errors = []

        # Extract and clean each field
        email = self.clean_email(row.get("Email", ""))
        phone = self.clean_phone(row.get("Phone", ""))
        first_name = self.clean_name(row.get("First Name", ""))
        last_name = self.clean_name(row.get("Last Name", ""))
        city = self.clean_city(
            row.get("City", row.get("Zip", ""))
        )  # Fallback to Zip field if no City
        state = self.clean_state(row.get("State", row.get("Zip", "")))
        country = self.clean_country(row.get("Country", ""))
        zip_code = self.clean_zip(row.get("Zip", ""))
        gender = self.clean_gender(row.get("Gender", ""))

        # Validate: must have at least email or phone
        if not email and not phone:
            errors.append("Missing both Email and Phone")

        # Facebook REQUIRES country
        if not country:
            errors.append("Missing Country (required by Facebook)")

        # Process fields (hash if requested)
        if self.hash_data:
            processed["email"] = self.hash_field(email) if email else ""
            processed["phone"] = self.hash_field(phone) if phone else ""
            processed["fn"] = self.hash_field(first_name) if first_name else ""
            processed["ln"] = self.hash_field(last_name) if last_name else ""
            processed["ct"] = self.hash_field(city) if city else ""
            processed["st"] = self.hash_field(state) if state else ""
            processed["gen"] = self.hash_field(gender) if gender else ""
        else:
            # Unhashed data (Facebook will hash during upload)
            processed["email"] = email
            processed["phone"] = phone
            processed["fn"] = first_name
            processed["ln"] = last_name
            processed["ct"] = city
            processed["st"] = state
            processed["gen"] = gender

        # Never hash country and zip (Facebook requirement)
        processed["country"] = country
        processed["zip"] = zip_code

        is_valid = len(errors) == 0
        if is_valid:
            self.stats["valid_rows"] += 1
        else:
            self.stats["invalid_rows"] += 1
            if self.verbose:
                print(f"  ⚠ Row skipped: {', '.join(errors)}")

        return processed, is_valid

    def convert(self, input_path: str, output_path: str) -> bool:
        """
        Read input CSV, process, and write output CSV for Facebook.
        """
        try:
            # Read input
            self.log(f"📖 Reading input file: {input_path}")
            rows_read = 0
            processed_rows = []

            with open(input_path, "r", encoding="utf-8") as infile:
                reader = csv.DictReader(infile)
                for row in reader:
                    rows_read += 1
                    self.stats["total_rows"] = rows_read
                    processed, is_valid = self.process_row(row)
                    if is_valid:
                        processed_rows.append(processed)
                    if rows_read % 100 == 0:
                        self.log(f"   Processed {rows_read} rows")

            self.log(f"   Found {self.stats['total_rows']} rows")

            # Write output
            self.log(f"💾 Writing output file: {output_path}")

            # Facebook column order
            column_order = [
                "email",
                "phone",
                "fn",
                "ln",
                "ct",
                "st",
                "zip",
                "country",
                "gen",
            ]

            with open(output_path, "w", newline="", encoding="utf-8") as outfile:
                writer = csv.DictWriter(outfile, fieldnames=column_order)
                writer.writeheader()
                writer.writerows(processed_rows)

            self.log(f"   ✅ Successfully wrote {self.stats['valid_rows']} rows")

            # Print summary
            self.print_summary()
            return True

        except Exception as e:
            self.log(f"❌ Error: {str(e)}")
            import traceback

            traceback.print_exc()
            return False

    def print_summary(self):
        """Print conversion summary."""
        self.log("\n" + "=" * 60)
        self.log("📊 CONVERSION SUMMARY")
        self.log("=" * 60)
        self.log(f"Total rows read:      {self.stats['total_rows']}")
        self.log(f"Valid rows processed: {self.stats['valid_rows']}")
        self.log(f"Invalid rows skipped: {self.stats['invalid_rows']}")
        match_rate = (
            (self.stats["valid_rows"] / max(1, self.stats["total_rows"]) * 100)
            if self.stats["total_rows"] > 0
            else 0
        )
        self.log(f"Conversion rate:      {match_rate:.1f}%")
        self.log(
            f"Data hashed:          {'Yes (SHA-256)' if self.hash_data else 'No (Facebook will auto-hash)'}"
        )
        self.log("=" * 60)
        self.log("\n✅ CSV ready for Facebook Custom Audiences upload!")
        self.log("   Minimum rows for upload: 100")
        self.log("   Maximum rows per upload: 10,000")
        if self.stats["valid_rows"] >= 100:
            self.log("   Your file has: ✅ Good!")
        else:
            self.log(
                f"   Your file has: ⚠ {100 - self.stats['valid_rows']} more rows needed"
            )
        self.log("\n📋 Next steps:")
        self.log("   1. Go to Facebook Business Manager > Audiences")
        self.log("   2. Create Audience > Custom Audience > Customer List")
        self.log("   3. Upload this CSV file")
        self.log("   4. Map columns (should auto-detect)")
        self.log("   5. Wait 24-48 hours for matching")
        self.log("   6. Access insights via Meta Business Suite\n")


def main():
    """Main entry point."""
    if len(sys.argv) < 3:
        print(
            "Usage: python convert_to_facebook_custom_audience.py <input_csv> <output_csv> [--hash]"
        )
        print("\nOptions:")
        print(
            "  --hash    Pre-hash data with SHA-256 (optional, Facebook will hash if not provided)"
        )
        print("\nExample:")
        print(
            "  python convert_to_facebook_custom_audience.py sample_doctor_data.csv facebook_audience.csv"
        )
        print(
            "  python convert_to_facebook_custom_audience.py sample_data.csv output.csv --hash"
        )
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    hash_data = "--hash" in sys.argv

    # Verify input exists
    if not Path(input_file).exists():
        print(f"❌ Error: Input file not found: {input_file}")
        sys.exit(1)

    # Convert
    converter = FacebookAudienceConverter(verbose=True, hash_data=hash_data)
    success = converter.convert(input_file, output_file)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
