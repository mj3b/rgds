# Citation and provenance correction

The previous README assigned the independent-study DOI to the RGDS v2 implementation. The current citation separates those artifacts.

On September 9, 2026, the public [Zenodo record](https://zenodo.org/records/20242004) identified version `v1.4`, publication date May 16, 2026, and the file `mj3b/rgds-independent-study-v1.4.zip`. Its repository URL and related-work link point to `mj3b/rgds-independent-study`. The displayed file checksum is `md5:b0d5a0a235918b9a26e6ba6b2c3f68eb`. This observation identifies the archive; it is not a new file-integrity verification.

The record assigns `10.5281/zenodo.20242004` to that version and `10.5281/zenodo.20242003` to all versions. The [ORCID profile](https://orcid.org/0009-0001-8121-2878) identifies Mark Julius Banasihan and lists the related RGDS study. ORCID lists a January 2026 work date and a report classification, while Zenodo lists a May 16 deposit publication date and a software classification. This correction preserves those source-specific distinctions.

The implementation's [CITATION.cff](../CITATION.cff) identifies the GitHub repository and author. It includes the archived study as a reference, with the resource type and date reported by Zenodo. It deliberately omits an implementation DOI and release version for the unreleased corrected branch. Reproducible citations should identify the commit used.

Historical releases, tags, files, and authorship remain unchanged. The historical tag is exactly `v.2.0.0`. Future releases should use a new semantic version, without renaming that tag. No ORCID or Zenodo record was edited during this repository correction.

## Previous citation, retained for provenance

This block records the earlier attribution error. Use the current citation metadata for new citations of the implementation.

```bibtex
@software{banasihan2026rgds,
  author    = {Banasihan, Mark Julius},
  title     = {{RGDS}: Regulated Gate Decision Support},
  year      = {2026},
  version   = {2.0.0},
  doi       = {10.5281/zenodo.20242004},
  url       = {https://doi.org/10.5281/zenodo.20242004},
  license   = {Apache-2.0}
}
```
