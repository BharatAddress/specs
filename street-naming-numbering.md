# Street Naming and Numbering Guidance

Authoritative source: the ULB. Maintain a Street Name Register with unique `street_id` per street and track aliases. Assign logical, monotonic house numbers per street segment; allow suffixes for infill (e.g., 16A, 16B).

Key rules:
- One `street_id` per unique street within a ULB.
- House numbers must be unique per `street_id` for top-level addresses.
- Record locality, ward, and ULB LGD codes for joins.

Outputs feed the Bharat Address Register schema (`address-register.schema.json`).
