# Credential Audit Parser

## Overview

A beginner Python project that parses a structured text file, extracts username and password fields, and demonstrates file processing and dictionary-based data organisation.

## Learning Objectives

* Read and process text files in Python.
* Filter lines using string methods.
* Use list comprehensions to extract fields.
* Associate related records using dictionaries.
* Understand the security risks of handling credentials in plaintext.

## How It Works

1. Reads a structured input file.
2. Extracts username and password fields.
3. Associates account records.
4. Demonstrates how credential data can be processed.

## Security Considerations

The initial implementation writes credentials in plaintext. This project should only use synthetic data in an authorised environment. A safer extension would avoid exporting passwords and instead generate a sanitised audit summary.

## Future Improvements

* Validate input records and handle malformed lines.
* Detect missing or duplicate account records.
* Add unit tests.
* Produce a sanitised summary report instead of a plaintext credential export.
