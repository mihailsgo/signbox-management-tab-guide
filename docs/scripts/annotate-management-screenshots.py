from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


ROOT = Path("docs/images/management")
RAW = ROOT / "raw"
ANNOTATED = ROOT / "annotated"
ANNOTATED.mkdir(parents=True, exist_ok=True)


def get_font(size=24):
    for candidate in ["arial.ttf", "segoeui.ttf", "calibri.ttf"]:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


FONT = get_font(24)
SMALL = get_font(20)


def draw_callout(draw, number, target, box_xy, text):
    tx, ty = target
    bx, by = box_xy

    draw.line((tx, ty, bx, by), fill=(230, 40, 40), width=4)
    draw.ellipse((tx - 12, ty - 12, tx + 12, ty + 12), fill=(230, 40, 40), outline=(255, 255, 255), width=2)
    draw.text((tx - 7, ty - 12), str(number), font=SMALL, fill=(255, 255, 255))

    text_w, text_h = draw.multiline_textbbox((0, 0), text, font=SMALL)[2:]
    pad_x, pad_y = 14, 10
    rect = (bx, by, bx + text_w + pad_x * 2, by + text_h + pad_y * 2)
    draw.rounded_rectangle(rect, radius=8, fill=(251, 248, 231), outline=(70, 70, 70), width=2)
    draw.multiline_text((bx + pad_x, by + pad_y), text, font=SMALL, fill=(45, 45, 45), spacing=4)


CONFIGS = {
    "01-login-page.png": [
        (1, (860, 538), (390, 310), "Sign in with your\nwork account email."),
        (2, (860, 598), (390, 380), "Use your assigned\nportal password."),
        (3, (1025, 452), (740, 330), "Use the language selector\nbefore authentication."),
        (4, (860, 668), (740, 420), "Click Sign In to open\nthe portal home."),
    ],
    "02-post-login-home.png": [
        (1, (1325, 34), (1210, 80), "Use Management to open\nconfiguration screens."),
        (2, (366, 147), (80, 180), "Create new process is outside\nManagement scope."),
        (3, (1495, 875), (1230, 760), "Process action buttons stay in\nworkspace, not in Management."),
    ],
    "03-management-overview.png": [
        (1, (1450, 38), (1200, 72), "Top navigation keeps\nManagement context visible."),
        (2, (252, 285), (200, 210), "Left menu switches between\nprofiles and attributes."),
        (3, (480, 168), (460, 66), "Landing opens on\nDocument profiles."),
        (4, (1548, 139), (1240, 170), "Primary action creates\na new profile."),
    ],
    "04-document-profiles-list.png": [
        (1, (460, 310), (450, 85), "Profile name is clickable\nand opens edit form."),
        (2, (1075, 313), (760, 96), "Column headers are the\nprofile review checklist."),
        (3, (1550, 139), (1220, 160), "Create new profile opens\na blank profile form."),
        (4, (1500, 400), (1220, 260), "E-Seal shows whether\na seal profile is set."),
    ],
    "05-document-profiles-detail.png": [
        (1, (380, 145), (500, 78), "This screen edits an\nexisting document profile."),
        (2, (458, 283), (620, 224), "Core identity fields:\nname, type, owner group."),
        (3, (430, 610), (620, 480), "Attributes section links\nreusable metadata fields."),
        (4, (1528, 740), (1270, 845), "Submit saves profile\nchanges to Management."),
    ],
    "06-document-profiles-edit.png": [
        (1, (1176, 355), (680, 160), "E-Seal profile name is used\nwhen sealing is configured."),
        (2, (403, 444), (680, 240), "E-Seal required enforces\nseal usage in processes."),
        (3, (1003, 445), (680, 320), "Review required adds\nmandatory review step."),
        (4, (400, 541), (680, 395), "Do not cancel on decline\nchanges decline behavior."),
    ],
    "07-document-profiles-create-form.png": [
        (1, (380, 145), (500, 76), "Create mode starts with\nempty profile fields."),
        (2, (462, 283), (620, 224), "Complete required fields\nbefore adding attributes."),
        (3, (560, 721), (680, 650), "Attributes can be added by\nNew or Existing selection."),
        (4, (1528, 740), (1260, 845), "Submit creates the profile\nand returns to list."),
    ],
    "08-document-attributes-list.png": [
        (1, (188, 212), (205, 210), "Document attributes section\nis active in left menu."),
        (2, (592, 168), (470, 86), "Attribute table defines\nreusable field catalog."),
        (3, (1484, 168), (730, 98), "Create new attribute opens\nthe attribute modal."),
        (4, (1316, 252), (710, 170), "Required column marks fields\nmandatory for users."),
    ],
    "09-document-attributes-create-form.png": [
        (1, (627, 351), (720, 210), "Modal title confirms\nattribute creation mode."),
        (2, (538, 390), (690, 342), "Attribute name should be\nbusiness-readable."),
        (3, (933, 390), (1040, 330), "Attribute type controls input\nbehavior in forms."),
        (4, (536, 505), (690, 480), "Required means users must\nprovide this value."),
        (5, (1163, 617), (1260, 510), "Submit saves the attribute\nand closes the modal."),
    ],
}


def annotate_file(filename, callouts):
    image = Image.open(RAW / filename).convert("RGB")
    draw = ImageDraw.Draw(image)

    title = "SignBox Management Guide - Annotated"
    draw.rectangle((0, 0, image.width, 42), fill=(20, 50, 105))
    draw.text((12, 8), title, font=FONT, fill=(255, 255, 255))

    for callout in callouts:
        number, target, box_xy, text = callout
        draw_callout(draw, number, target, box_xy, text)

    output_name = filename.replace(".png", "-annotated.png")
    image.save(ANNOTATED / output_name, quality=95)
    print(f"Annotated: {output_name}")


if __name__ == "__main__":
    for name, points in CONFIGS.items():
        annotate_file(name, points)
