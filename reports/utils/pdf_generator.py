import io
from django.conf import settings
from django.utils.timezone import localtime
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    Image as RLImage, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus.flowables import HRFlowable
import os

COLOR_PRIMARY = HexColor('#1a237e')
COLOR_ACCENT = HexColor('#283593')
COLOR_LIGHT = HexColor('#e8eaf6')

def add_header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(HexColor('#666666'))
    canvas.drawString(72, 40, "KCMBI Church Mission Report - Official Document")
    canvas.drawRightString(A4[0] - 72, 40, f"Generated: {localtime().strftime('%d-%b-%Y %H:%M')}")
    canvas.restoreState()

def draw_field(canvas, doc):
    add_header_footer(canvas, doc)

def generate_preacher_pdf(instance):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            topMargin=60, bottomMargin=60,
                            leftMargin=50, rightMargin=50)
    styles = getSampleStyleSheet()
    story = []

    title_style = ParagraphStyle('Title', parent=styles['Title'],
                                  fontSize=20, textColor=COLOR_PRIMARY,
                                  spaceAfter=6, alignment=TA_CENTER,
                                  fontName='Helvetica-Bold')
    subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'],
                                     fontSize=10, textColor=HexColor('#555555'),
                                     alignment=TA_CENTER, spaceAfter=20)

    story.append(Paragraph("KCMBI CHURCH MISSION REPORT", title_style))
    story.append(Paragraph("Preacher Personal Information", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=COLOR_PRIMARY, spaceAfter=15))

    label_style = ParagraphStyle('Label', parent=styles['Normal'],
                                  fontSize=10, textColor=HexColor('#333333'),
                                  fontName='Helvetica-Bold')
    value_style = ParagraphStyle('Value', parent=styles['Normal'],
                                  fontSize=10, textColor=HexColor('#000000'))

    data = [
        [Paragraph("Field", label_style), Paragraph("Details", label_style)],
        [Paragraph("Name of Preacher", value_style), Paragraph(instance.name_of_preacher, value_style)],
        [Paragraph("Team Leader", value_style), Paragraph(instance.team_leader_name, value_style)],
        [Paragraph("Cell Number", value_style), Paragraph(instance.cell_number, value_style)],
        [Paragraph("Preacher Address", value_style), Paragraph(instance.preacher_address, value_style)],
        [Paragraph("Congregation Address", value_style), Paragraph(instance.congregation_address, value_style)],
        [Paragraph("Email Address", value_style), Paragraph(instance.email_address, value_style)],
        [Paragraph("Bank Name", value_style), Paragraph(instance.bank_name, value_style)],
        [Paragraph("Account Number", value_style), Paragraph(instance.account_number, value_style)],
        [Paragraph("IFSC Code", value_style), Paragraph(instance.ifsc_code, value_style)],
    ]

    col_widths = [150, 340]
    table = Table(data, colWidths=col_widths, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BACKGROUND', (0, 1), (-1, -1), HexColor('#f5f5f5')),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor('#ffffff'), HexColor('#f9f9f9')]),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(table)
    story.append(Spacer(1, 20))

    if instance.preacher_photo and os.path.exists(instance.preacher_photo.path):
        story.append(Paragraph("Preacher Photo", label_style))
        story.append(Spacer(1, 6))
        img = RLImage(instance.preacher_photo.path, width=2*inch, height=2.5*inch)
        story.append(img)
        story.append(Spacer(1, 10))

    if instance.aadhar_card_photo and os.path.exists(instance.aadhar_card_photo.path):
        story.append(Paragraph("Aadhar Card Photo", label_style))
        story.append(Spacer(1, 6))
        img = RLImage(instance.aadhar_card_photo.path, width=3*inch, height=2*inch)
        story.append(img)

    story.append(Spacer(1, 30))


    doc.build(story, onFirstPage=draw_field, onLaterPages=draw_field)
    buffer.seek(0)
    return buffer

def generate_teamleader_pdf(instance):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            topMargin=60, bottomMargin=60,
                            leftMargin=50, rightMargin=50)
    styles = getSampleStyleSheet()
    story = []

    title_style = ParagraphStyle('Title', parent=styles['Title'],
                                  fontSize=20, textColor=COLOR_PRIMARY,
                                  spaceAfter=6, alignment=TA_CENTER,
                                  fontName='Helvetica-Bold')
    subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'],
                                     fontSize=10, textColor=HexColor('#555555'),
                                     alignment=TA_CENTER, spaceAfter=20)

    story.append(Paragraph("KCMBI CHURCH MISSION REPORT", title_style))
    story.append(Paragraph("Team Leader Personal Data", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=COLOR_PRIMARY, spaceAfter=15))

    label_style = ParagraphStyle('Label', parent=styles['Normal'],
                                  fontSize=10, textColor=HexColor('#333333'),
                                  fontName='Helvetica-Bold')
    value_style = ParagraphStyle('Value', parent=styles['Normal'],
                                  fontSize=10, textColor=HexColor('#000000'))

    data = [
        [Paragraph("Field", label_style), Paragraph("Details", label_style)],
        [Paragraph("Name", value_style), Paragraph(instance.name, value_style)],
        [Paragraph("Address", value_style), Paragraph(instance.address, value_style)],
        [Paragraph("Email Address", value_style), Paragraph(instance.email_address, value_style)],
        [Paragraph("Cell Number", value_style), Paragraph(instance.cell_number, value_style)],
        [Paragraph("Date of Birth", value_style), Paragraph(instance.date_of_birth.strftime('%d-%b-%Y'), value_style)],
        [Paragraph("Bank Name", value_style), Paragraph(instance.bank_name, value_style)],
        [Paragraph("Account Number", value_style), Paragraph(instance.account_number, value_style)],
        [Paragraph("IFSC Code", value_style), Paragraph(instance.ifsc_code, value_style)],
        [Paragraph("KCMBIs Submitting", value_style), Paragraph(str(instance.number_of_kcmbis_submitting), value_style)],
    ]

    col_widths = [150, 340]
    table = Table(data, colWidths=col_widths, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BACKGROUND', (0, 1), (-1, -1), HexColor('#f5f5f5')),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor('#ffffff'), HexColor('#f9f9f9')]),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(table)
    story.append(Spacer(1, 20))

    if instance.team_leader_photo and os.path.exists(instance.team_leader_photo.path):
        story.append(Paragraph("Team Leader Photo", label_style))
        story.append(Spacer(1, 6))
        img = RLImage(instance.team_leader_photo.path, width=2*inch, height=2.5*inch)
        story.append(img)
        story.append(Spacer(1, 10))

    if instance.aadhar_card_photo and os.path.exists(instance.aadhar_card_photo.path):
        story.append(Paragraph("Aadhar Card Photo", label_style))
        story.append(Spacer(1, 6))
        img = RLImage(instance.aadhar_card_photo.path, width=3*inch, height=2*inch)
        story.append(img)

    story.append(Spacer(1, 30))


    doc.build(story, onFirstPage=draw_field, onLaterPages=draw_field)
    buffer.seek(0)
    return buffer

def generate_congregation_pdf(instance):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            topMargin=60, bottomMargin=60,
                            leftMargin=50, rightMargin=50)
    styles = getSampleStyleSheet()
    story = []

    title_style = ParagraphStyle('Title', parent=styles['Title'],
                                  fontSize=20, textColor=COLOR_PRIMARY,
                                  spaceAfter=6, alignment=TA_CENTER,
                                  fontName='Helvetica-Bold')
    subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'],
                                     fontSize=10, textColor=HexColor('#555555'),
                                     alignment=TA_CENTER, spaceAfter=20)

    story.append(Paragraph("KCMBI CHURCH MISSION REPORT", title_style))
    story.append(Paragraph("Congregation Update", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=COLOR_PRIMARY, spaceAfter=15))

    label_style = ParagraphStyle('Label', parent=styles['Normal'],
                                  fontSize=10, textColor=HexColor('#333333'),
                                  fontName='Helvetica-Bold')
    value_style = ParagraphStyle('Value', parent=styles['Normal'],
                                  fontSize=10, textColor=HexColor('#000000'),
                                  leading=14, spaceAfter=2)

    info_style = ParagraphStyle('InfoBox', parent=styles['Normal'],
                                 fontSize=10, textColor=HexColor('#1a237e'),
                                 leading=16, backColor=HexColor('#f0f0ff'),
                                 borderPadding=10, leftIndent=10, rightIndent=10)

    team_leader_name = instance.preacher_ref.team_leader_ref.name if instance.preacher_ref and instance.preacher_ref.team_leader_ref else 'N/A'
    data = [
        [Paragraph("Field", label_style), Paragraph("Details", label_style)],
        [Paragraph("Team Leader", value_style), Paragraph(team_leader_name, value_style)],
        [Paragraph("Zone", value_style), Paragraph(f"{instance.zone.zone_number} {instance.zone.zone_name or ''}" if instance.zone else 'N/A', value_style)],
        [Paragraph("Name of Preacher", value_style), Paragraph(instance.name_of_preacher, value_style)],
        [Paragraph("Name of Village", value_style), Paragraph(instance.name_of_village, value_style)],
        [Paragraph("Month of Reporting", value_style), Paragraph(instance.month_of_reporting, value_style)],
        [Paragraph("Bible Studies/Meetings", value_style), Paragraph(str(instance.bible_studies_meetings_count), value_style)],
        [Paragraph("Baptisms Count", value_style), Paragraph(str(instance.baptisms_count), value_style)],
        [Paragraph("Names of Baptized", value_style), Paragraph(instance.names_of_baptized_people or 'N/A', value_style)],
        [Paragraph("Church Members Count", value_style), Paragraph(str(instance.church_members_count), value_style)],
        [Paragraph("Benevolent Aid Received", value_style), Paragraph(f"Rs. {instance.benevolent_aid_received}", value_style)],
        [Paragraph("Average Weekly Giving", value_style), Paragraph(f"Rs. {instance.average_weekly_giving}", value_style)],
    ]

    col_widths = [150, 340]
    table = Table(data, colWidths=col_widths, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BACKGROUND', (0, 1), (-1, -1), HexColor('#f5f5f5')),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor('#ffffff'), HexColor('#f9f9f9')]),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(table)
    story.append(Spacer(1, 20))

    if instance.inspiring_stories:
        story.append(Paragraph("Inspiring Stories", label_style))
        story.append(Spacer(1, 4))
        story.append(Paragraph(instance.inspiring_stories, info_style))
        story.append(Spacer(1, 15))

    if instance.church_photo and os.path.exists(instance.church_photo.path):
        story.append(Paragraph("Church Photo", label_style))
        story.append(Spacer(1, 6))
        img = RLImage(instance.church_photo.path, width=4*inch, height=2.63*inch, hAlign='CENTER')
        story.append(img)
        story.append(Spacer(1, 15))

    if instance.other_photo and os.path.exists(instance.other_photo.path):
        story.append(PageBreak())
        img = RLImage(instance.other_photo.path, width=5.71*inch, height=8.86*inch, hAlign='CENTER')
        story.append(img)

    story.append(Spacer(1, 20))


    doc.build(story, onFirstPage=draw_field, onLaterPages=draw_field)
    buffer.seek(0)
    return buffer

def generate_fieldreport_pdf(instance):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            topMargin=60, bottomMargin=60,
                            leftMargin=50, rightMargin=50)
    styles = getSampleStyleSheet()
    story = []

    title_style = ParagraphStyle('Title', parent=styles['Title'],
                                  fontSize=20, textColor=COLOR_PRIMARY,
                                  spaceAfter=6, alignment=TA_CENTER,
                                  fontName='Helvetica-Bold')
    subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'],
                                     fontSize=10, textColor=HexColor('#555555'),
                                     alignment=TA_CENTER, spaceAfter=20)

    story.append(Paragraph("KCMBI CHURCH MISSION REPORT", title_style))
    story.append(Paragraph("KCMBI Field Report / Zone Field Report", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=COLOR_PRIMARY, spaceAfter=15))

    label_style = ParagraphStyle('Label', parent=styles['Normal'],
                                  fontSize=10, textColor=HexColor('#333333'),
                                  fontName='Helvetica-Bold')
    value_style = ParagraphStyle('Value', parent=styles['Normal'],
                                  fontSize=10, textColor=HexColor('#000000'))

    raw = instance.preachers_in_attendance or ''
    preachers_list = [n.strip() for n in raw.replace('\r\n', '\n').split('\n') if n.strip()]
    if len(preachers_list) <= 1:
        preachers_list = [n.strip() for n in raw.split(',') if n.strip()]
    preachers_formatted = '\n'.join(f'{i+1}. {name}' for i, name in enumerate(preachers_list)) if preachers_list else 'N/A'
    data = [
        [Paragraph("Field", label_style), Paragraph("Details", label_style)],
        [Paragraph("Team Leader", value_style), Paragraph(instance.team_leader, value_style)],
        [Paragraph("Zone", value_style), Paragraph(f'{instance.zone.zone_number} {instance.zone.zone_name or ""}' if instance.zone else 'N/A', value_style)],
        [Paragraph("Meeting Date & Time", value_style), Paragraph(localtime(instance.meeting_date_time).strftime('%d-%b-%Y %I:%M %p'), value_style)],
        [Paragraph("KCMBI Number", value_style), Paragraph(instance.kcmbi_number, value_style)],
        [Paragraph("Class Topic / Text", value_style), Paragraph(instance.class_topic_or_text, value_style)],
        [Paragraph("Meeting Address", value_style), Paragraph(instance.meeting_address, value_style)],
        [Paragraph("Preachers in Attendance", value_style), Paragraph(preachers_formatted, value_style)],
        [Paragraph("Group Concerns", value_style), Paragraph(instance.group_concerns or 'N/A', value_style)],
    ]

    col_widths = [150, 340]
    table = Table(data, colWidths=col_widths, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BACKGROUND', (0, 1), (-1, -1), HexColor('#f5f5f5')),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor('#ffffff'), HexColor('#f9f9f9')]),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(table)
    story.append(Spacer(1, 20))

    if instance.meeting_photo and os.path.exists(instance.meeting_photo.path):
        story.append(Paragraph("Meeting Photo", label_style))
        story.append(Spacer(1, 6))
        img = RLImage(instance.meeting_photo.path, width=4*inch, height=3*inch)
        story.append(img)

    story.append(Spacer(1, 30))


    doc.build(story, onFirstPage=draw_field, onLaterPages=draw_field)
    buffer.seek(0)
    return buffer

def generate_zone_pdf(instance):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            topMargin=60, bottomMargin=60,
                            leftMargin=50, rightMargin=50)
    styles = getSampleStyleSheet()
    story = []

    title_style = ParagraphStyle('Title', parent=styles['Title'],
                                  fontSize=20, textColor=COLOR_PRIMARY,
                                  spaceAfter=6, alignment=TA_CENTER,
                                  fontName='Helvetica-Bold')
    subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'],
                                     fontSize=10, textColor=HexColor('#555555'),
                                     alignment=TA_CENTER, spaceAfter=20)

    story.append(Paragraph("KCMBI CHURCH MISSION REPORT", title_style))
    story.append(Paragraph("Zone Details", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=COLOR_PRIMARY, spaceAfter=15))

    label_style = ParagraphStyle('Label', parent=styles['Normal'],
                                  fontSize=10, textColor=HexColor('#333333'),
                                  fontName='Helvetica-Bold')
    value_style = ParagraphStyle('Value', parent=styles['Normal'],
                                  fontSize=10, textColor=HexColor('#000000'))

    data = [
        [Paragraph("Field", label_style), Paragraph("Details", label_style)],
        [Paragraph("Zone Number", value_style), Paragraph(instance.zone_number, value_style)],
        [Paragraph("Zone Name", value_style), Paragraph(instance.zone_name or 'N/A', value_style)],
        [Paragraph("Team Leader", value_style), Paragraph(instance.team_leader.name, value_style)],
        [Paragraph("Location", value_style), Paragraph(instance.location or 'N/A', value_style)],
        [Paragraph("Description", value_style), Paragraph(instance.description or 'N/A', value_style)],
    ]

    col_widths = [150, 340]
    table = Table(data, colWidths=col_widths, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BACKGROUND', (0, 1), (-1, -1), HexColor('#f5f5f5')),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor('#ffffff'), HexColor('#f9f9f9')]),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(table)
    story.append(Spacer(1, 20))

    preachers = instance.preachers.all()
    if preachers:
        story.append(Paragraph("Preachers in this Zone", label_style))
        story.append(Spacer(1, 6))
        for p in preachers:
            story.append(Paragraph(f"  - {p.name_of_preacher} ({p.cell_number})", value_style))
        story.append(Spacer(1, 10))

    story.append(Spacer(1, 30))


    doc.build(story, onFirstPage=draw_field, onLaterPages=draw_field)
    buffer.seek(0)
    return buffer



