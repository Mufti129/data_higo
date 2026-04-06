from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(df, ci_age, ci_interest, filename="report_mufti.pdf"):

    styles = getSampleStyleSheet()
    story = []

    def add(text):
        story.append(Paragraph(text, styles["Normal"]))
        story.append(Spacer(1, 10))

    story.append(Paragraph("<b>Digital User Analysis Report</b>", styles["Title"]))
    story.append(Spacer(1, 20))

    add("<b>Nama:</b> Mufti")

    add("<b>Step 1:</b> Data Generation")
    add("<b>Step 2:</b> Feature Engineering")
    add("<b>Step 3:</b> Analysis")
    add("<b>Step 4:</b> Confidence Interval")

    add("<b>Statistical Summary</b>")
    add(f"Mean Umur: {ci_age['mean']:.2f}")
    add(f"CI Umur: ({ci_age['lower']:.2f}, {ci_age['upper']:.2f})")

    add(f"Mean Minat: {ci_interest['mean']:.2f}")
    add(f"CI Minat: ({ci_interest['lower']:.2f}, {ci_interest['upper']:.2f})")

    add("<b>Insights</b>")
    add("- Mayoritas user usia produktif")
    add("- Aktivitas dominan siang hari")
    add("- High interest = high potential")

    add("<b>Recommendation</b>")
    add("- Fokus campaign siang hari")
    add("- Target usia 25–40")
    add("- Prioritaskan high interest user")

    doc = SimpleDocTemplate(filename)
    doc.build(story)
