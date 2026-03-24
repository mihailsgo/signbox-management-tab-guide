# Management User Guide Validation Checklist

## Scope and source verification

- [x] Screenshots and instructions validated against `https://signbox.trustlynx.com/`.
- [x] UI labels cross-checked with `apps/internal/public/locales/en.json`.
- [x] Screen behavior cross-checked with frontend management components.
- [x] Data-contract statements cross-checked with backend document profile/attribute controllers and models.

## Screenshot inventory (fresh capture set)

Raw:
- [x] `docs/images/management/raw/01-login-page.png`
- [x] `docs/images/management/raw/02-post-login-home.png`
- [x] `docs/images/management/raw/03-management-overview.png`
- [x] `docs/images/management/raw/04-document-profiles-list.png`
- [x] `docs/images/management/raw/05-document-profiles-detail.png`
- [x] `docs/images/management/raw/06-document-profiles-edit.png`
- [x] `docs/images/management/raw/07-document-profiles-create-form.png`
- [x] `docs/images/management/raw/08-document-attributes-list.png`
- [x] `docs/images/management/raw/09-document-attributes-create-form.png`

Annotated:
- [x] `docs/images/management/annotated/01-login-page-annotated.png`
- [x] `docs/images/management/annotated/02-post-login-home-annotated.png`
- [x] `docs/images/management/annotated/03-management-overview-annotated.png`
- [x] `docs/images/management/annotated/04-document-profiles-list-annotated.png`
- [x] `docs/images/management/annotated/05-document-profiles-detail-annotated.png`
- [x] `docs/images/management/annotated/06-document-profiles-edit-annotated.png`
- [x] `docs/images/management/annotated/07-document-profiles-create-form-annotated.png`
- [x] `docs/images/management/annotated/08-document-attributes-list-annotated.png`
- [x] `docs/images/management/annotated/09-document-attributes-create-form-annotated.png`

## Pointer QA pass 1 (author validation)

- [x] Every callout has a visible red target marker.
- [x] Every marker points to the intended UI control or data area.
- [x] No pointer targets empty space outside intended control area.
- [x] No callout text duplicates trivial UI labels (for example "click here").
- [x] All screenshots remain readable after annotation.

## Pointer QA pass 2 (independent re-check)

- [x] Reopened all 9 annotated images for second-pass verification.
- [x] Rechecked pointer-to-text mapping against guide instructions.
- [x] Corrected pointer coordinates where ambiguity was detected.
- [x] Confirmed all final pointers land on intended components.

## Senior visual review sign-off (web designer perspective)

- [x] Target component is fully visible for each callout.
- [x] Annotation boxes do not hide critical controls.
- [x] Visual hierarchy is clear (primary actions remain visually dominant).
- [x] Text contrast and readability are sufficient in all callouts.
- [x] Screenshots rejected/remade if alignment or clarity was weak.

## Documentation quality verification

- [x] Guide is task-first and junior-user readable.
- [x] Every screen/flow explains purpose, usage, navigation, click path, and expected result.
- [x] Field-level meaning and pre-submit checks are documented.
- [x] Common mistakes and recovery actions are documented.
- [x] Callout explanations are included under each screenshot.
- [x] Markdown image links and paths resolve correctly.
