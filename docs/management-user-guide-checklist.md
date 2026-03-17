# Management User Guide Checklist

## Scope Verification

- [x] Logged in to `https://signbox.trustlynx.com/`
- [x] Opened top navigation **Management**
- [x] Documented only Management internals
- [x] Kept Home/Drafts/History/Contacts only as navigation context

## Visited Management Pages

- [x] Management landing/overview
- [x] Document profiles list
- [x] Document profiles detail (opened from profile name link)
- [x] Document profiles edit form
- [x] Document profiles create form
- [x] Document attributes list
- [x] Document attributes create form

## Documented Workflows

- [x] Open Management from top navigation
- [x] Review Document profiles table
- [x] Open existing profile details
- [x] Edit existing profile
- [x] Create new profile
- [x] Open Document attributes
- [x] Create new attribute

## Captured Screenshots (Raw)

- [x] `docs/images/management/raw/01-login-page.png`
- [x] `docs/images/management/raw/02-post-login-home.png`
- [x] `docs/images/management/raw/03-management-overview.png`
- [x] `docs/images/management/raw/04-document-profiles-list.png`
- [x] `docs/images/management/raw/05-document-profiles-detail.png`
- [x] `docs/images/management/raw/06-document-profiles-edit.png`
- [x] `docs/images/management/raw/07-document-profiles-create-form.png`
- [x] `docs/images/management/raw/08-document-attributes-list.png`
- [x] `docs/images/management/raw/09-document-attributes-create-form.png`

## Captured Screenshots (Annotated)

- [x] `docs/images/management/annotated/01-login-page-annotated.png`
- [x] `docs/images/management/annotated/02-post-login-home-annotated.png`
- [x] `docs/images/management/annotated/03-management-overview-annotated.png`
- [x] `docs/images/management/annotated/04-document-profiles-list-annotated.png`
- [x] `docs/images/management/annotated/05-document-profiles-detail-annotated.png`
- [x] `docs/images/management/annotated/06-document-profiles-edit-annotated.png`
- [x] `docs/images/management/annotated/07-document-profiles-create-form-annotated.png`
- [x] `docs/images/management/annotated/08-document-attributes-list-annotated.png`
- [x] `docs/images/management/annotated/09-document-attributes-create-form-annotated.png`

## Screenshot QA (Artifacts / Clarity Review)

- [x] Checked all 18 screenshots (9 raw + 9 annotated).
- [x] Replaced initial auto-annotation set with cleaner manual annotation positions.
- [x] Removed mislabeled "detail" wording confusion by describing the opened profile screen as editable form.
- [x] Verified no broken image files, no cut-off main controls, and consistent resolution.
- [x] Verified annotation text is readable and user-focused.

## Covered UI Elements

- [x] Top Management tab in navigation
- [x] Subsection difference: Document profiles vs Document attributes
- [x] Document profiles columns:
  - [x] Profile name
  - [x] Document type
  - [x] Owner group
  - [x] Attribute count
  - [x] E-Seal
- [x] Profile name link behavior (opens detail)
- [x] Create new profile action
- [x] Profile edit/create form fields
- [x] Document attributes columns:
  - [x] Attribute name
  - [x] Attribute type
  - [x] Required
- [x] Create new attribute action and form fields

## Blockers

- [x] No MFA/OTP/CAPTCHA blocker encountered.
- [ ] N/A

## Assumptions and Limits

- Some fields/buttons are interpreted from visible labels and standard UI behavior.
- Document attributes list had no visible existing rows during capture; row-based open/edit flow could not be verified.
- No destructive submit actions were completed intentionally; forms were explored for documentation only.

## Quality Review

- [x] Steps are ordered and beginner-friendly
- [x] Screenshot references match guide sections
- [x] Major visible Management screens are covered
- [x] Common confusion points and FAQ included
- [x] Quick start summary included
