# Bharat Address Specifications

Website: https://bharataddress.github.io

![Schema Lint](https://github.com/BharatAddress/specs/actions/workflows/schema-lint.yml/badge.svg)

Purpose: normative documents and schemas for the Bharat Address Open Source Project. This repo defines the minimal address feature schema (JSON Schema draft 2020-12) and related guidance for ULBs and integrators.

Contents:
- `address-register.schema.json`: Minimal JSON Schema for address features
- `street-naming-numbering.md`: Guidance for ULBs
- `digipin-integration.md`: DIGIPIN entrance point selection and privacy notes
- `lgd-ulb-codes.md`: How to key every record to LGD and wards
- `ulpin-linkage.md`: Optional linkage to ULPIN
- `ogc-api-features.yml` / `ogc-api-features.json`: OpenAPI 3.1 for OGC API Features
- `examples/`: Example Feature/FeatureCollection and API responses
- `scripts/`: Schema and example validators
- `DATA_DICTIONARY.md`: Field-by-field semantics
- `CONFORMANCE.md`: OGC conformance notes
- `CHANGELOG.md`: Versioned changes

Licensing: documentation and schemas are under CC BY 4.0.

Versioning: semantic versioning. Current release: `0.1.0`.

Conformance: see `CONFORMANCE.md` for OGC API - Features alignment.

References:
- India Post DIGIPIN: https://www.indiapost.gov.in/digipin
- Know Your DIGIPIN: https://dac.indiapost.gov.in/mydigipin/home
- LGD Portal: https://lgdirectory.gov.in/
- OGC API Features: https://ogcapi.ogc.org/features/
