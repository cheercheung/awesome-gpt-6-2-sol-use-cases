# Maintenance

The [curated data](../data/gpt-6-2-sol-usecase-curated.json) records the numbered source posts. The English README supplies the editorial copy. The data and all eleven README files use the same topic order, author credits, case anchors, media links, dates, and verbatim prompts. Numbers stay attached to their source posts when cases move between topic sections.

## Add or correct a case

1. Record the original post, author, date, task, and visible outcome. Keep the creator's model claim separate from verified model identity.
2. Preserve all source media and identify footage reused across posts in the data. Label unfinished attempts as limits.
3. Write a source-linked case heading, a practical takeaway, evidence notes, and the type and date. Include the prompt when the creator published it verbatim.
4. Sort the centralized menu by source publication time, newest first. In the case sections, use the same order within each topic and place the topic with the newest case first. Update totals and keep the curated data in case-section order. Use the same ordering in all eleven READMEs and keep the prompts in their original language.
5. Compare the source, prompt, and media set against all eleven README files. Inspect the desktop and narrow render.

## Checks before publication

Regenerate the [public case catalog](usecase-catalog.md) after you change the English Menu or curated data. It follows the Menu order and sources case details from the JSON.

```sh
python3 scripts/build_case_index.py
python3 scripts/build_case_index.py --check
git diff --check
```

For the full review, use the installed Model Repository Pipeline. Set `PIPELINE` to the framework directory. Set `INTAKE`, `SCHEMA`, `SCHEMA_SHA256`, and `EVIDENCE_DIR` to the locked intake, independently reviewed localization schema, its SHA-256, and the external evidence directory for the run.

```sh
python3 "$PIPELINE/bundled-skills/usecase-update-loop/scripts/verify_usecase_update.py" --repo .
python3 "$PIPELINE/scripts/verify_localized_readmes.py" --repo . --shape usecase \
  --usecase-schema "$SCHEMA" --usecase-schema-sha256 "$SCHEMA_SHA256" --json
python3 "$PIPELINE/scripts/model_repo_orchestrator.py" surface-audit --repo . \
  --shape usecase --run-mode recurring-update --intake "$INTAKE" --out "$EVIDENCE_DIR/surfaces.md"
python3 "$PIPELINE/scripts/model_repo_orchestrator.py" public-policy-audit --repo . \
  --shape usecase --run-mode recurring-update --intake "$INTAKE" --out "$EVIDENCE_DIR/public-policy.md"
python3 "$PIPELINE/scripts/audit_public_links.py" --repo . --out "$EVIDENCE_DIR/public-links.md"
```

Compare the expected source media with rendered cases by exact commit. Check R2 image bytes, video poster links, and playback. Inspect the GitHub render at desktop and narrow widths, then repeat the public readback after publication.

## License scope

Original editorial content is licensed under [CC BY 4.0](../LICENSE). Quoted prompts, linked or embedded demonstrations, and other creator media remain subject to their original rights and terms.
