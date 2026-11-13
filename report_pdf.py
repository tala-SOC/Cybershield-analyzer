from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    PageBreak,
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepTogether
)


def generate_pdf(report, filename):

    # =========================================================
    # COLORS
    # =========================================================

    NAVY = colors.HexColor("#080B2A")
    PURPLE = colors.HexColor("#6C3CE9")
    BLUE = colors.HexColor("#2563EB")

    LIGHT_BG = colors.HexColor("#F5F7FF")
    CARD_BG = colors.HexColor("#FFFFFF")

    DARK = colors.HexColor("#172033")
    GRAY = colors.HexColor("#667085")

    GREEN = colors.HexColor("#16A34A")
    RED = colors.HexColor("#DC2626")
    ORANGE = colors.HexColor("#EA580C")

    WHITE = colors.white


    # =========================================================
    # DOCUMENT
    # =========================================================

    doc = SimpleDocTemplate(

        filename,

        pagesize=A4,

        rightMargin=18 * mm,
        leftMargin=18 * mm,

        topMargin=18 * mm,
        bottomMargin=18 * mm
    )


    # =========================================================
    # STYLES
    # =========================================================

    styles = getSampleStyleSheet()


    title_style = ParagraphStyle(

        "CyberTitle",

        parent=styles["Title"],

        fontName="Helvetica-Bold",

        fontSize=25,

        leading=30,

        alignment=TA_CENTER,

        textColor=WHITE,

        spaceAfter=8
    )


    subtitle_style = ParagraphStyle(

        "CyberSubtitle",

        parent=styles["Normal"],

        fontName="Helvetica",

        fontSize=10,

        leading=14,

        alignment=TA_CENTER,

        textColor=colors.HexColor("#D8D9FF")
    )


    section_style = ParagraphStyle(

        "Section",

        parent=styles["Heading2"],

        fontName="Helvetica-Bold",

        fontSize=14,

        leading=18,

        textColor=NAVY,

        spaceBefore=4,

        spaceAfter=8
    )


    normal_style = ParagraphStyle(

        "NormalCyber",

        parent=styles["Normal"],

        fontName="Helvetica",

        fontSize=9.5,

        leading=14,

        textColor=DARK
    )


    small_style = ParagraphStyle(

        "Small",

        parent=styles["Normal"],

        fontName="Helvetica",

        fontSize=8,

        leading=11,

        textColor=GRAY
    )


    value_style = ParagraphStyle(

        "Value",

        parent=normal_style,

        fontName="Helvetica-Bold",

        textColor=NAVY
    )


    center_value = ParagraphStyle(

        "CenterValue",

        parent=normal_style,

        fontName="Helvetica-Bold",

        fontSize=18,

        alignment=TA_CENTER,

        textColor=NAVY
    )


    # =========================================================
    # HELPERS
    # =========================================================

    def card(data, widths=None):

        table = Table(

            [[data]],

            colWidths=widths

        )

        table.setStyle(

            TableStyle([

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    CARD_BG
                ),

                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    0.7,
                    colors.HexColor("#E3E7F5")
                ),

                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    12
                ),

                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    12
                ),

                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    12
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    12
                )

            ])

        )

        return table


    # =========================================================
    # STORY
    # =========================================================

    story = []


    # =========================================================
    # HEADER
    # =========================================================

    header_data = [

        [
            Paragraph(
                "🛡 CYBERSHIELD",
                title_style
            )
        ],

        [
            Paragraph(
                "WEBSITE SECURITY ASSESSMENT",
                subtitle_style
            )
        ]

    ]


    header = Table(

        header_data,

        colWidths=[174 * mm],

        rowHeights=[18 * mm, 10 * mm]

    )


    header.setStyle(

        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (-1, -1),
                NAVY
            ),

            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                PURPLE
            ),

            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),

            (
                "ALIGN",
                (0, 0),
                (-1, -1),
                "CENTER"
            ),

            (
                "LEFTPADDING",
                (0, 0),
                (-1, -1),
                10
            ),

            (
                "RIGHTPADDING",
                (0, 0),
                (-1, -1),
                10
            )

        ])

    )


    story.append(header)

    story.append(Spacer(1, 15))


    # =========================================================
    # TARGET
    # =========================================================

    story.append(

        Paragraph(
            "🎯 Target Information",
            section_style
        )

    )


    target_data = [

        [
            Paragraph(
                "<b>Website</b>",
                small_style
            ),

            Paragraph(
                str(report.get("target", "Unknown")),
                value_style
            )
        ],

        [
            Paragraph(
                "<b>URL</b>",
                small_style
            ),

            Paragraph(
                str(report.get("url", "Unknown")),
                normal_style
            )
        ]

    ]


    target_table = Table(

        target_data,

        colWidths=[
            38 * mm,
            130 * mm
        ]

    )


    target_table.setStyle(

        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (-1, -1),
                CARD_BG
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.HexColor("#E3E7F5")
            ),

            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),

            (
                "LEFTPADDING",
                (0, 0),
                (-1, -1),
                10
            ),

            (
                "RIGHTPADDING",
                (0, 0),
                (-1, -1),
                10
            ),

            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                9
            ),

            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                9
            )

        ])

    )


    story.append(target_table)

    story.append(Spacer(1, 15))


    # =========================================================
    # GENERAL INFORMATION
    # =========================================================

    story.append(

        Paragraph(
            "📊 General Information",
            section_style
        )

    )


    general_data = [

        [
            Paragraph("<b>Status Code</b>", small_style),
            Paragraph(
                str(report.get("status", "Unknown")),
                value_style
            ),

            Paragraph("<b>Response Time</b>", small_style),
            Paragraph(
                f"{report.get('response_time', 'Unknown')} sec",
                value_style
            )
        ],

        [
            Paragraph("<b>Server</b>", small_style),
            Paragraph(
                str(report.get("server", "Unknown")),
                value_style
            ),

            Paragraph("<b>Content Type</b>", small_style),
            Paragraph(
                str(report.get("content_type", "Unknown")),
                value_style
            )
        ]

    ]


    general_table = Table(

        general_data,

        colWidths=[
            30 * mm,
            53 * mm,
            32 * mm,
            59 * mm
        ]

    )


    general_table.setStyle(

        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (-1, -1),
                CARD_BG
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.HexColor("#E3E7F5")
            ),

            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),

            (
                "LEFTPADDING",
                (0, 0),
                (-1, -1),
                8
            ),

            (
                "RIGHTPADDING",
                (0, 0),
                (-1, -1),
                8
            ),

            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                9
            ),

            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                9
            )

        ])

    )


    story.append(general_table)

    story.append(Spacer(1, 15))


    # =========================================================
    # HTTPS / SSL / DNS
    # =========================================================

    story.append(

        Paragraph(
            "🔐 Network & Encryption",
            section_style
        )

    )


    https = report.get("https", False)

    ssl_info = report.get("ssl", {})

    ssl_valid = ssl_info.get(
        "valid",
        False
    )


    https_text = (
        "ENABLED ✓"
        if https
        else
        "DISABLED ✕"
    )


    ssl_text = (
        "VALID ✓"
        if ssl_valid
        else
        "INVALID / UNAVAILABLE ✕"
    )


    dns_text = report.get(
        "dns",
        "Unknown"
    )


    network_data = [

        [
            Paragraph(
                "<b>HTTPS</b>",
                small_style
            ),

            Paragraph(
                https_text,
                value_style
            ),

            Paragraph(
                "<b>SSL Certificate</b>",
                small_style
            ),

            Paragraph(
                ssl_text,
                value_style
            )
        ],

        [
            Paragraph(
                "<b>DNS Status</b>",
                small_style
            ),

            Paragraph(
                str(dns_text),
                normal_style
            ),

            Paragraph(
                "<b>IP Address</b>",
                small_style
            ),

            Paragraph(
                str(report.get("ip", "Unknown")),
                value_style
            )
        ]

    ]


    network_table = Table(

        network_data,

        colWidths=[
            30 * mm,
            53 * mm,
            34 * mm,
            57 * mm
        ]

    )


    network_table.setStyle(

        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (-1, -1),
                CARD_BG
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.HexColor("#E3E7F5")
            ),

            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),

            (
                "LEFTPADDING",
                (0, 0),
                (-1, -1),
                8
            ),

            (
                "RIGHTPADDING",
                (0, 0),
                (-1, -1),
                8
            ),

            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                9
            ),

            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                9
            )

        ])

    )


    story.append(network_table)

    story.append(Spacer(1, 15))


    # =========================================================
    # SECURITY HEADERS
    # =========================================================

    story.append(

        Paragraph(
            "🛡 Security Headers",
            section_style
        )

    )


    enabled = report.get(
        "enabled_headers",
        []
    )


    missing = report.get(
        "missing_headers",
        []
    )


    header_score = report.get(
        "header_score",
        "N/A"
    )


    header_rows = [

        [
            Paragraph("<b>Header</b>", normal_style),
            Paragraph("<b>Status</b>", normal_style)
        ]

    ]


    for header in enabled:

        header_rows.append(

            [
                Paragraph(
                    str(header),
                    normal_style
                ),

                Paragraph(
                    "Enabled ✓",
                    value_style
                )
            ]

        )


    for header in missing:

        header_rows.append(

            [
                Paragraph(
                    str(header),
                    normal_style
                ),

                Paragraph(
                    "Missing ✕",
                    normal_style
                )
            ]

        )


    if len(header_rows) == 1:

        header_rows.append(

            [
                Paragraph(
                    "No security header data available",
                    normal_style
                ),

                Paragraph(
                    "N/A",
                    normal_style
                )
            ]

        )


    header_table = Table(

        header_rows,

        colWidths=[
            120 * mm,
            54 * mm
        ],

        repeatRows=1

    )


    header_table.setStyle(

        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                PURPLE
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                WHITE
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.HexColor("#D9DDED")
            ),

            (
                "BACKGROUND",
                (0, 1),
                (-1, -1),
                CARD_BG
            ),

            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),

            (
                "LEFTPADDING",
                (0, 0),
                (-1, -1),
                8
            ),

            (
                "RIGHTPADDING",
                (0, 0),
                (-1, -1),
                8
            ),

            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                7
            ),

            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                7
            )

        ])

    )


    story.append(header_table)

    story.append(Spacer(1, 8))


    story.append(

        Paragraph(
            f"<b>Security Headers Score:</b> "
            f"{header_score}/100",
            normal_style
        )

    )

    story.append(Spacer(1, 15))


    # =========================================================
    # SECURITY ASSESSMENT
    # =========================================================
    story.append(PageBreak())
    story.append(

        Paragraph(
            "⚡ Security Assessment",
            section_style
        )

    )


    protection = report.get(
        "protection",
        0
    )


    attack_probability = report.get(
        "attack_probability",
        0
    )


    risk = report.get(
        "risk",
        "Unknown"
    )


    score_data = [

        [
            Paragraph(
                "PROTECTION",
                small_style
            ),

            Paragraph(
                "RISK PROBABILITY",
                small_style
            ),

            Paragraph(
                "RISK LEVEL",
                small_style
            )
        ],

        [
            Paragraph(
                f"{protection}%",
                center_value
            ),

            Paragraph(
                f"{attack_probability}%",
                center_value
            ),

            Paragraph(
                str(risk),
                center_value
            )
        ]

    ]


    score_table = Table(

        score_data,

        colWidths=[
            58 * mm,
            58 * mm,
            58 * mm
        ]

    )


    score_table.setStyle(

        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (-1, -1),
                CARD_BG
            ),

            (
                "BOX",
                (0, 0),
                (-1, -1),
                0.8,
                PURPLE
            ),

            (
                "INNERGRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.HexColor("#E3E7F5")
            ),

            (
                "ALIGN",
                (0, 0),
                (-1, -1),
                "CENTER"
            ),

            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),

            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                10
            ),

            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                10
            )

        ])

    )


    story.append(score_table)

    story.append(Spacer(1, 15))


    # =========================================================
    # RECOMMENDATIONS
    # =========================================================

    story.append(

        Paragraph(
            "💡 Security Recommendations",
            section_style
        )

    )


    recommendations = report.get(
        "recommendations",
        []
    )


    if recommendations:

        recommendation_rows = []


        for recommendation in recommendations:

            recommendation_rows.append(

                [
                    Paragraph(
                        "•",
                        value_style
                    ),

                    Paragraph(
                        str(recommendation),
                        normal_style
                    )
                ]

            )


        recommendation_table = Table(

            recommendation_rows,

            colWidths=[
                8 * mm,
                166 * mm
            ]

        )


        recommendation_table.setStyle(

            TableStyle([

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    CARD_BG
                ),

                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.HexColor("#E3E7F5")
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP"
                ),

                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    8
                ),

                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    8
                ),

                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    7
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    7
                )

            ])

        )


        story.append(
            recommendation_table
        )


    else:

        story.append(

            Paragraph(
                "No specific recommendations generated.",
                normal_style
            )

        )


    story.append(Spacer(1, 20))


    # =========================================================
    # FOOTER
    # =========================================================

    footer = Table(

        [[
            Paragraph(
                "CyberShield Analyzer • Security Assessment Report",
                small_style
            )
        ]],

        colWidths=[174 * mm]

    )


    footer.setStyle(

        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (-1, -1),
                LIGHT_BG
            ),

            (
                "ALIGN",
                (0, 0),
                (-1, -1),
                "CENTER"
            ),

            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                8
            ),

            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                8
            )

        ])

    )


    story.append(footer)


    # =========================================================
    # BUILD PDF
    # =========================================================

    doc.build(story)